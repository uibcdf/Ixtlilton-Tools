import os
import pathlib
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local.include import exists as include_exists
    from ixtlilton_tools.admin.directory.user.home.local.include import fix_owner as fix_include_owner

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local/include')

    if not include_exists(username):

        os.mkdir('/home/'+username+'/local/include')
        fix_include_owner(username)

    pass

