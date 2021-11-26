import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt.modulefiles import exists as modulefiles_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt.modulefiles import fix_owner as fix_modulefiles_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/opt/modulefiles')

    if not modulefiles_exists(username):

        os.mkdir('/home/'+username+'/local/opt/modulefiles')
        fix_modulefiles_owner(username)

    pass

