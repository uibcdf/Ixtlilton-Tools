import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home import exists as home_exists
    from ixtlilton_tools.admin.directory.user.home import is_empty as home_is_empty

    path = '/home/'+username

    if not home_exists(username):
        raise DirectoryConflict('The home directory of user {username} does not exists')
    else:
        if not home_is_empty(username):
            raise DirectoryConflict('The home directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
