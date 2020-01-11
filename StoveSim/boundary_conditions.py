# adapted from D:\Primary Air Material\Primary Air Literature Review\Scripts\mass_flow_fuel
Firepower = 5 # assumed  kW
LHV = 20
import os
from decimal import *

import cantera as ct
import numpy as np


getcontext().prec = 10
def calculate_fuel_mass_flow(Firepower, LHV):
    """Compute the mass flux to be assigned for each contributing surface of fuel body.
    Assumes 4 total fuel blocks, with 3/4 combustion chamber diameter as span, no flow from front and back faces, square cross section
        Args:
            Firepower (double): user-defined firepower for the analysis
            LHV (double): user-defined lower heating value for the Wood
        Returns:
            m_dot_fuel_total (double): mass flow rate for fuel
    """

    HV_unit_conv = LHV*1000 # Converted to kJ/kg
    getcontext().prec = 10
    m_dot_fuel_total = Decimal(Firepower)/Decimal(HV_unit_conv) # kg/s
    print('Total mass flow rate for given firepower (kg/s):'+"\n")
    print(m_dot_fuel_total)


    return m_dot_fuel_total

m_dot_fuel_total = calculate_fuel_mass_flow(Firepower, LHV)

def calculate_species_flow_rates(m_dot_fuel_total):
    """Calculate the mass flow rate of each of the volatile species.
    Volaile mass fractions are based on work from Udesen
    Args:
        m_dot_fuel_total (double): mass flow rate for fuel
    Returns:
        m_dot_frac_CO (double): mass flow rate of CO species.
        m_dot_frac_CO2 (double): mass flow rate of CO2 species.
        m_dot_frac_H2 (double): mass flow rate of H2 species.
        m_dot_frac_H2O (double): mass flow rate of H2O species.
        m_dot_frac_CH4 (double): mass flow rate of CH4 species.
    """

    w_CO = Decimal(0.383) # mass fraction of CO
    w_CO2 = Decimal(0.237) # mass fraction of CO2
    w_H2 = Decimal(0.006) # mass fraction of H2
    w_H2O = Decimal(0.312) # mass fraction of H20
    w_CH4 = Decimal(0.062) # mass fraction of CH4

    # Calculating mass flow rates
    m_dot_frac_CO = m_dot_fuel_total*w_CO
    m_dot_frac_CO2 = m_dot_fuel_total*w_CO2
    m_dot_frac_H2 = m_dot_fuel_total*w_H2
    m_dot_frac_H2O = m_dot_fuel_total*w_H2O
    m_dot_frac_CH4 = m_dot_fuel_total*w_CH4

    return m_dot_frac_CO, m_dot_frac_CO2, m_dot_frac_H2, m_dot_frac_H2O, m_dot_frac_CH4

m_dot_frac_CO, m_dot_frac_CO2, m_dot_frac_H2, m_dot_frac_H2O, m_dot_frac_CH4 = calculate_species_flow_rates(m_dot_fuel_total)

def write_primary_flow_to_bc_file(m_dot_frac_CO, m_dot_frac_CO2, m_dot_frac_H2, m_dot_frac_H2O, m_dot_frac_CH4, m_dot_fuel_total):
    """Open and write the primary flow to the boundary conditions file.
    Args:
        m_dot_fuel_total (double): mass flow rate for fuel
        m_dot_frac_CO (double): mass flow rate of CO species.
        m_dot_frac_CO2 (double): mass flow rate of CO2 species.
        m_dot_frac_H2 (double): mass flow rate of H2 species.
        m_dot_frac_H2O (double): mass flow rate of H2O species.
        m_dot_frac_CH4 (double): mass flow rate of CH4 species.
    """
    current_dir = os.getcwd()
    steps = "//boundary_conditions//boundary_conditions"
    write_file_dir = current_dir + steps

    with open(write_file_dir, 'r+') as f:
            f.write("fuel mass flow rate:"+"\n")
            f.write(str(m_dot_fuel_total))
            f.write("\n")
            f.write("CO mass flow rate:"+"\n")
            f.write(str(m_dot_frac_CO))
            f.write("\n")
            f.write("CO2 mass flow rate:"+"\n")
            f.write(str(m_dot_frac_CO2))
            f.write("\n")
            f.write("H2 mass flow rate:"+"\n")
            f.write(str(m_dot_frac_H2))
            f.write("\n")
            f.write("H2O mass flow rate:"+"\n")
            f.write(str(m_dot_frac_H2O))
            f.write("\n")
            f.write("CH4 mass flow rate:"+"\n")
            f.write(str(m_dot_frac_CH4))
            f.write("\n")

