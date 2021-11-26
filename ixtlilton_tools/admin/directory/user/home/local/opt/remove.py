import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.opt import exists as opt_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt import is_empty as opt_is_empty

    path = pathlib.Path('/home/'+username+'/local/opt')

    if not opt_exists(username):
        raise DirectoryConflict('The opt directory of user {username} does not exists')
    else:
        if not opt_is_empty(username):
            raise DirectoryConflict('The opt directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
