import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.bin import exists as bin_exists
    from ixtlilton_tools.admin.directory.user.home.local.bin import fix_owner as fix_bin_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/bin')

    if not bin_exists(username):

        os.mkdir('/home/'+username+'/local/bin')
        fix_bin_owner(username)

    pass

