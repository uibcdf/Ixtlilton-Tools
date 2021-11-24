import os
import pathlib
import subprocess
import pandas as pd
import numpy as np
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, NoAdminRights

def fix(username, fullname=None, phone=None, mail=None, category=None):

    from ixtlilton_tools.admin import running_with_admin_rights
    from ixtlilton_tools.admin.user import exists as user_exists
    from ixtlilton_tools.admin.directory.user import scratch, work

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

    pass

