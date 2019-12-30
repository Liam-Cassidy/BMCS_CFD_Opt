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

# boundary condition imports:
from boundary_conditions import calculate_fuel_mass_flow

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
import argument_processor

from argument_processor import arg_process

def main():
    """ Main script"""
    # Construct the argument parse and parse the arguments
    parser = argparse.ArgumentParser(description='BMCS_CFD_Opt')
    # File directory argument
    parser.add_argument('-v1','--variable_1', required=True, help='Please enter the first geometric or operational parameter to be varied for sake of optimization; NOTE, the input needs to exactly match that of the input file (e.g. Secondary_air_flow_rate)')
    parser.add_argument('-v2','--variable_2', required=False, help='Please enter the second geometric or operational parameter to be varied for sake of optimization; NOTE, the input needs to exactly match that of the input file (e.g. Secondary_air_flow_rate)')
    parser.add_argument('-o','--output_metric', required=True, help='Please enter the single output metric to be used for optimization: options include CO2_eq (CO2 equivalent emissions released at steady state), or q_pot (total heat transfer to pot)')
    parser.add_argument('-i','--inputfile', required=True, help='Please enter the full file path (directory and filename.extension) in Linux format for the input.yaml file in LINUX format. For example, /mnt/c/Oregon_State/Spring_2019/Soft_dev_eng/StoveOpt/StoveOpt/inputFiles/input.yaml')
    import sys
    args = parser.parse_args(sys.argv[1:])


    # Compute boundary conditions:
    m_dot_fuel_total = calculate_fuel_mass_flow(firepower, LHV) # fuel mass flow rate (kg/s)



    # Build the matrix for the cases
    # Col 1 is the case number, col 2 is secondary flow rates, and col 3 is the angles for the secondary inlet


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
