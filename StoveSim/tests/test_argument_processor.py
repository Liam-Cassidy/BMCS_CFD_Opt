# tesing the argument processesor


def arg_process(number):
    """Fake function for pytest"""
    number_added = number + 1
    return number_added

def test_arg_process():
    number = 1
    number_added = arg_process(number)
    assert number_added == 2

test_arg_process()
