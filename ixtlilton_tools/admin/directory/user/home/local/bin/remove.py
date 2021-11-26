import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.bin import exists as bin_exists
    from ixtlilton_tools.admin.directory.user.home.local.bin import is_empty as bin_is_empty

    path = pathlib.Path('/home/'+username+'/local/bin')

    if not bin_exists(username):
        raise DirectoryConflict('The bin directory of user {username} does not exists')
    else:
        if not bin_is_empty(username):
            raise DirectoryConflict('The bin directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
