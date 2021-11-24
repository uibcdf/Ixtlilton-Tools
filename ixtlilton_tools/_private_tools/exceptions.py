class BadCallError(ValueError):
    def __init__(self, message=None):
        if message is None:
            message = 'Wrong way of invoking this method. Check the online documentation for more information: http://www.uibcdf.org/MolSysMT'
        super().__init__(message)

class NotImplementedError(NotImplementedError):
    def __init__(self, message=None):
        if message is None:
            message = 'It has not been implemeted yet. Write a new issue in https://github.com/uibcdf/MolSysMT/issues asking for it.'
        super().__init__(message)

class LibraryNotFound(ValueError):
    def __init__(self, library):
        message = 'The python library {} was not found.'.format(library)
        super().__init__(message)

class NoAdminRights(ValueError):
    def __init__(self, message=None):
        if message is None:
            message = 'This method needs administration rights.'
        super().__init__(message)

class DirectoryConflict(ValueError):
    def __init__(self, message=None):
        if message is None:
            message = 'There is a directory conflict'
        super().__init__(message)

class NoUIDsAvailable(ValueError):
    def __init__(self, message=None):
        if message is None:
            message = 'All user ids between 2000 and 2999 are already taken.'
        super().__init__(message)

class UserDoesNotExist(ValueError):
    def __init__(self, username=None, message=None):
        if message is None:
            if username is None:
                message = 'The user does not exists.'
            else:
                message = f'The user {username} does not exists.'
        super().__init__(message)


