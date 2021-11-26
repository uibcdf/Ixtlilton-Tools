import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.opt.apps import exists as apps_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt.apps import is_empty as apps_is_empty

    path = pathlib.Path('/home/'+username+'/local/opt/apps')

    if not apps_exists(username):
        raise DirectoryConflict('The apps directory of user {username} does not exists')
    else:
        if not apps_is_empty(username):
            raise DirectoryConflict('The apps directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
