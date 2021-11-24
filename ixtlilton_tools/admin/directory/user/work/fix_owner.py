import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, DirectoryConflict
import subprocess

def fix_owner(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.work import exists as work_exists
    from ixtlilton_tools.admin.directory.user.work import fix_owner as fix_work_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/work/'+username)

    if not work_exists(username):
        raise DirectoryConflict('The work directory of user {username} does not exists')
    else:
        owner = path.owner()
        group = path.group()
        if owner!=username or group!=username:
            subprocess.run(['chown', '-R', f'{username}:{username}', str(path)])

    pass
