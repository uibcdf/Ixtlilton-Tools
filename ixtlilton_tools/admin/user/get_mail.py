
def get_mail(username):

    from ixtlilton_tools.admin.user import get_gecos_fields

    gecos_fields = get_gecos_fields(username)

    return gecos_fields['mail']

