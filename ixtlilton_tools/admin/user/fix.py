import os
import pathlib
import subprocess
import pandas as pd
import numpy as np
from ixtlilton_tools._private_tools.exceptions import UserDoesNotExists, NoAdminRights

def fix(username, fullname=None, phone=None, mail=None, category=None):

    from ixtlilton_tools.admin import running_with_admin_rights
    from ixtlilton_tools.user import exists import user_exists

    if not running_with_admin_rights():
        raise NoAdminRights()

    if not user_exists(username):
        raise UserDoesNotExist()

    # gecos fields 

    if fullname is not None:
        subprocess.run(['chfn', '-f', fullname, username])

    if phone is not None:
        subprocess.run(['chfn', '-h', phone, username])

    if mail is not None:
        subprocess.run(['chfn', '-o', mail, username])

    # user directories

    for parent_dir in ['/work/', '/scratch/']:

        path = pathlib.Path(parent_dir+username)

        if not path.exists:
            os.mkdir(path)
        elif not path.is_dir():
            raise WorkDirectoryConflict('The work directory path is not a directory')

        owner = path.owner()
        group = path.group()
        print(f"{path.name} is owned by {owner}:{group}")

    pass

