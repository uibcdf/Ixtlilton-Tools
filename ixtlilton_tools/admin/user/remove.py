import os
import pandas as pd
import numpy as np
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, NoAdminRights
import subprocess
import pathlib

def remove(username):

    from ixtlilton_tools.admin import running_with_admin_rights
    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user import scratch, work, home

    if not running_with_admin_rights():
        raise NoAdminRights()

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    ## removing user

    subprocess.run(['userdel', username])

    ## removing mailbox file

    path=pathlib.Path('/var/spool/mail/'+username)
    if path.exists():
        os.remove(path)

    ## removing directories if empty

    scratch.remove(username)
    work.remove(username)
    home.local.opt.modulefiles.remove(username)
    home.local.opt.apps.remove(username)
    home.local.opt.src.remove(username)
    home.local.opt.remove(username)
    home.local.bin.remove(username)
    home.local.etc.remove(username)
    home.local.lib.remove(username)
    home.local.lib32.remove(username)
    home.local.lib64.remove(username)
    home.local.include.remove(username)
    home.local.src.remove(username)
    home.local.share.remove(username)
    home.local.man.remove(username)
    home.local.remove(username)
    home.remove(username)
