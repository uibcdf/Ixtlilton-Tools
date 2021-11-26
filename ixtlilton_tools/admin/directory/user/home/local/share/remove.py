import pathlib
import shutil
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict

def remove(username):

    from ixtlilton_tools.admin.directory.user.home.local.share import exists as share_exists
    from ixtlilton_tools.admin.directory.user.home.local.share import is_empty as share_is_empty

    path = pathlib.Path('/home/'+username+'/local/share')

    if not share_exists(username):
        raise DirectoryConflict('The share directory of user {username} does not exists')
    else:
        if not share_is_empty(username):
            raise DirectoryConflict('The share directory of user {username} is not empty')
        else:
            shutil.rmtree(path)

    pass
