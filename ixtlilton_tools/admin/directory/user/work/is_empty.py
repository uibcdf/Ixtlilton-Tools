import os
import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

initial_content=[]

def is_empty(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.work import exists as work_exists
    from ixtlilton_tools.admin.directory.user.work import is_empty as work_is_empty

    output = False

    if not work_exists(username):
        raise DirectoryConflict('The work directory of user {username} does not exists')
    else:
        path = pathlib.Path('/work/'+username)
        if set(initial_content)==set(os.listdir(path)):
            output = True

    return output


