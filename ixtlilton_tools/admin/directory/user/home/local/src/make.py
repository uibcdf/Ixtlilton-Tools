import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.src import exists as src_exists
    from ixtlilton_tools.admin.directory.user.home.local.src import fix_owner as fix_src_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/src')

    if not src_exists(username):

        os.mkdir('/home/'+username+'/local/src')
        fix_src_owner(username)

    pass

