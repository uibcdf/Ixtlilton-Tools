import os
import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local import exists as local_exists
    from ixtlilton_tools.admin.directory.user.home.local import is_empty as local_is_empty

    path = pathlib.Path('/home/'+username+'/local')
    aux_path = pathlib.Path('/home/'+username+'/.local')

    if not local_exists(username):
        raise DirectoryConflict('The local directory of user {username} does not exists')
    else:
        if not local_is_empty(username):
            raise DirectoryConflict('The local directory of user {username} is not empty')
        else:
            os.unlink(path)
            shutil.rmtree(aux_path)

    pass

