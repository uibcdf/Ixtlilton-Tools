import os
import pathlib
import subprocess
import pandas as pd
import numpy as np
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, NoAdminRights

def fix(username, fullname=None, phone=None, mail=None, category=None):

    from ixtlilton_tools.admin import running_with_admin_rights
    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user import scratch, work, home

    if not running_with_admin_rights():
        raise NoAdminRights()

    if not user_exists(username):
        raise UserDoesNotExist(user=username)

    # gecos fields 

    if fullname is not None:
        subprocess.run(['chfn', '-f', fullname, username])

    if phone is not None:
        subprocess.run(['chfn', '-h', phone, username])

    if mail is not None:
        subprocess.run(['chfn', '-o', mail, username])

    # user directories

    work.make(username)
    work.fix_owner(username)

    scratch.make(username)
    scratch.fix_owner(username)

    home.local.make(username)
    home.local.fix_owner(username)

    home.local.bin.make(username)
    home.local.bin.fix_owner(username)

    home.local.etc.make(username)
    home.local.etc.fix_owner(username)

    home.local.include.make(username)
    home.local.include.fix_owner(username)

    home.local.lib.make(username)
    home.local.lib.fix_owner(username)

    home.local.lib32.make(username)
    home.local.lib32.fix_owner(username)

    home.local.man.make(username)
    home.local.man.fix_owner(username)

    home.local.share.make(username)
    home.local.share.fix_owner(username)

    home.local.src.make(username)
    home.local.src.fix_owner(username)

    home.local.opt.make(username)
    home.local.opt.fix_owner(username)

    home.local.opt.modulefiles.make(username)
    home.local.opt.modulefiles.fix_owner(username)

    home.local.opt.apps.make(username)
    home.local.opt.apps.fix_owner(username)

    pass

