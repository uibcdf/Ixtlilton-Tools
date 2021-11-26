import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.lib64 import exists as lib64_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib64 import is_empty as lib64_is_empty

    path = pathlib.Path('/home/'+username+'/local/lib64')

    if not lib64_exists(username):
        raise DirectoryConflict('The lib64 directory of user {username} does not exists')
    else:
        if not lib64_is_empty(username):
            raise DirectoryConflict('The lib64 directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
