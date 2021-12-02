
def exists(groupname):

    from ixtlilton_tools.admin import get_groups

    groups_df = get_groups()

    return groupname in groups_df.index

