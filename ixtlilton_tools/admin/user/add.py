import pandas as pd
import numpy as np
from ixtlilton_tools._private_tools.exceptions import NoUIDsAvailable, NoAdminRights
import subprocess

def add(username, fullname=None, phone=None, mail=None, category=None):

    from ixtlilton_tools.admin import running_with_admin_rights
    from ixtlilton_tools.admin import generate_random_password
    from ixtlilton_tools.admin import get_users
    from ixtlilton_tools.admin.user import fix as fix_user

    if not running_with_admin_rights():
        raise NoAdminRights()

    # category in: member, collaborator

    ## user id

    df = get_users()
    uids = df['uid'].to_numpy().astype('int')
    uids = uids[(uids>=2000)*(uids<3000)]

    user_id = None

    for ii in range(2000, 3000):
        if ii not in uids:
            user_id = str(ii)
            break

    if user_id is None:
        raise NoUIDsAvailable()

    ## passwd

    password = generate_random_password(12)

    ## adding user

    subprocess.run(['useradd', '-u', user_id, '-p', password, username])

    ## fixing user

    fix_user(username, fullname=fullname, phone=phone, mail=mail, category=category)


