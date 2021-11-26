import os
import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

initial_content=[]

def is_empty(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib64 import exists as lib64_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib64 import is_empty as lib64_is_empty

    output = False

    if not lib64_exists(username):
        raise DirectoryConflict('The lib64 directory of user {username} does not exists')
    else:
        path = pathlib.Path('/home/'+username+'/local/lib64')
        if set(initial_content)==set(os.listdir(path)):
            output = True

    return output


