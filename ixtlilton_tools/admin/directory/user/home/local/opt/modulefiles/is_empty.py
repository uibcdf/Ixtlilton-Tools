import os
import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

initial_content=[]

def is_empty(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt.modulefiles import exists as modulefiles_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt.modulefiles import is_empty as modulefiles_is_empty

    output = False

    if not modulefiles_exists(username):
        raise DirectoryConflict('The modulefiles directory of user {username} does not exists')
    else:
        path = pathlib.Path('/home/'+username+'/local/opt/modulefiles')
        if set(initial_content)==set(os.listdir(path)):
            output = True

    return output


