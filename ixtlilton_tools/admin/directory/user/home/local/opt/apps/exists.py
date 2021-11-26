import pathlib
from ixtlilton_tools._private_tools.exceptions import DirectoryConflict

def exists(username):

    path = pathlib.Path('/home/'+username+'/local/opt/apps')

    if path.exists() and not path.is_dir():
        raise DirectoryConflict(f'The apps directory of user {username} exists but is not a directory')

    return path.exists()

