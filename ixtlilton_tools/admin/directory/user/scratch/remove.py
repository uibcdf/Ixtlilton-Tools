import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.scratch import exists as scratch_exists
    from ixtlilton_tools.admin.directory.user.scratch import is_empty as scratch_is_empty

    path = '/scratch/'+username

    if not scratch_exists(username):
        raise DirectoryConflict('The scratch directory of user {username} does not exists')
    else:
        if not scratch_is_empty(username):
            raise DirectoryConflict('The scratch directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
