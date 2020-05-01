import numpy
import yaml
import sys
import argparse
import xlrd
import time
from time import sleep

def convert_namespace(args):
    """Purpose is to convert the namespace from the args to a pure input file for reading

    Args:
        args (namespace): Argument provided by user on command fuel_vertice_concatenate

    Returns:

        input_file (string): Outputs the input file extracted from the name space. Location of the input file provided by user.

    """
    input_file = args.inputfile


    return input_file


def pull_input_data(input_file):
    """
    Goal is to convert the geometry file argument to working syntax: Single quote, back slash

    Args:
        args (dictionary): Object contains the contents of the input file specified by the user
    Returns:
        D_fd (double): Diameter of secondary inlet, defined by user.
        H_fd (double): Height of centerline of secondary inlet, defined by user.
        Dc (double): Combustion chamber diameter, defined by user.
        H_cc (double): Height of combustion chamber, defined by user.
        L_channel (double): Length of channel/skirt/shield, defined by user.
        L_deck (double): Length of cone deck, defined by user.
        h_deck_pot (double): Pot spacing from cone deck, defined by user.
        number_of_angles_analyzed (int): Number og angles to analyze defined by user
        lower_angle_design_value (float): lower limit for angles.
        upper_angle_design_value (float): upper limit for angles analyzed.
        number_of_flowrates_analyzed (int): number of flow rates analyzed.
        lower_flowrate_design_value (float): lower limit of flow rates simulated.
        upper_flowrate_design_value (float): upper limit of flow rates simulated.
        Firepower (float): firepower used to compute fuel release rate.
        LHV (float): lower heating value of wood.
    """

    with open(input_file, 'r') as f:
        doc = yaml.load(f)

        # Stove geometry Definitions
        Dc = doc['case']['Combustion_chamber_diameter']
        H_cc = doc['case']['Combustion_chamber_height']
        L_deck = doc['case']['Length_cone_deck']
        h_deck_pot = doc['case']['Height_cone_deck']
        D_fd = doc['case']['Diameter_secondary_inlet']
        H_fd = doc['case']['Height_secondary_inlet']

        # secondary flow settings
        number_of_angles_analyzed = doc['case']['number_of_angles_analyzed']
        lower_angle_design_value = doc['case']['lower_angle_design_value']
        upper_angle_design_value = doc['case']['upper_angle_design_value']
        number_of_flowrates_analyzed = doc['case']['number_of_flowrates_analyzed']
        lower_flowrate_design_value = doc['case']['lower_flowrate_design_value']
        upper_flowrate_design_value = doc['case']['upper_flowrate_design_value']

        # firepower and primary gas release
        Firepower = doc['case']['firepower']
        LHV = doc['case']['Lower_heating_value']

    return  D_fd, H_fd, Dc, H_cc, L_deck, h_deck_pot, number_of_angles_analyzed, number_of_flowrates_analyzed, lower_angle_design_value, lower_flowrate_design_value, upper_angle_design_value, upper_flowrate_design_value, Firepower, LHV
