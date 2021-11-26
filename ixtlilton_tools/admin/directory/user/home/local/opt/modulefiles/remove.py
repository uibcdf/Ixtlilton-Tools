import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.opt.modulefiles import exists as modulefiles_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt.modulefiles import is_empty as modulefiles_is_empty

    path = pathlib.Path('/home/'+username+'/local/opt/modulefiles')

    if not modulefiles_exists(username):
        raise DirectoryConflict('The modulefiles directory of user {username} does not exists')
    else:
        if not modulefiles_is_empty(username):
            raise DirectoryConflict('The modulefiles directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
