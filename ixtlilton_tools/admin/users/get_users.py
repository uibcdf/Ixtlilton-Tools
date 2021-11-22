import pandas as pd

def get_users():

    df = pd.DataFrame(columns=['name', 'uid', 'gid', 'gecos', 'home', 'login shell'])

    with open("/etc/passwd", 'r') as fff:
        for line in fff:
            name, x, uid, gid, gecos, home, shell = line.rstrip('\n').split(':')
            df = df.append({'name': name, 'uid': uid, 'gid': gid,  'gecos': gecos,
                'home': home,  'login shell': shell}, ignore_index=True)

    df.set_index('name')

    return df