#write_primary_flow_to_bc_file(m_dot_frac_CO, m_dot_frac_CO2, m_dot_frac_H2, m_dot_frac_H2O, m_dot_frac_CH4, m_dot_fuel_total)




# Computing constant heat flux values for pot surface and walls:

def compute_flux_pot():
    """Computing the constant heat flux to a pot assuming nucleate pool boiling. The computation assumes the heat flux to the water is conservatively assumed to the at the minimum q_s flux from the Nukiyama pool boiling curve.
    Args:
        None.
    Returns:
        T_s (float): Constant surface temperature of pot.
    """

    T_sat = 373.15

    # Zuber correlation -- constants and thermophysical properties
    C = 0.09
    rho_v =0.5955 # kg/m3
    h_fg =2654 # kJ/kg
    g = 9.81 # m/s2
    sigma = 58.9/1000
    rho_liq = 957.9 #kg/m3


    q_flux_min = C*rho_v*h_fg*((g*sigma*(rho_liq-rho_v))/(rho_liq+rho_v)**2)**0.25

    print("recovered flux to pot (kW/m2):")
    print(q_flux_min)

    q_flux_min_corr = q_flux_min*1000

    print("recovered flux to pot (W/m2):")
    print(q_flux_min_corr)

    T_excess = 12 # K

    T_s = T_excess + T_sat

    # surface temp.
    print("Pot surface temperature")
    print(T_s)

compute_flux_pot()

def compute_primary_air_flow(Firepower):
    """Apply agenbroad method for estimating the intake flow rate
    Args:
        Firepower (double): user-defined firepower for the analysis
    Returns:
        m_dot_primary_air (double): mass flow rate of naturally entrained air (kg/s).
        mol_dot_primary_air (double): molar flow rate of naturally entrained air (mol/s).
    """
    cp_average = 1.099# kJ/kg-K
    Q_dot = Firepower # kJ/s (kW)
    T_amb = 300 # K
    T_h = 1300 # K

    m_dot_primary_air = (Q_dot)/(cp_average*(T_h - T_amb)) #kg/s

    mw_air = 0.018 #kg/mol

    mol_dot_primary_air = m_dot_primary_air/mw_air

    print("mass flow rate of air:")
    print(m_dot_primary_air)

    print("molar flow rate of primary air:")
    print(mol_dot_primary_air)

    return mol_dot_primary_air, m_dot_primary_air

mol_dot_primary_air, m_dot_primary_air = compute_primary_air_flow(Firepower)

# Looking at computing the primary inlet mixture -- Cantera.

