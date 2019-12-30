# the purpose of the arg processor is to create the simulation matrix
import numpy as np
import math as mt

#lower_angle_design_value = 100
#upper_angle_design_value = 260

#number_of_flowrates_analyzed =  10 # unitless
#lower_flowrate_design_value = 0.01 # m3/s ---update with reasonable values from the UC berkely article
#upper_flowrate_design_value = 0.1 # m3/s
#Diameter_secondary_inlet = 0.01 # m


def create_1d_angle_array_RHS(number_of_angles_analyzed, lower_angle_design_value, upper_angle_design_value):
    """create 1D arrays for the angles under scrutiny per user input for each side of the stove
    Args:
        number_of_angles_analyzed (int): number of angles to be used in simulations
        lower_angle_design_value (double): lower limit for the 1D array of angles simulated
        upper_angle_design_value (double): upper limit for the 1D array of angles simulated
    Returns:
        rhs_angle_array (array): one-dimensional (1 column) array of angles analyzed for the RHS of domain
    """
    # Right hand side:
    step_rhs = (upper_angle_design_value - lower_angle_design_value)/(number_of_angles_analyzed-1)
    zero_rhs_array = np.zeros((number_of_angles_analyzed,1), dtype=float)
    print("empty zeros array")
    print(zero_rhs_array)

    # assign the first and last value to lower and upper limit
    zero_rhs_array[0] = lower_angle_design_value
    zero_rhs_array[number_of_angles_analyzed-1] = upper_angle_design_value
    print("empty zeros array after additions")
    print(zero_rhs_array)

    # Loop through and add value for index 1 through N-2 with the steps
    i = 1
    while i <= number_of_angles_analyzed - 2:
        zero_rhs_array[i] = zero_rhs_array[i-1] + step_rhs
        i = i + 1

    print("zero_rhs_array after looping")
    print(zero_rhs_array)

    # renaming to rhs_angle_array:
    rhs_angle_array = zero_rhs_array
    return rhs_angle_array, step_rhs, lower_angle_design_value, upper_angle_design_value

#rhs_angle_array, step_rhs, lower_angle_design_value, upper_angle_design_value = create_1d_angle_array_RHS(number_of_angles_analyzed, lower_angle_design_value, upper_angle_design_value)


def create_1d_angle_array_LHS(rhs_angle_array, step_rhs, lower_angle_design_value, upper_angle_design_value, number_of_angles_analyzed):
    """Creating the angle array for the LHS of the domain secondary inlet
    Args:
        angle_1d_array_RHS (array): one-dimensional (1 column) array of angles analyzed for the RHS of domain
        step_rhs (float): angular step between angle values
        lower_angle_design_value (double): lower limit for the 1D array of angles simulated
        upper_angle_design_value (double): upper limit for the 1D array of angles simulated
    Returns:
        lhs_angle_array (array): 1D array for lhs angles
    """

    # Assigning the first value to the array:
    lhs_angle_array = np.zeros((number_of_angles_analyzed,1), dtype=float)
    lhs_angle_array[0] = 90 - (lower_angle_design_value - 90)

    # looping through to the end:
    i = 1
    while i <= number_of_angles_analyzed - 1:
        lhs_angle_array[i] =   lhs_angle_array[i-1] - step_rhs
        i = i + 1

    print("lhs angle array")
    print(lhs_angle_array)

    return lhs_angle_array

#lhs_angle_array = create_1d_angle_array_LHS(rhs_angle_array, step_rhs, lower_angle_design_value, upper_angle_design_value)


