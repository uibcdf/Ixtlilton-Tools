import os
import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

initial_content=[]

def is_empty(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.bin import exists as bin_exists
    from ixtlilton_tools.admin.directory.user.home.local.bin import is_empty as bin_is_empty

    output = False

    if not bin_exists(username):
        raise DirectoryConflict('The bin directory of user {username} does not exists')
    else:
        path = pathlib.Path('/home/'+username+'/local/bin')
        if set(initial_content)==set(os.listdir(path)):
            output = True

    return output


