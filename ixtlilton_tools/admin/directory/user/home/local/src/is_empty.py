import os
import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

initial_content=[]

def is_empty(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.src import exists as src_exists
    from ixtlilton_tools.admin.directory.user.home.local.src import is_empty as src_is_empty

    output = False

    if not src_exists(username):
        raise DirectoryConflict('The src directory of user {username} does not exists')
    else:
        path = pathlib.Path('/home/'+username+'/local/src')
        if set(initial_content)==set(os.listdir(path)):
            output = True

    return output


