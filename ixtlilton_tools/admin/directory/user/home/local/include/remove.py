import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.include import exists as include_exists
    from ixtlilton_tools.admin.directory.user.home.local.include import is_empty as include_is_empty

    path = pathlib.Path('/home/'+username+'/local/include')

    if not include_exists(username):
        raise DirectoryConflict('The include directory of user {username} does not exists')
    else:
        if not include_is_empty(username):
            raise DirectoryConflict('The include directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
