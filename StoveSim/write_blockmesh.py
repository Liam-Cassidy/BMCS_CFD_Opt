# using the vertices and coordinates, create the blockmesh file in OF format:

# write the static directory for blockmesh (and any other files that are consistent across the simulation space in future):
import os
import shutil
from shutil import copyfile
from shutil import copy
import sys


def determine_working_directory():
    """Determine the current working directory"""
    current_dir = os.getcwd()
    print("Current directory from write_blockmesh mod:")
    print(current_dir)
    return current_dir

#current_dir = determine_working_directory()


def find_block_mesh_template(current_dir):
    """Create a static files folder for placing files that are not changed across the simulation space
    Args:
        current_dir (str): Current working directory.
    Returns:
        block_mesh_template_path (str): full path where the block mesh template exists.
        foam_files_templates (str): where the template files exist. Will be used to create cases.

    """

    # NEED TO ADD SOME FUNCTIONALITY FOR IF THE FILE PATH ALREADY EXISTS IN THE SYSTEM
    foam_files_templates = current_dir + "//" + "foam_files_templates//"
    print("foam_files_templates directory")
    print(foam_files_templates)


    # Edit the blockmesh template:
    block_mesh_template_fname = "blockMeshDict_template"

    # full path:
    block_mesh_template_path = foam_files_templates + "system//" + block_mesh_template_fname
    print("blockmesh full path:")
    print(block_mesh_template_path)

    return block_mesh_template_path, foam_files_templates

#block_mesh_template_path, foam_files_templates = find_block_mesh_template(current_dir)


