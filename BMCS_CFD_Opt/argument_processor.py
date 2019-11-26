# The purpose of argument_processor is to determine the arguments that are to be varied and those that are static. Also, this is where the number of CFD jobs to be run are to be determined.


def arg_process(number):
    """Fake function for pytest"""
    number_added = number + 1
    return number_added
