import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.work import exists as work_exists
    from ixtlilton_tools.admin.directory.user.work import fix_owner as fix_work_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/work/'+username)

    if not work_exists(username):
        os.mkdir(path)
        fix_work_owner(username)

    pass
