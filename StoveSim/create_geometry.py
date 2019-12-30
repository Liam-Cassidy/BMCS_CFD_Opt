# Create the geometry prior to meshing
# Using geometry definitions from the input file for the geometry calcs.

# required:
Dc = 0.1
D_fd = 0.01
H_fd = 0.05
H_cc = 0.1
W_gap = 0.03
h_deck_pot = 0.01
L_channel = 0.1

def compute_coordinates(Dc, D_fd, H_fd, H_cc, W_gap, h_deck_pot, L_channel):
    """Use raw input values to calculate the vertices for the domain
    Args:


    Returns:

    """
    # setting shift equal to 0.01
    shift = 0.01

    pt_0_x = 0
    pt_0_y = 0
    pt_0_z = 0
    pt_1_x = Dc
    pt_1_y = 0
    pt_1_z = 0
    pt_2_x = 0
    pt_2_y = H_fd-0.5*D_fd
    pt_2_z = 0
    pt_3_x = Dc
    pt_3_y = H_fd - 0.5*D_fd
    pt_3_z = 0
    pt_4_x = 0
    pt_4_y = H_fd + 0.5*D_fd
    pt_4_z = 0
    pt_5_x = Dc
    pt_5_y = H_fd + 0.5*D_fd
    pt_5_z = 0
    pt_6_x = 0
    pt_6_y = H_cc
    pt_6_z = 0
    pt_7_x = Dc
    pt_7_y = H_cc
    pt_7_z = 0
    pt_8_x = 0
    pt_8_y = H_cc + h_deck_pot
    pt_8_z = 0
    pt_9_x = Dc
    pt_9_y = H_cc + h_deck_pot
    pt_9_z = 0
    pt_10_x = -1*W_gap
    pt_10_y = H_cc + h_deck_pot
    pt_10_z = 0
    pt_11_x = Dc + W_gap
    pt_11_y = H_cc + h_deck_pot
    pt_11_z = 0
    pt_12_x = -1*W_gap
    pt_12_y = H_cc + h_deck_pot + L_channel
    pt_12_z = 0
    pt_13_x = Dc + W_gap
    pt_13_y = H_cc + h_deck_pot + L_channel
    pt_13_z = 0
    pt_14_x = 0
    pt_14_y = H_cc + h_deck_pot + L_channel
    pt_14_z = 0
    pt_15_x = Dc
    pt_15_y = H_cc + h_deck_pot + L_channel
    pt_15_z = 0

    # back points
    pt_16_x = pt_0_x
    pt_16_y = pt_0_y
    pt_16_z = shift
    pt_17_x = pt_1_x
    pt_17_y = pt_1_y
    pt_17_z = shift
    pt_18_x = pt_2_x
    pt_18_y = pt_2_y
    pt_18_z = shift
    pt_19_x = pt_3_x
    pt_19_y = pt_3_y
    pt_19_z = shift
    pt_20_x = pt_4_x
    pt_20_y = pt_4_y
    pt_20_z = shift
    pt_21_x = pt_5_x
    pt_21_y = pt_5_y
    pt_21_z = shift
    pt_22_x = pt_6_x
    pt_22_y = pt_6_y
    pt_22_z = shift
    pt_23_x = pt_7_x
    pt_23_y = pt_7_y
    pt_23_z = shift
    pt_24_x = pt_8_x
    pt_24_y = pt_8_y
    pt_24_z = shift
    pt_25_x = pt_9_x
    pt_25_y = pt_9_y
    pt_25_z = shift
    pt_26_x = pt_10_x
    pt_26_y = pt_10_y
    pt_26_z = shift
    pt_27_x = pt_11_x
    pt_27_y = pt_11_y
    pt_27_z = shift
    pt_28_x = pt_12_x
    pt_28_y = pt_12_y
    pt_28_z = shift
    pt_29_x = pt_13_x
    pt_29_y = pt_13_y
    pt_29_z = shift
    pt_30_x = pt_14_x
    pt_30_y = pt_14_y
    pt_30_z = shift
    pt_31_x = pt_15_x
    pt_31_y = pt_15_y
    pt_31_z = shift

    return pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z


pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z = compute_coordinates(Dc, D_fd, H_fd, H_cc, W_gap, h_deck_pot, L_channel)


