import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.lib import exists as lib_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib import is_empty as lib_is_empty

    path = pathlib.Path('/home/'+username+'/local/lib')

    if not lib_exists(username):
        raise DirectoryConflict('The lib directory of user {username} does not exists')
    else:
        if not lib_is_empty(username):
            raise DirectoryConflict('The lib directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
