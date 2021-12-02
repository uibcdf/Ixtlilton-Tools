from ixtlilton_tools._private_tools.exceptions import UserDoesNotExist, GroupDoesNotExist, NoAdminRights
import subprocess

def add_user(groupname, username):

    from ixtlilton_tools.admin import running_with_admin_rights
    from ixtlilton_tools.admin.group import exists as group_exists
    from ixtlilton_tools.admin.user import exists as user_exists

    if not running_with_admin_rights():
        raise NoAdminRights()

    if not group_exists(groupname):
        raise GroupDoesNotExist(groupname=groupname)

    if not user_exists(username):
        raise UserDoesNotExist(username=username)

    subprocess.run(['usermod', '-a', '-G', groupname, username])

    pass