def write_blockmesh(block_mesh_template_path, pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str):
    """Open up the blockmesh template, write the full blockmesh, rename to blockMeshDict.

    """
    print("block mesh template path before writing")
    print(block_mesh_template_path)
    with open(block_mesh_template_path, 'r+') as f:
            f.seek(602) #where writing begins
            f.write("convertToMeters 1;"+"\n")
            f.write("\n")
            f.write("vertices"+"\n")
            f.write("("+"\n")

            f.write(pt_0_str +'\n')
            f.write(pt_1_str +'\n')
            f.write(pt_2_str+'\n')
            f.write(pt_3_str+'\n')
            f.write(pt_4_str+'\n')
            f.write(pt_5_str+'\n')
            f.write(pt_6_str+'\n')
            f.write(pt_7_str+'\n')
            f.write(pt_8_str+'\n')
            f.write(pt_9_str+'\n')
            f.write(pt_10_str+'\n')
            f.write(pt_11_str+'\n')
            f.write(pt_12_str+'\n')
            f.write(pt_13_str+'\n')
            f.write(pt_14_str+'\n')
            f.write(pt_15_str+'\n')
            f.write(pt_16_str+'\n')
            f.write(pt_17_str+'\n')
            f.write(pt_18_str+'\n')
            f.write(pt_19_str+'\n')
            f.write(pt_20_str+'\n')
            f.write(pt_21_str+'\n')
            f.write(pt_22_str +'\n')
            f.write(pt_23_str +'\n')
            f.write(pt_24_str+'\n')
            f.write(pt_25_str+'\n')
            f.write(pt_26_str+'\n')
            f.write(pt_27_str+'\n')
            f.write(pt_28_str+'\n')
            f.write(pt_29_str+'\n')
            f.write(pt_30_str+'\n')
            f.write(pt_31_str+'\n')

            f.write("\n")
            f.write(");"+"\n")
            f.write("\n")
            f.write("blocks"+"\n")
            f.write("(")
            f.write("\n")

            num_cells_int_str_concat = "(5 5 5)" # going with this for now

            f.write("hex (0 1 17 16 2 3 19 18) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (2 3 19 18 4 5 21 20) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (4 5 21 20 6 7 23 22) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (6 7 23 22 8 9 25 24) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (6 6 22 22 10 8 24 26) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (7 7 23 23 9 11 27 25) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (10 8 24 26 12 14 30 28) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (9 11 27 25 15 13 29 31) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")

            f.write(");" + "\n")
            f.write("\n")

            # edges
            f.write("edges" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("\n")

            # boundaries:
            f.write("boundary" + "\n")
            f.write("(" + "\n")

            # LHS outlet
            f.write("outlet_LHS" + "\n")
            f.write("{" + "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(12 14 30 28)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # RHS outlet
            f.write("outlet_RHS" + "\n")
            f.write("{" + "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(15 13 29 31)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air RHS
            f.write("secondary_air_RHS"+ "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(3 19 21 5)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air LHS
            f.write("secondary_air_LHS" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(2 18 20 4)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # Primary air inlets
            f.write("primary_inlet"+"\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 1 17 16)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Stove Body
            f.write("stove_body" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 16 18 2)" + "\n")
            f.write("(1 17 19 3)" + "\n")
            f.write("(4 20 22 6)" + "\n")
            f.write("(5 21 23 7)" + "\n")
            f.write("(6 22 22 6)" + "\n")
            f.write("(7 23 23 7)" + "\n")
            f.write("(11 27 29 13)" + "\n")
            f.write("(9 25 31 15)" + "\n")
            f.write("(8 24 30 14)" + "\n")
            f.write("(10 26 28 12)" + "\n")
            f.write("(8 9 25 24)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Empty front and back faces
            f.write("\n")
            f.write("frontAndBack" + "\n")
            f.write("{" + "\n")
            f.write("type empty;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 1 3 2)" + "\n")
            f.write("(16 17 19 18)" + "\n")
            f.write("(2 3 5 4)" + "\n")
            f.write("(18 19 21 20)" + "\n")
            f.write("(4 5 7 6)" + "\n")
            f.write("(20 21 23 22)" + "\n")
            f.write("(6 7 9 8)" + "\n")
            f.write("(22 23 25 24)" + "\n")
            #f.write("(10 6 8 10)" + "\n")
            #f.write("(26 22 24 26)" + "\n")
            #f.write("(7 11 9 7)" + "\n")
            #f.write("(23 27 25 23)" + "\n")
            f.write("(10 8 14 12)" + "\n")
            f.write("(26 24 30 28)" + "\n")
            f.write("(9 11 13 15)" + "\n")
            f.write("(25 27 29 31)" + "\n")

            f.write(");" + "\n")
            f.write("}" + "\n")
            f.write(");" + "\n")
            f.write("\n")
            f.write("mergePatchPairs" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("// ************************************************************************* //")

#write_blockmesh(block_mesh_template_path, pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str)


def write_blockmesh_2(block_mesh_template_path, pt_0_str, pt_1_str, pt_2_str, pt_3_str, pt_4_str, pt_5_str, pt_6_str, pt_7_str, pt_8_str, pt_9_str, pt_10_str, pt_11_str, pt_12_str, pt_13_str, pt_14_str, pt_15_str, pt_16_str, pt_17_str, pt_18_str, pt_19_str, pt_20_str, pt_21_str, pt_22_str, pt_23_str, pt_24_str, pt_25_str, pt_26_str, pt_27_str, pt_28_str, pt_29_str, pt_30_str, pt_31_str, pt_32_str, pt_33_str, pt_34_str, pt_35_str):
    """Changing mesh to not have the angle."""

    print("block mesh template path before writing")
    print(block_mesh_template_path)
    with open(block_mesh_template_path, 'r+') as f:
            f.seek(602) #where writing begins
            f.write("convertToMeters 1;"+"\n")
            f.write("\n")
            f.write("vertices"+"\n")
            f.write("("+"\n")

            f.write(pt_0_str +'\n')
            f.write(pt_1_str +'\n')
            f.write(pt_2_str+'\n')
            f.write(pt_3_str+'\n')
            f.write(pt_4_str+'\n')
            f.write(pt_5_str+'\n')
            f.write(pt_6_str+'\n')
            f.write(pt_7_str+'\n')
            f.write(pt_8_str+'\n')
            f.write(pt_9_str+'\n')
            f.write(pt_10_str+'\n')
            f.write(pt_11_str+'\n')
            f.write(pt_12_str+'\n')
            f.write(pt_13_str+'\n')
            f.write(pt_14_str+'\n')
            f.write(pt_15_str+'\n')
            f.write(pt_16_str+'\n')
            f.write(pt_17_str+'\n')
            f.write(pt_18_str+'\n')
            f.write(pt_19_str+'\n')
            f.write(pt_20_str+'\n')
            f.write(pt_21_str+'\n')
            f.write(pt_22_str +'\n')
            f.write(pt_23_str +'\n')
            f.write(pt_24_str+'\n')
            f.write(pt_25_str+'\n')
            f.write(pt_26_str+'\n')
            f.write(pt_27_str+'\n')
            f.write(pt_28_str+'\n')
            f.write(pt_29_str+'\n')
            f.write(pt_30_str+'\n')
            f.write(pt_31_str+'\n')
            f.write(pt_32_str+'\n')
            f.write(pt_33_str+'\n')
            f.write(pt_34_str+'\n')
            f.write(pt_35_str+'\n')

            f.write("\n")
            f.write(");"+"\n")
            f.write("\n")
            f.write("blocks"+"\n")
            f.write("(")
            f.write("\n")

            num_cells_int_str_concat = "(5 5 5)" # going with this for now

            f.write("hex (0 1 17 16 2 3 19 18) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (2 3 19 18 4 5 21 20) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (4 5 21 20 6 7 23 22) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (6 7 23 22 8 9 25 24) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            #f.write("hex (6 6 22 22 10 8 24 26) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n") PREVIOUS PRYRAMID MESHES
            #f.write("hex (7 7 23 23 9 11 27 25) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (32 6 22 33 10 8 24 26) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (7 34 35 23 9 11 27 25) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (10 8 24 26 12 14 30 28) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")
            f.write("hex (9 11 27 25 15 13 29 31) " + num_cells_int_str_concat + " " +   "simpleGrading (1 1 1)" + "\n")

            f.write(");" + "\n")
            f.write("\n")

            # edges
            f.write("edges" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("\n")

            # boundaries:
            f.write("boundary" + "\n")
            f.write("(" + "\n")

            # LHS outlet
            f.write("outlet_LHS" + "\n")
            f.write("{" + "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(12 14 30 28)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # RHS outlet
            f.write("outlet_RHS" + "\n")
            f.write("{" + "\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(15 13 29 31)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air RHS
            f.write("secondary_air_RHS"+ "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(3 19 21 5)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Secondary air LHS
            f.write("secondary_air_LHS" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(2 18 20 4)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            # Primary air inlets
            f.write("primary_inlet"+"\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 1 17 16)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Stove Body
            f.write("stove_body" + "\n")
            f.write("{"+"\n")
            f.write("type patch;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 16 18 2)" + "\n")
            f.write("(1 17 19 3)" + "\n")
            f.write("(4 20 22 6)" + "\n")
            f.write("(5 21 23 7)" + "\n")
            #f.write("(6 22 22 6)" + "\n") old walls from pyramid mesh
            #f.write("(7 23 23 7)" + "\n")
            f.write("(32 6 22 33)" + "\n")
            f.write("(32 33 26 10)" + "\n")
            f.write("(7 34 35 23)" + "\n")
            f.write("(34 35 27 11)" + "\n")

            f.write("(11 27 29 13)" + "\n")
            f.write("(9 25 31 15)" + "\n")
            f.write("(8 24 30 14)" + "\n")
            f.write("(10 26 28 12)" + "\n")
            f.write("(8 9 25 24)" + "\n")
            f.write(");" + "\n")
            f.write("}" + "\n")

            #Empty front and back faces
            f.write("\n")
            f.write("frontAndBack" + "\n")
            f.write("{" + "\n")
            f.write("type empty;" + "\n")
            f.write("faces" + "\n")
            f.write("(" + "\n")
            f.write("(0 1 3 2)" + "\n")
            f.write("(16 17 19 18)" + "\n")
            f.write("(2 3 5 4)" + "\n")
            f.write("(18 19 21 20)" + "\n")
            f.write("(4 5 7 6)" + "\n")
            f.write("(20 21 23 22)" + "\n")
            f.write("(6 7 9 8)" + "\n")
            f.write("(22 23 25 24)" + "\n")
            #f.write("(10 6 8 10)" + "\n")
            #f.write("(26 22 24 26)" + "\n")
            #f.write("(7 11 9 7)" + "\n")
            #f.write("(23 27 25 23)" + "\n")
            f.write("(10 8 14 12)" + "\n")
            f.write("(26 24 30 28)" + "\n")
            f.write("(9 11 13 15)" + "\n")
            f.write("(25 27 29 31)" + "\n")

            f.write(");" + "\n")
            f.write("}" + "\n")
            f.write(");" + "\n")
            f.write("\n")
            f.write("mergePatchPairs" + "\n")
            f.write("(" + "\n")
            f.write(");" + "\n")
            f.write("// ************************************************************************* //")




def rename_block_mesh(block_mesh_template_path, foam_files_templates):
    """rename the template to blockMeshDict, and leave in the templates folder for now.

    Args:
        block_mesh_template_path (str): full path of edited blockmesh template.
    Returns:
        blockMeshDict_for_run (str): renamed edited blockmesh, in template folder still.
    """

    system_folder = foam_files_templates + "system//"
    blockMeshDict_fname_for_run = "blockMeshDict"
    blockMeshDict_for_run = system_folder + blockMeshDict_fname_for_run

    copy(block_mesh_template_path, blockMeshDict_for_run)

    return blockMeshDict_for_run

def move_blockmesh_to_static_system_dir(blockMeshDict_for_run):
    """copy the edited blockmesh file into the static-system directory. The files will be copied in bulk over to each of the case directories during case setup.
    Args:
        blockMeshDict_for_run (str): renamed edited blockmesh, in template folder still.
    Returns:
        blockMeshDict_static (str): full path for the static-system-blockMeshDict location.
    """

    current_dir = os.getcwd() # StoveSim parent directory.
    static_system_steps = "//static_foam_files//system//blockMeshDict"
    blockMeshDict_static = current_dir + static_system_steps

    copy(blockMeshDict_for_run, blockMeshDict_static)

    return blockMeshDict_static






#blockMeshDict_for_run = rename_block_mesh(block_mesh_template_path, foam_files_templates)





# Figure out blocks by hand. Ugh
