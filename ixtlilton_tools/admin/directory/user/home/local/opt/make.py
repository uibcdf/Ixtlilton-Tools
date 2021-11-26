import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt import exists as opt_exists
    from ixtlilton_tools.admin.directory.user.home.local.opt import fix_owner as fix_opt_owner
    from ixtlilton_tools.admin.directory.user.home.local.opt.modulefiles import make as make_modulefiles
    from ixtlilton_tools.admin.directory.user.home.local.opt.apps import make as make_apps
    from ixtlilton_tools.admin.directory.user.home.local.opt.src import make as make_src

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/opt')

    if not opt_exists(username):

        os.mkdir('/home/'+username+'/local/opt')
        fix_opt_owner(username)

        make_modulefiles(username)
        make_apps(username)
        make_src(username)

    pass

