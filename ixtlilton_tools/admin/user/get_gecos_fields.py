
def get_gecos_fields(username):

    from ixtlilton_tools.admin import get_users

    users_df = get_users()

    gecos = users_df.loc[username]['gecos']
    gecos_fields = gecos.split(',')

    if len(gecos_fields)==4:

        aux_dict = {'fullname': gecos_fields[0],
                    'phone': gecos_fields[3],
                    'mail': gecos_fields[1],
                }

    elif len(gecos_fieds)==1:

        aux_dict = {'fullname': None,
                }

    else:

        raise ValueError('Unknown gecos entry')

    return aux_dict