def concatenate_vertices_to_string(pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z):
    """Convert the float format vertices to string length 5
    Args:
        pt_i_j (float): point number i, in coordinate direction j in float format.
    Returns:
        pt_i_j_str (str): point number i, in coordinate direction j in string format.
    """
    pt_0_x_str = str(pt_0_x)[:5]
    pt_0_y_str = str(pt_0_y)[:5]
    pt_0_z_str = str(pt_0_z)[:5]
    pt_1_x_str = str(pt_1_x)[:5]
    pt_1_y_str = str(pt_1_y)[:5]
    pt_1_z_str = str(pt_1_z)[:5]
    pt_2_x_str = str(pt_2_x)[:5]
    pt_2_y_str = str(pt_2_y)[:5]
    pt_2_z_str = str(pt_2_z)[:5]
    pt_3_x_str = str(pt_3_x)[:5]
    pt_3_y_str = str(pt_3_y)[:5]
    pt_3_z_str = str(pt_3_z)[:5]
    pt_4_x_str = str(pt_4_x)[:5]
    pt_4_y_str = str(pt_4_y)[:5]
    pt_4_z_str = str(pt_4_z)[:5]
    pt_5_x_str = str(pt_5_x)[:5]
    pt_5_y_str = str(pt_5_y)[:5]
    pt_5_z_str = str(pt_5_z)[:5]
    pt_6_x_str = str(pt_6_x)[:5]
    pt_6_y_str = str(pt_6_y)[:5]
    pt_6_z_str = str(pt_6_z)[:5]
    pt_7_x_str = str(pt_7_x)[:5]
    pt_7_y_str = str(pt_7_y)[:5]
    pt_7_z_str = str(pt_7_z)[:5]
    pt_8_x_str = str(pt_8_x)[:5]
    pt_8_y_str = str(pt_8_y)[:5]
    pt_8_z_str = str(pt_8_z)[:5]
    pt_9_x_str = str(pt_9_x)[:5]
    pt_9_y_str = str(pt_9_y)[:5]
    pt_9_z_str = str(pt_9_z)[:5]
    pt_10_x_str =str(pt_10_x)[:5]
    pt_10_y_str =str(pt_10_y)[:5]
    pt_10_z_str =str(pt_10_z)[:5]
    pt_11_x_str =str(pt_11_x)[:5]
    pt_11_y_str =str(pt_11_y)[:5]
    pt_11_z_str =str(pt_11_z)[:5]
    pt_12_x_str =str(pt_12_x)[:5]
    pt_12_y_str =str(pt_12_y)[:5]
    pt_12_z_str =str(pt_12_z)[:5]
    pt_13_x_str =str(pt_13_x)[:5]
    pt_13_y_str =str(pt_13_y)[:5]
    pt_13_z_str =str(pt_13_z)[:5]
    pt_14_x_str =str(pt_14_x)[:5]
    pt_14_y_str =str(pt_14_y)[:5]
    pt_14_z_str =str(pt_14_z)[:5]
    pt_15_x_str =str(pt_15_x)[:5]
    pt_15_y_str =str(pt_15_y)[:5]
    pt_15_z_str =str(pt_15_z)[:5]
    pt_16_x_str =str(pt_16_x)[:5]
    pt_16_y_str =str(pt_16_y)[:5]
    pt_16_z_str =str(pt_16_z)[:5]
    pt_17_x_str =str(pt_17_x)[:5]
    pt_17_y_str =str(pt_17_y)[:5]
    pt_17_z_str =str(pt_17_z)[:5]
    pt_18_x_str =str(pt_18_x)[:5]
    pt_18_y_str =str(pt_18_y)[:5]
    pt_18_z_str = str(pt_18_z)[:5]
    pt_19_x_str = str(pt_19_x)[:5]
    pt_19_y_str = str(pt_19_y)[:5]
    pt_19_z_str = str(pt_19_z)[:5]
    pt_20_x_str = str(pt_20_x)[:5]
    pt_20_y_str = str(pt_20_y)[:5]
    pt_20_z_str = str(pt_20_z)[:5]
    pt_21_x_str = str(pt_21_x)[:5]
    pt_21_y_str = str(pt_21_y)[:5]
    pt_21_z_str = str(pt_21_z)[:5]
    pt_22_x_str = str(pt_22_x)[:5]
    pt_22_y_str = str(pt_22_y)[:5]
    pt_22_z_str = str(pt_22_z)[:5]
    pt_23_x_str = str(pt_23_x)[:5]
    pt_23_y_str = str(pt_23_y)[:5]
    pt_23_z_str = str(pt_23_z)[:5]
    pt_24_x_str = str(pt_24_x)[:5]
    pt_24_y_str = str(pt_24_y)[:5]
    pt_24_z_str = str(pt_24_z)[:5]
    pt_25_x_str = str(pt_25_x)[:5]
    pt_25_y_str = str(pt_25_y)[:5]
    pt_25_z_str = str(pt_25_z)[:5]
    pt_26_x_str = str(pt_26_x)[:5]
    pt_26_y_str = str(pt_26_y)[:5]
    pt_26_z_str = str(pt_26_z)[:5]
    pt_27_x_str = str(pt_27_x)[:5]
    pt_27_y_str = str(pt_27_y)[:5]
    pt_27_z_str = str(pt_27_z)[:5]
    pt_28_x_str = str(pt_28_x)[:5]
    pt_28_y_str = str(pt_28_y)[:5]
    pt_28_z_str = str(pt_28_z)[:5]
    pt_29_x_str = str(pt_29_x)[:5]
    pt_29_y_str = str(pt_29_y)[:5]
    pt_29_z_str = str(pt_29_z)[:5]
    pt_30_x_str = str(pt_30_x)[:5]
    pt_30_y_str = str(pt_30_y)[:5]
    pt_30_z_str = str(pt_30_z)[:5]
    pt_31_x_str = str(pt_31_x)[:5]
    pt_31_y_str = str(pt_31_y)[:5]
    pt_31_z_str = str(pt_31_z)[:5]

    pt_0_str = "(" + pt_0_x_str + " " + pt_0_y_str + " " + pt_0_z_str + ")"
    pt_1_str = "(" + pt_1_x_str + " " + pt_1_y_str + " " + pt_1_z_str + ")"
    pt_2_str = "(" + pt_2_x_str + " " + pt_2_y_str + " " + pt_2_z_str + ")"
    pt_3_str = "(" + pt_3_x_str + " " + pt_3_y_str + " " + pt_3_z_str + ")"
    pt_4_str = "(" + pt_4_x_str + " " + pt_4_y_str + " " + pt_4_z_str + ")"
    pt_5_str = "(" + pt_5_x_str + " " + pt_5_y_str + " " + pt_5_z_str + ")"
    pt_6_str = "(" + pt_6_x_str + " " + pt_6_y_str + " " + pt_6_z_str + ")"
    pt_7_str = "(" + pt_7_x_str + " " + pt_7_y_str + " " + pt_7_z_str + ")"
    pt_8_str = "(" + pt_8_x_str + " " + pt_8_y_str + " " + pt_8_z_str + ")"
    pt_9_str = "(" + pt_9_x_str + " " + pt_9_y_str + " " + pt_9_z_str + ")"
    pt_10_str = "(" + pt_10_x_str + " " + pt_10_y_str + " " + pt_10_z_str + ")"
    pt_11_str = "(" + pt_11_x_str + " " + pt_11_y_str + " " + pt_11_z_str + ")"
    pt_12_str = "(" + pt_12_x_str + " " + pt_12_y_str + " " + pt_12_z_str + ")"
    pt_13_str = "(" + pt_13_x_str + " " + pt_13_y_str + " " + pt_13_z_str + ")"
    pt_14_str = "(" + pt_14_x_str + " " + pt_14_y_str + " " + pt_14_z_str + ")"
    pt_15_str = "(" + pt_15_x_str + " " + pt_15_y_str + " " + pt_15_z_str + ")"
    pt_16_str = "(" + pt_16_x_str + " " + pt_16_y_str + " " + pt_16_z_str + ")"
    pt_17_str = "(" + pt_17_x_str + " " + pt_17_y_str + " " + pt_17_z_str + ")"
    pt_18_str = "(" + pt_18_x_str + " " + pt_18_y_str + " " + pt_18_z_str + ")"
    pt_19_str = "(" + pt_19_x_str + " " + pt_19_y_str + " " + pt_19_z_str + ")"
    pt_20_str = "(" + pt_20_x_str + " " + pt_20_y_str + " " + pt_20_z_str + ")"
    pt_21_str = "(" + pt_21_x_str + " " + pt_21_y_str + " " + pt_21_z_str + ")"
    pt_22_str = "(" + pt_22_x_str + " " + pt_22_y_str + " " + pt_22_z_str + ")"
    pt_23_str = "(" + pt_23_x_str + " " + pt_23_y_str + " " + pt_23_z_str + ")"
    pt_24_str = "(" + pt_24_x_str + " " + pt_24_y_str + " " + pt_24_z_str + ")"
    pt_25_str = "(" +  pt_25_x_str + " " + pt_25_y_str + " " + pt_25_z_str + ")"
    pt_26_str = "(" +  pt_26_x_str + " " + pt_26_y_str + " " + pt_26_z_str + ")"
    pt_27_str = "(" +  pt_27_x_str + " " + pt_27_y_str + " " + pt_27_z_str + ")"
    pt_28_str = "(" +  pt_28_x_str + " " + pt_28_y_str + " " + pt_28_z_str + ")"
    pt_29_str = "(" +  pt_29_x_str + " " + pt_29_y_str + " " + pt_29_z_str + ")"
    pt_30_str = "(" +  pt_30_x_str + " " + pt_30_y_str + " " + pt_30_z_str + ")"
    pt_31_str = "(" +  pt_31_x_str + " " + pt_31_y_str + " " + pt_31_z_str + ")"


    return  pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str

pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str = concatenate_vertices_to_string(pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z)
