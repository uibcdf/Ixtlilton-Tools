import pandas as pd

def get_groups():

    df = pd.DataFrame(columns=['name', 'gid', 'members'])

    with open("/etc/group", 'r') as fff:
        for line in fff:
            name, x, gid, members = line.rstrip('\n').split(':')
            df = df.append({'name': name, 'gid': gid, 'members': members}, ignore_index=True)

    return df

