import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.work import exists as work_exists
    from ixtlilton_tools.admin.directory.user.work import is_empty as work_is_empty

    path = '/work/'+username

    if not work_exists(username):
        raise DirectoryConflict('The work directory of user {username} does not exists')
    else:
        if not work_is_empty(username):
            raise DirectoryConflict('The work directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
