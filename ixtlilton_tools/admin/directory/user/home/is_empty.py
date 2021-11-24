import os
import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

initial_content=['.mozilla', '.bash_logout', '.bash_profile', '.bashrc', '.emacs']

def is_empty(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home import exists as home_exists
    from ixtlilton_tools.admin.directory.user.home import is_empty as home_is_empty

    output = False

    if not home_exists(username):
        raise DirectoryConflict('The home directory of user {username} does not exists')
    else:
        path = pathlib.Path('/home/'+username)
        if set(initial_content)==set(os.listdir(path)):
            output = True

    return output


