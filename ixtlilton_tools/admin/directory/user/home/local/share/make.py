import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.share import exists as share_exists
    from ixtlilton_tools.admin.directory.user.home.local.share import fix_owner as fix_share_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/share')

    if not share_exists(username):

        os.mkdir('/home/'+username+'/local/share')
        fix_share_owner(username)

    pass

