# adapted from D:\Primary Air Material\Primary Air Literature Review\Scripts\mass_flow_fuel


Firepower = 5 # kW -- > will be taken from the input file
LHV = 20 # MJ/kg --> will be taken from the input file

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
    m_dot_fuel_total = firepower/HV_unit_conv # kg/s
    print('Total mass flow rate for given firepower (kg/s):'+"\n")
    print(m_dot_fuel_total)

    return m_dot_fuel_total

calculate_fuel_mass_flow(firepower, LHV)


# working with the secondary inlet Definitions
