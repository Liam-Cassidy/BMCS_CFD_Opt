# Case setup: using the number of cases, (1) iteratively create subdirectories for each case simulated.
# (2) Create details files iteratively based on the case number (angle and flow rate in line one and 2 respectively--consider having a set number of figures for ease)

import os
import numpy as np
import shutil
from shutil import copytree
from shutil import copy


def create_simulations_folder():
    """Create a directory within the StoveSim master folder called simulations. This is where case folders will be created based on N-cases.
    Args:
        None
    Returns:
        simulation_folder_path (str): string with full path to simulation folder.
    """
    current_dir = os.getcwd()
    print("current directory:")
    print(current_dir)

    simulation_folder_name = "//simulations//"

    simulation_folder_path = current_dir + simulation_folder_name
    print("simulation_folder_path")
    print(simulation_folder_path)

    os.mkdir(simulation_folder_path)

    return simulation_folder_path

#simulation_folder_path = create_simulations_folder()

#N_simulations = 18

# use the number of cases determined (using angles and flow rates per user input) to iteratively create case_x folders.
# store full paths in an array (string elements) with N_simulations entries
# N_simulations is determined earlier.

def create_case_directories(N_simulations, simulation_folder_path):
    """Create case directories
    Args:
        N_simulations (int): Number of unique simulations in the study.
        simulation_folder_path (str): string with full path to simulation folder.


    Returns:
        case_path_array (array): 1D array full of string elemets pertaining to the full case folder paths.
        case_number_array (array): 1D array of case_i strings only
    """

    case_path_array = []
    case_number_array = []


    #added_dir = np.zeros((N_simulations,1), dtype=str)
    index = 0
    while index <= N_simulations:
        number_add = str(index)
        added_dir = "case_" + number_add
        case_number_array.append(added_dir)
        #print("added dir")
        #print(added_dir)
        case_path = simulation_folder_path + added_dir
        case_path_array.append(case_path)
        #print("case path i:")
        #print(case_path)
        os.mkdir(case_path)
        index=index+1

    print("full case path array:")
    print(case_path_array)

        #print("full case list:")
        #print(case_number_array)

    return case_number_array, case_path_array

#case_number_array, case_path_array = create_case_directories(N_simulations, simulation_folder_path)


# FROM BEFORE:
# pulling the velocity components from the array:
#Vx_RHS = Simulation_array_empty[:,5] # RHS x component.
#Vy_RHS = Simulation_array_empty[:,6]  # RHS y component.
#Vx_LHS = Simulation_array_empty[:,7]  # LHS x component.
#Vy_LHS = Simulation_array_empty[:,8]  # LHS y component.

def add_foam_directories(case_path_array, N_simulations):
    """Loop through the new case directories and add the system, constant, and 0 folder
    Args:
    case_full_paths (dict): list of full strings of case folders for future use
    k_tot (int): number of cases total written initially

    Returns:
    case_zero_paths (dict): list of the full paths for 0 foam paths
    case_system_paths (dict): list of the full paths for system foam paths
    case_constant_paths (dict): of the full paths for constant foam paths
    """

    constant_dir_add = "//constant//"
    system_dir_add = "//system//"
    zero_dir_add    = "//0//"
    TDAC_dir_add = "//TDAC//"

    #initialize paths
    case_zero_paths = []
    case_system_paths = []
    case_constant_paths = []
    case_TDAC_paths = []

    y = 0

    while y <= N_simulations:
        const = case_path_array[y] + constant_dir_add
        zero = case_path_array[y] + zero_dir_add
        system = case_path_array[y] + system_dir_add
        TDAC = case_path_array[y] + TDAC_dir_add

        # Make locate_directories
        #os.mkdir(const)
        #os.mkdir(zero)
        #os.mkdir(system)
        # add to dictionaries
        case_zero_paths.append(zero)
        case_system_paths.append(system)
        case_constant_paths.append(const)
        case_TDAC_paths.append(TDAC)

        y = y + 1
    #print("case_zero_paths dictionary")
    #print(case_zero_paths)
    #print("case_constant_paths dictionary")
    #print(case_constant_paths)
    #print("case_system_paths dictionary")
    #print(case_system_paths)
    return case_zero_paths, case_system_paths, case_constant_paths, case_TDAC_paths

#case_zero_paths, case_system_paths, case_constant_paths = add_foam_directories(case_full_paths, k_tot)

def paste_static_foam_files(case_zero_paths, case_system_paths, case_constant_paths, case_TDAC_paths, N_simulations):
    """copy and paste static OpenFOAM solver files into the constant, 0, system directories
    Location for static files is in StoveOpt master directory
    N_simulations (int): number of cases total written initially

    Args:
    case_zero_paths (array): list of the full paths for 0 foam paths
    case_system_paths (array): list of the full paths for system foam paths
    case_constant_paths (array): list of the full paths for constant foam paths
    case_TDAC_paths (array): list of full paths for TDAC case folders

    Returns:
    None
    """
    current_dir = os.getcwd()
    static_zero_files = current_dir + "//static_foam_files//" + "0"
    static_constant_files = current_dir + "//static_foam_files//" + "constant"
    static_system_files = current_dir + "//static_foam_files//" + "system"
    static_TDAC_files = current_dir + "//static_foam_files//" + "TDAC"

    # Copytree--Moves all contents from a directory to location specified
    # Loop will change the destination based on index, and paste from the static sources
    i = 0 # initialize loop
    while i <= N_simulations:
        copytree(static_zero_files, case_zero_paths[i])
        copytree(static_constant_files, case_constant_paths[i])
        copytree(static_system_files, case_system_paths[i])
        copytree(static_TDAC_files, case_TDAC_paths[i])

        i = i + 1

#paste_static_foam_files(case_zero_paths, case_system_paths, case_constant_paths, k_tot)






# Loop through the list of case_path_array and paste the static files required for the simulations, AND WRITE the cases that are dynamic. Should just be O/U/ files.
def populate_cases(case_path_array, N_simulations, Vx_RHS, Vy_RHS, Vx_LHS, Vy_LHS, foam_files_templates):
    """Loop through the list of case_path_array and paste the static files required for the simulations, AND WRITE the files that are dynamic: Should just be U-initial boundary_conditions
    at this point
    Args:
        case_path_array (array): 1D array full of string elemets pertaining to the full case folder paths.
        foam_files_templates (str): path where the OpenFOAM static files are. To be pasted into directories.
        case_number_array (array): 1D array of case_i strings only.

    Returns:
        case_U_paths (array): list of the U-boundary condition file paths.
    """
