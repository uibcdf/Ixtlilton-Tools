import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt.apps import exists as apps_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt.apps import fix_owner as fix_apps_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/opt/apps')

    if not apps_exists(username):

        os.mkdir('/home/'+username+'/local/opt/apps')
        fix_apps_owner(username)

    pass

