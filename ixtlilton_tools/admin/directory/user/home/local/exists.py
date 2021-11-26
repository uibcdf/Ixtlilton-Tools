import pathlib
from ixtlilton_tools._private_tools.exceptions import DirectoryConflict

def exists(username):

    path = pathlib.Path('/home/'+username+'/local')
    path_source = pathlib.Path('/home/'+username+'/.local')

    if path_source.exists() and not path.is_symlink():
        raise DirectoryConflict(f'The local directory of user {username} exists but is not a directory')

    return path.exists()

