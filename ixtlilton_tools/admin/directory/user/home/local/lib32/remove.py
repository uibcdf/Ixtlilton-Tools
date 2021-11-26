import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.lib32 import exists as lib32_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib32 import is_empty as lib32_is_empty

    path = pathlib.Path('/home/'+username+'/local/lib32')

    if not lib32_exists(username):
        raise DirectoryConflict('The lib32 directory of user {username} does not exists')
    else:
        if not lib32_is_empty(username):
            raise DirectoryConflict('The lib32 directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
