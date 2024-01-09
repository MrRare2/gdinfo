from . import _payload
from ._vars import base
import json
import requests

class UserNotExist(Exception):
    pass

_url = base+"profile/"

def get_user_info(user):
    final = _url+str(user)
    req = requests.get(final)
    if req.text.startswith("-1"): raise UserNotExist(f"User {user} does not exist.")
    res = _payload._payload(final, req.json())
    return res

