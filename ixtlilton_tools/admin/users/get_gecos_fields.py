
def get_gecos_fields(username):

    from ixtlilton_tools.admin import get_users

    users_df = get_users()

    gecos = DataFrame.iloc[username]['gecos']
    gecos_fields = gecos.split(',')

    aux_dict = {'fullname': gecos_fields[0],
                'phone': gecos_fields[2],
                'mail': gecos_fields[4],
            }

    return aux_dict

