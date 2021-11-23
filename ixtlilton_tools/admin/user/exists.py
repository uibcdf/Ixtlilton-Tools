
def exists(username):

    from ixtlilton_tools.admin import get_users

    users_df = get_users()

    return username in users_df.index

