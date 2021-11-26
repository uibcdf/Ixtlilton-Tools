import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict
import subprocess

def fix_owner(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib import exists as lib_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib import fix_owner as fix_lib_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/lib')

    if not lib_exists(username):
        raise DirectoryConflict('The lib directory of user {username} does not exists')
    else:
        owner = path.owner()
        group = path.group()
        if owner!=username or group!=username:
            subprocess.run(['chown', '-R', f'{username}:{username}', str(path)])

    pass
