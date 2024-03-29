import os

def running_with_admin_rights():

    from ixtlilton_tools.admin import running_as_root

    # checking if user is root
    if running_as_root():
        return True

    # checking if user belongs to wheel group
    return 10 in os.getgroups()