def create_1D_velocity_magnitude_array_RHS(number_of_flowrates_analyzed, lower_flowrate_design_value, upper_flowrate_design_value, D_fd):
    """Goal is to create an array of velocity magnitudes. Will be used to create the velocity components in accordance with the angle arrays previously determined.
    Args:
        number_of_flowrates_analyzed (int): user-defined number of flow rates to simulate.
        lower_flowrate_design_value (float): lower limit flow rate defined.
        upper_flowrate_design_value (float): upper limit flow rate defined.
    Returns:
        RHS_velocity_magnitude_array (array): array of velocity magnitudes for RHS secondary inlet.
        LHS_velocity_magnitude_array (array): array of velocity magnitudes for LHS secondary inlet.
        mass_flow_rate_array (array): mass flow rates derived by the chosen flow rate field.
    """

    # declaring an empty mass flow rate array
    mass_flow_rate_array = np.zeros((number_of_flowrates_analyzed,1), dtype=float)
    rho_air = 1.225 # density air kg/m^3

    flow_rate_RHS_empty = np.zeros((number_of_flowrates_analyzed,1), dtype=float) # define empty array for flow rates (RHS)
    flow_rate_RHS_empty[0] = lower_flowrate_design_value # filling initial value with the defined lower limit value
    flow_rate_RHS_empty[number_of_flowrates_analyzed-1] = upper_flowrate_design_value # filling last entry with the defined upper limit

    # determining steps between flow rates:
    step_flowrate_rhs = (upper_flowrate_design_value - lower_flowrate_design_value)/(number_of_flowrates_analyzed-1)
    print("flowrate step")
    print(step_flowrate_rhs)

    # Looping through array and assigning intermediate values
    i = 1
    while i <= number_of_flowrates_analyzed - 2:
        flow_rate_RHS_empty[i] = flow_rate_RHS_empty[i-1] + step_flowrate_rhs
        i = i + 1

    print("flow rate array after looping:")
    print(flow_rate_RHS_empty)

    # Convert to velocity using user-defined secondary air flow rate
    area_secondary_inlet = (3.14159/4)*(D_fd**2) # secondary inlet cross sectional area m^2
    # Multiplying each np array entry with the area Q*A = V
    RHS_velocity_magnitude_array = flow_rate_RHS_empty*area_secondary_inlet
    print("RHS velocity magnitude following multiplication")
    print(RHS_velocity_magnitude_array)

    mass_flow_rate_array = rho_air*flow_rate_RHS_empty
    print("mass flow rate array:")
    print(mass_flow_rate_array)

    # setting the LHS equal to the RHS velocities:
    LHS_velocity_magnitude_array = RHS_velocity_magnitude_array

    return RHS_velocity_magnitude_array, LHS_velocity_magnitude_array, mass_flow_rate_array, flow_rate_RHS_empty

#RHS_velocity_magnitude_array, LHS_velocity_magnitude_array, mass_flow_rate_array, flow_rate_RHS_empty = create_1D_velocity_magnitude_array_RHS(number_of_flowrates_analyzed, lower_flowrate_design_value, upper_flowrate_design_value, Diameter_secondary_inlet)

def compute_number_of_simulations(number_of_flowrates_analyzed, number_of_angles_analyzed):
    """using the number of angles and flow rates described by user, calculate the number of unioque simulations.
    Args:
        number_of_angles_analyzed (int): user-defined number of  angles to be analyzed.
        number_of_flowrates_analyzed (int): user defined number of flow rates to be analyzed.
    Returns:
        N_simulations (int): Number of unique simulations to be run. Also the number of rows in the global simulation array.
    """

    N_simulations = number_of_angles_analyzed*number_of_flowrates_analyzed # for each flow rate, there are x number of simulations (x being number of angles_)
    print("number of unique simulations:")
    print(N_simulations)

    return N_simulations

#N_simulations = compute_number_of_simulations(number_of_flowrates_analyzed, number_of_angles_analyzed)

def create_empty_simulation_array(N_simulations):
    """Creating an empty global simulation array with 9 columns corresponding to case_number, Q_i, m_dot_i, V_mag, theta_rhs_i, theta_lhs_i, Vx_rhs_i, Vy_rhs_i, Vx_lhs_i, Vy_lhs_i. Creating an empty case number array to be merged later
    Args:
        N_simulations (int): Number of unique simulations to be run. Also the number of rows in the global simulation array.
    Returns:
        Simulation_array_empty (array): empty numpy array for the simulation field.
        case_number_array_empty (array): empty numpy array for case numbers.

    """
    # case number array:
    case_number_array_empty = np.zeros((N_simulations,1), dtype=str)
    print("case_number_array_empty:")
    print(case_number_array_empty)

    # For data type float
    Simulation_array_empty = np.zeros((N_simulations,9), dtype=float)
    print("simulation array empty:")
    print(Simulation_array_empty)

    return Simulation_array_empty, case_number_array_empty

#Simulation_array_empty, case_number_array_empty = create_empty_simulation_array(N_simulations)


