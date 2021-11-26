import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.etc import exists as etc_exists
    from ixtlilton_tools.admin.directory.user.home.local.etc import fix_owner as fix_etc_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/etc')

    if not etc_exists(username):

        os.mkdir('/home/'+username+'/local/etc')
        fix_etc_owner(username)

    pass

