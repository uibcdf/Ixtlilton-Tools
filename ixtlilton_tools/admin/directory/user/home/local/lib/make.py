import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib import exists as lib_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib import fix_owner as fix_lib_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/lib')

    if not lib_exists(username):

        os.mkdir('/home/'+username+'/local/lib')
        fix_lib_owner(username)

    pass

