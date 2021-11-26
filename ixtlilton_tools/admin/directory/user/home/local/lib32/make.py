import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib32 import exists as lib32_exists
    from ixtlilton_tools.admin.directory.user.home.local.lib32 import fix_owner as fix_lib32_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/lib32')

    if not lib32_exists(username):

        os.mkdir('/home/'+username+'/local/lib32')
        fix_lib32_owner(username)

    pass

