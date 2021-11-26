import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.man import exists as man_exists
    from ixtlilton_tools.admin.directory.user.home.local.man import fix_owner as fix_man_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/man')

    if not man_exists(username):

        os.mkdir('/home/'+username+'/local/man')
        fix_man_owner(username)

    pass

