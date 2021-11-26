import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict
import subprocess

def fix_owner(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib64 import exists as lib64_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib64 import fix_owner as fix_lib64_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/lib64')

    if not lib64_exists(username):
        raise DirectoryConflict('The lib64 directory of user {username} does not exists')
    else:
        owner = path.owner()
        group = path.group()
        if owner!=username or group!=username:
            subprocess.run(['chown', '-R', f'{username}:{username}', str(path)])

    pass