def compute_primary_mixture(m_dot_frac_CO, m_dot_frac_CO2, m_dot_frac_H2, m_dot_frac_H2O, m_dot_frac_CH4, mol_dot_primary_air):
    """
    Mixing two streams using `Quantity` objects.

    In this example, air and methane are mixed in stoichiometric proportions. This
    is a simpler, steady-state version of the example ``reactors/mix1.py``.

    Since the goal is to simulate a continuous flow system, the mixing takes place
    at constant enthalpy and pressure.
    """


    gas = ct.Solution('gri30.xml')

    # Stream A (air)
    A = ct.Quantity(gas, constant='HP')
    A.TPX = 300.0, ct.one_atm, 'O2:0.21, N2:0.79'

    # Stream B (methane)
    B = ct.Quantity(gas, constant='HP')
    #B.TPX = 300.0, ct.one_atm, 'CH4:1'


    # Converting mass flow rates per species into molar flow rates:
    MW_CO = 0.02801 # kg/mol
    MW_CO2 = 0.04401 # kg/mol
    MW_H2 = 0.00201588 # kg/mol
    MW_H2O = 0.01802 # kg/mol
    MW_CH4 = 0.01604 # kg/mol

    # molar flow rates of fuel. (mol/s)
    mol_dot_co = m_dot_frac_CO/Decimal(MW_CO)
    mol_dot_co2 = m_dot_frac_CO2/Decimal(MW_CO2)
    mol_dot_h2 = m_dot_frac_H2/Decimal(MW_H2)
    mol_dot_h2o = m_dot_frac_H2O/Decimal(MW_H2O)
    mol_dot_ch4 = m_dot_frac_CH4/Decimal(MW_CH4)

    total_molar_flow_rate = mol_dot_co + mol_dot_co2 + mol_dot_h2 + mol_dot_h2 + mol_dot_h2o + mol_dot_ch4

    mol_frac_co = mol_dot_co/total_molar_flow_rate
    mol_frac_co2 = mol_dot_co2/total_molar_flow_rate
    mol_frac_h2 = mol_dot_h2/total_molar_flow_rate
    mol_frac_h2o = mol_dot_h2o/total_molar_flow_rate
    mol_frac_ch4 = mol_dot_ch4/total_molar_flow_rate

    print("total molar flow rate of fuel")
    print(total_molar_flow_rate)

    print("mole fraction co:")
    print(mol_frac_co)

    print("mole fraction co2:")
    print(mol_frac_co2)

    print("mol fraction of h2:")
    print(mol_frac_h2)

    print("mol fraction of h2o:")
    print(mol_frac_h2o)

    print("mole fraction of ch4:")
    print(mol_frac_ch4)


    B.TPX = 300.0, ct.one_atm, {'H2':mol_frac_h2, 'H2O':mol_frac_h2o, 'CH4':mol_frac_ch4, 'CO':mol_frac_co, 'CO2':mol_frac_co2}

    # Set molar flow rates:
    # CH4 + 2 O2 -> CO2 + 2 H2O

    # PREVIOUS LINES:
    #A.moles = 0.011 # mol/s
    #nO2 = A.X[A.species_index('O2')]

    # NEW LINES: air properties.
    mol_frac_n2_atm = 0.79
    mol_frac_o2_atm = 0.21
    A.TPX = 300.00, ct.one_atm, {'N2':mol_frac_n2_atm, 'O2':mol_frac_o2_atm}

    B.moles = float(total_molar_flow_rate)
    A.moles = float(mol_dot_primary_air) # chosen randomly for now.

    # Compute the mixed state
    M = A + B
    print(M.report())

    gas = M # assign the mixture to gas solution object

    # Show that this state corresponds to stoichiometric combustion
    gas.equilibrate('HP') # equilibrate the mixture with constant enthaly and pressure
    print(gas.report()) # print the gas solution object report

    mol_fractions = gas.X
    mol_fractions_numpy = np.array(mol_fractions)
    print(mol_fractions)

    #gas.write_csv('mol_fractions_numpy.csv', quiet=False)


    return mol_fractions_numpy


mol_fractions_numpy = compute_primary_mixture(m_dot_frac_CO, m_dot_frac_CO2, m_dot_frac_H2, m_dot_frac_H2O, m_dot_frac_CH4, mol_dot_primary_air)




# Figure out how to write out the species, fractions temperature data.
# create a loop and write outs for temperature, pressure, species mass fraction, species mol fractions.




#m_dot_fuel_total = calculate_fuel_mass_flow(firepower, LHV)


# working with the secondary inlet Definitions

# Let's put the Cantera mumbo jumbo in here
