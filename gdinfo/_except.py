class LoginError(Exception):
    pass

class NotLoggedIn(LoginError):
    pass

class Error(Exception):
    pass
