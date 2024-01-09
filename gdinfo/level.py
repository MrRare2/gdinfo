from . import _payload
from ._vars import base
import json
import requests

class LevelNotExist(Exception):
    pass

_url = base+"level/"

def get_level_info(levelID):
    final = _url+str(levelID)
    req = requests.get(final)
    if req.text.startswith("-1"): raise LevelNotExist(f"Level {levelID} does not exist.")
    res = _payload._payload(final, req.json())
    return res

