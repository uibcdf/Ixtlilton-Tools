import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.etc import exists as etc_exists
    from ixtlilton_tools.admin.directory.user.home.local.etc import is_empty as etc_is_empty

    path = pathlib.Path('/home/'+username+'/local/etc')

    if not etc_exists(username):
        raise DirectoryConflict('The etc directory of user {username} does not exists')
    else:
        if not etc_is_empty(username):
            raise DirectoryConflict('The etc directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
