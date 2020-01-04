# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:52:06 2019

@author: Lee
"""


#from import_geometry import *
import os
import fileinput
import shutil

""" Command line arguments:"""
# Import necessary packages
import sys
import argparse
import yaml
import time
from time import sleep


"""
import import_geometry
import create_blockmeshfile
import new_case_setup
import post_processor
import run_surrounding_cases
import case_setup
import create_controldict
import runner
import compute_coordinates
"""

# Importing all for now. change to explicit imports.
"""from import_geometry import *
from create_blockmeshfile import *
from run_surrounding_cases import *
from new_case_setup import *
from post_processor import *
from case_setup import *
from create_controldict import *
from runner import *
from compute_coordinates import *
"""
import readArgumentsRaw
from readArgumentsRaw import convert_namespace, pull_input_data


import argument_processor
from argument_processor import create_1d_angle_array_RHS, create_1d_angle_array_LHS, create_1D_velocity_magnitude_array_RHS, compute_number_of_simulations, create_empty_simulation_array, fill_simulation_array


import boundary_conditions
from boundary_conditions import calculate_fuel_mass_flow

import create_geometry
from create_geometry import compute_coordinates, concatenate_vertices_to_string

import write_blockmesh
from write_blockmesh import determine_working_directory, find_block_mesh_template, write_blockmesh, rename_block_mesh

import case_setup
from case_setup import create_simulations_folder, create_case_directories


def main():
    """ Main script"""
    # Construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser(description='StoveSim')
    # File directory argument
    parser.add_argument('-i','--inputfile', required=True, help='Please enter the full file path (directory and filename.extension) in Linux format for the input.yaml file in LINUX format. For example, /mnt/c/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/StoveOpt/inputFiles/input.yaml')
    import sys
    args = parser.parse_args(sys.argv[1:])

    # Reading arguments raw
    input_file = convert_namespace(args)
    D_fd, H_fd, Dc, H_cc, L_channel, L_deck, h_deck_pot, W_gap, number_of_angles_analyzed, number_of_flowrates_analyzed, lower_angle_design_value, lower_flowrate_design_value, upper_angle_design_value, upper_flowrate_design_value, Firepower, LHV = pull_input_data(input_file)

    print("D_fd test:")
    print(D_fd)

    # Compute boundary conditions:
    m_dot_fuel_total = calculate_fuel_mass_flow(Firepower, LHV) # fuel mass flow rate (kg/s)

    print("mdot fuel after BC mod")
    print(m_dot_fuel_total)

    # ARGUMUENT PROCESSOR: extract the angle/flow rate definitions and create global simulation array. Fill array with
    rhs_angle_array, step_rhs, lower_angle_design_value, upper_angle_design_value = create_1d_angle_array_RHS(number_of_angles_analyzed, lower_angle_design_value, upper_angle_design_value)
    lhs_angle_array = create_1d_angle_array_LHS(rhs_angle_array, step_rhs, lower_angle_design_value, upper_angle_design_value, number_of_angles_analyzed)
    RHS_velocity_magnitude_array, LHS_velocity_magnitude_array, mass_flow_rate_array, flow_rate_RHS_empty = create_1D_velocity_magnitude_array_RHS(number_of_flowrates_analyzed, lower_flowrate_design_value, upper_flowrate_design_value, D_fd)
    N_simulations = compute_number_of_simulations(number_of_flowrates_analyzed, number_of_angles_analyzed)
    Simulation_array_empty, case_number_array_empty = create_empty_simulation_array(N_simulations)
    Global_simulation_array, Vx_RHS, Vy_RHS, Vx_LHS, Vy_LHS = fill_simulation_array(Simulation_array_empty, RHS_velocity_magnitude_array, mass_flow_rate_array, lhs_angle_array, rhs_angle_array, number_of_flowrates_analyzed, number_of_angles_analyzed, flow_rate_RHS_empty)

    print("Firepower prior to BC:")
    print(Firepower)


    # Creating geometry:
    pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z = compute_coordinates(Dc, D_fd, H_fd, H_cc, W_gap, h_deck_pot, L_channel)

    # Build the matrix for the cases
    # Col 1 is the case number, col 2 is secondary flow rates, and col 3 is the angles for the secondary inlet

    # Convert to strings:
    pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str = concatenate_vertices_to_string(pt_0_x, pt_0_y, pt_0_z, pt_1_x, pt_1_y, pt_1_z, pt_2_x, pt_2_y, pt_2_z, pt_3_x, pt_3_y, pt_3_z, pt_4_x, pt_4_y, pt_4_z, pt_5_x, pt_5_y, pt_5_z, pt_6_x, pt_6_y, pt_6_z, pt_7_x, pt_7_y, pt_7_z, pt_8_x, pt_8_y, pt_8_z, pt_9_x, pt_9_y, pt_9_z, pt_10_x, pt_10_y, pt_10_z, pt_11_x, pt_11_y, pt_11_z, pt_12_x, pt_12_y, pt_12_z, pt_13_x, pt_13_y, pt_13_z, pt_14_x, pt_14_y, pt_14_z, pt_15_x, pt_15_y, pt_15_z, pt_16_x, pt_16_y, pt_16_z, pt_17_x, pt_17_y, pt_17_z, pt_18_x, pt_18_y, pt_18_z, pt_19_x, pt_19_y, pt_19_z, pt_20_x, pt_20_y, pt_20_z, pt_21_x, pt_21_y, pt_21_z, pt_22_x, pt_22_y, pt_22_z, pt_23_x, pt_23_y, pt_23_z, pt_24_x, pt_24_y, pt_24_z, pt_25_x, pt_25_y, pt_25_z, pt_26_x, pt_26_y, pt_26_z, pt_27_x, pt_27_y, pt_27_z, pt_28_x, pt_28_y, pt_28_z, pt_29_x, pt_29_y, pt_29_z, pt_30_x, pt_30_y, pt_30_z, pt_31_x, pt_31_y, pt_31_z)


    # Mesh writing:
    current_dir = determine_working_directory()
    block_mesh_template_path, foam_files_templates = find_block_mesh_template(current_dir)
    write_blockmesh(block_mesh_template_path, pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str)
    blockMeshDict_for_run = rename_block_mesh(block_mesh_template_path, foam_files_templates)


    # case_setup mod
    simulation_folder_path = create_simulations_folder()
    case_number_array, case_path_array = create_case_directories(N_simulations, simulation_folder_path)




    # Create X number of results matrices: col 1 is case number, col 2 is the secondary flow rate, col 3 is the secondary angle, col 4 is the respective dependent variable being tracked


    # Create a geometry and mesh --> pull this entirely from the previous work, woohoo!


    # loop through the simulations, pull data from the post processing of the case, place values iteratively in the CORRECT results matrix col 4


    # plot results in matlplotlib



    # Ensure the args all work-->string vs non string, slash variations, quotation marks
    #correct_arguments(args)
    print('args printed:')
    print(args)

if __name__ == "__main__":
    main()