def fill_simulation_array(Simulation_array_empty, RHS_velocity_magnitude_array, mass_flow_rate_array, lhs_angle_array, rhs_angle_array, number_of_flowrates_analyzed, number_of_angles_analyzed, flow_rate_RHS_empty):
    """goal is to fill the simulation array based on outer loop of flow rates (index k), and inner loop based on angles (index i).
    Args:
        Simulation_array_empty (array): empty numpy array for the simulation field.
        RHS_velocity_magnitude_array (array): array of velocity magnitudes for RHS secondary inlet.
        mass_flow_rate_array (array): mass flow rates derived by the chosen flow rate field.
        lhs_angle_array (array): 1D array for lhs angles
        rhs_angle_array (array): one-dimensional (1 column) array of angles analyzed for the RHS of domain
    Returns:
        Global_simulation_array (array): 2D array with all preconditioning variables for a cold flow analysis.
        Vx_RHS (array): 1D array for x-velocity components for RHS secondary inlet.
        Vy_RHS (array): 1D array for y-velocity components for RHS secondary inlet.
        Vx_LHS (array): 1D array for x-velocity components for LHS secondary inlet.
        Vy_LHS (array): 1D array for y-velocity components for LHS secondary inlet.


    """

    k = 0 # outer loop index for flow rates. --> upper index is number_of_flowrates_analyzed
    i = 0 # inner loop index for the angles. --> upper index is number_of_angles_analyzed

    # column 1 --> flow rate (k)
    # column 2 --> m_dot (k)
    # column 3 --> V_mag(k)
    # column 4 --> rhs_angle (i)
    # column 5 --> lhs_angle (i)
    # column 6 --> vx_rhs (i) COMPUTED
    # column 7 --> vy_rhs (i) COMPUTED
    # column 8 --> vx_lhs (i) COMPUTED
    # column 9 --> vy_lhs (i) COMPUTED

    print("flow rate rhs empty")
    print(flow_rate_RHS_empty)

    print("number of flow rate cases")
    print(number_of_flowrates_analyzed)

    counter = 0 # used to move the index iteratively down the array
    while k <= number_of_flowrates_analyzed-1:
        while i <= number_of_angles_analyzed-1:
            # c1
            Simulation_array_empty[counter,0] = flow_rate_RHS_empty[k]
            Simulation_array_empty[counter,1] = mass_flow_rate_array[k]
            Simulation_array_empty[counter,2] = RHS_velocity_magnitude_array[k]
            Simulation_array_empty[counter,3] = rhs_angle_array[i]
            Simulation_array_empty[counter,4] = lhs_angle_array[i]

            # converting angles to radians:
            rhs_angle_radians = mt.radians(rhs_angle_array[i])
            lhs_angle_radians = mt.radians(lhs_angle_array[i])

            # computing and filling components:
            Simulation_array_empty[counter,5] = RHS_velocity_magnitude_array[k]*mt.cos(rhs_angle_radians) # RHS x component.
            Simulation_array_empty[counter,6] = RHS_velocity_magnitude_array[k]*mt.sin(rhs_angle_radians) # RHS y component.
            Simulation_array_empty[counter,7] = RHS_velocity_magnitude_array[k]*mt.cos(lhs_angle_radians) # LHS x component.
            Simulation_array_empty[counter,8] = RHS_velocity_magnitude_array[k]*mt.sin(lhs_angle_radians) # LHS y component.

            counter = counter + 1 # this is the ROW NUMBER
            i = i + 1
        i = 0
        k = k + 1


    # pulling the velocity components from the array:
    Vx_RHS = Simulation_array_empty[:,5] # RHS x component.
    Vy_RHS = Simulation_array_empty[:,6]  # RHS y component.
    Vx_LHS = Simulation_array_empty[:,7]  # LHS x component.
    Vy_LHS = Simulation_array_empty[:,8]  # LHS y component.

    #print("Vx_RHS")
    #print(Vx_RHS)


    #print('simulation array after looping:')
    #print(Simulation_array_empty)

    # rename to Global_simulation_array
    Global_simulation_array = Simulation_array_empty


    return Global_simulation_array, Vx_RHS, Vy_RHS, Vx_LHS, Vy_LHS

#Global_simulation_array, Vx_RHS, Vy_RHS, Vx_LHS, Vy_LHS = fill_simulation_array(Simulation_array_empty, RHS_velocity_magnitude_array, mass_flow_rate_array, lhs_angle_array, rhs_angle_array, number_of_flowrates_analyzed, number_of_angles_analyzed, flow_rate_RHS_empty)
