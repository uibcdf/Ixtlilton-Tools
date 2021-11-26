import os
import pathlib
import subprocess
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist

def make(username):

    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user.home.local import exists as local_exists
    from ixtlilton_tools.admin.directory.user.home.local import fix_owner as fix_local_owner
    from ixtlilton_tools.admin.directory.user.home.local.bin import make as make_local_bin
    from ixtlilton_tools.admin.directory.user.home.local.etc import make as make_local_etc
    from ixtlilton_tools.admin.directory.user.home.local.opt import make as make_local_opt
    from ixtlilton_tools.admin.directory.user.home.local.include import make as make_local_include
    from ixtlilton_tools.admin.directory.user.home.local.lib import make as make_local_lib
    from ixtlilton_tools.admin.directory.user.home.local.lib32 import make as make_local_lib32
    from ixtlilton_tools.admin.directory.user.home.local.lib64 import make as make_local_lib64
    from ixtlilton_tools.admin.directory.user.home.local.man import make as make_local_man
    from ixtlilton_tools.admin.directory.user.home.local.share import make as make_local_share
    from ixtlilton_tools.admin.directory.user.home.local.src import make as make_local_src

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    path = pathlib.Path('/home/'+username+'/local')
    aux_path = pathlib.Path('/home/'+username+'/.local')

    if not local_exists(username):

        if not aux_path.exists():
            os.mkdir(aux_path)
            subprocess.run(['chown', '-R', f'{username}:{username}', str(aux_path)])

        os.symlink('/home/'+username+'/.local', path, target_is_directory = True)
        fix_local_owner(username)

        make_local_bin(username)
        make_local_etc(username)
        make_local_opt(username)
        make_local_include(username)
        make_local_lib(username)
        make_local_lib32(username)
        make_local_lib64(username)
        make_local_man(username)
        make_local_share(username)
        make_local_src(username)

    pass

