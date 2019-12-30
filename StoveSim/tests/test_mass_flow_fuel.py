#  last update 12/29/2019


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
    m_dot_fuel_total = Firepower/HV_unit_conv # kg/s
    print('Total mass flow rate for given firepower (kg/s):'+"\n")
    print(m_dot_fuel_total)

    return m_dot_fuel_total


def test_mass_flow_fuel():
    """testing the calculate_fuel_mass_flow function"""
    LHV = 10
    Firepower = 5

    # Assigning a tolerance and expected value for the assertion
    tolerance = 0.1
    expected = 0.0005

    m_dot_fuel_total = calculate_fuel_mass_flow(Firepower, LHV)
    difference_abs = abs(m_dot_fuel_total-expected)
    assert difference_abs <= tolerance


test_mass_flow_fuel()
