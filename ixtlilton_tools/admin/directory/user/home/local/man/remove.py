import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.man import exists as man_exists
    from ixtlilton_tools.admin.directory.user.home.local.man import is_empty as man_is_empty

    path = pathlib.Path('/home/'+username+'/local/man')

    if not man_exists(username):
        raise DirectoryConflict('The man directory of user {username} does not exists')
    else:
        if not man_is_empty(username):
            raise DirectoryConflict('The man directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
