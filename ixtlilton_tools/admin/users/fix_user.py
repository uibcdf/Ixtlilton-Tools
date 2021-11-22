import pandas as pd
import numpy as np
from ixtlilton_tools._private_tools.exceptions import NoUIDsAvailable, NoAdminRights
from ixtlilton_tools.admin import running_with_admin_rights
from ixtlilton_tools.admin import generate_random_password

def fix_user(username, fullname=None, phone=None, mail=None, category=None):

    if not running_with_admin_rights():
        raise NoAdminRights()


    if fullname is not None:
        subprocess.run(['chfn', '-f', full_name, username])

    if phone is not None:
        subprocess.run(['chfn', '-w', phone, username])

    if mail is not None:
        subprocess.run(['chfn', '-o', mail, username])

    pass

