# the purpose of the arg processor is to create the simulation matrix
import numpy
number_of_angles_analyzed = 11
lower_angle_design_value = 100
upper_angle_design_value = 260


def create_1d_angle_array(number_of_angles_analyzed, lower_angle_design_value, upper_angle_design_value):
    """create 1D arrays for the angles under scrutiny per user input for each side of the stove
    Args:
        number_of_angles_analyzed (int): number of angles to be used in simulations
        lower_angle_design_value (double): lower limit for the 1D array of angles simulated
        upper_angle_design_value (double): upper limit for the 1D array of angles simulated
    Returns:
        angle_1d_array_RHS (array): one-dimensional (1 column) array of angles analyzed for the RHS of domain
        angle_1d_array_LHS (array): one-dimensional (1 column) array of angles analyzed for the LHS of domain

    """

    # Right hand side:
    step_rhs = (upper_angle_design_value - lower_angle_design_value)/(number_of_angles_analyzed-1)
    zero_rhs_array = np.zeros((5,1)), dtype=float)
    print("empty zeros array")


create_1d_angle_array(number_of_angles_analyzed, lower_angle_design_value, upper_angle_design_value)
