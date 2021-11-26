import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.src import exists as src_exists
    from ixtlilton_tools.admin.directory.user.home.local.src import is_empty as src_is_empty

    path = pathlib.Path('/home/'+username+'/local/src')

    if not src_exists(username):
        raise DirectoryConflict('The src directory of user {username} does not exists')
    else:
        if not src_is_empty(username):
            raise DirectoryConflict('The src directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
