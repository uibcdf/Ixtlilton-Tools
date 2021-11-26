import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib64 import exists as lib64_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib64 import fix_owner as fix_lib64_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/lib64')

    if not lib64_exists(username):

        os.mkdir('/home/'+username+'/local/lib64')
        fix_lib64_owner(username)

    pass

