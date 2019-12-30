# using the vertices and coordinates, create the blockmesh file in OF format:

# write the static directory for blockmesh (and any other files that are consistent across the simulation space in future):
import os
import shutil
from shutil import copyfile
from shutil import copy


def determine_working_directory():
    """Determine the current working directory"""
    current_dir = os.getcwd()
    print("Current directory from write_blockmesh mod:")
    print(current_dir)
    return current_dir

current_dir = determine_working_directory()


def create_static_file_folder(current_dir):
    """Create a static files folder for placing files that are not changed across the simulation space"""

    # NEED TO ADD SOME FUNCTIONALITY FOR IF THE FILE PATH ALREADY EXISTS IN THE SYSTEM
    static_foamfiles_folder = current_dir + "/" + "static_foamfiles"
    os.mkdir(static_foamfiles_folder)
    print("static_foamfiles_folder")
    print(static_foamfiles_folder)

create_static_file_folder(current_dir)

# Navigate to the static folder, create blockMeshDict file, write file.
# need to figure out the blocks by hand... ugh
