from ._level import Level
from ._user import User
from ._vars import base

class InvalidData(Exception):
    pass

def _payload(url, data):
    if url.startswith(base+"level"):
        return Level._parse(data)
    elif url.startswith(base+"profile"):
        return User._parse(data)
    raise InvalidData(f'Unknown data from {url}: {data}')
