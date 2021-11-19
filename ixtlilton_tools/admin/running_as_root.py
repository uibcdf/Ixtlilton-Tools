import os

def running_as_root():

    return 0==os.getuid()
