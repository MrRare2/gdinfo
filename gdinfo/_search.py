from .level import get_level_info
from ._user import _raw_to_json
from ._vars import base_bl, headers
from ._except import Error
from . import _abc
import requests

# this is the hardest to add lol:p
# FIXME!!!: make this better:)
def _post_old(query, page=0, diff=None, demonFilter=None, coins=0, star=1, noStar=0, featured=1, original=0, twoPlayer=0, epic=0):
    data = {
            "secret": "Wmfd2893gb7",
            "type": 0,
            "page": page,
            "diff": diff.value if isinstance(diff, _abc.LevelDifficultyInt) else diff or _abc.LevelDifficultyInt.NA.value,
            "demonFilter": demonFilter.value if isinstance(demonFilter, _abc.DemonDifficultyInt) else demonFilter or 0,
            "coins": 1 if coins == 1 else 0,
            "star": 1 if star == 1 else 0,
            "noStar": 1 if noStar == 1 else 0,
            "featured": 1 if featured == 1 else 0,
            "epic": 1 if epic == 1 else 0,
            "twoPlayer": 1 if twoPlayer == 1 else 0,
            "original": 1 if original == 1 else 0,
            "str": query
           }

    url = base_bl+"getGJLevels21.php"

    req = requests.post(url, data=data, headers=headers).text

    if req == "-1":
        raise Error("Error when searching, Please recheck your parameters")

    return

def _post(query, page=0, diff=None, demonFilter=None, coins=0, star=0, noStar=0, featured=1, original=0, twoPlayer=0, epic=0, id_only=False):
    data = {
        "secret": "Wmfd2893gb7",
        "type": 0,
        "page": page,
        "diff": diff.value if isinstance(diff, _abc.LevelDifficultyInt) else diff or _abc.LevelDifficultyInt.NA.value,
        "demonFilter": demonFilter.value if isinstance(demonFilter, _abc.DemonDifficultyInt) else demonFilter or 0,
        "coins": coins,
        "star": star,
        "noStar": noStar,
        "featured": featured,
        "epic": epic,
        "twoPlayer": twoPlayer,
        "original": original,
        "str": query
    }

    default_keys = ["type", "str", "secret", "page"]
    data ={key: value for key, value in data.items() if key in default_keys or value == 1}

    url = base_bl + "getGJLevels21.php"

    req = requests.post(url, data=data, headers=headers).text

    if req == "-1":
        raise Error("Error when searching, Please recheck your parameters")

    req = req[:req.find("#")].split("|")

    if id_only:
        for i in req:
            yield _raw_to_json(i, splitter=":")['1']
    else:
        for i in req:
            yield get_level_info(_raw_to_json(i, splitter=":")['1'])

def _post_recent_tab(page=0, id_only=False):
    # THE RECENTTT TTAAABBB!! - evw
    data = {
            "secret": "Wmfd2893gb7",
            "type": 4,
            "page": page
           }

    url = base_bl + "getGJLevels21.php"

    req = requests.post(url, data=data, headers=headers).text
    if req == "-1":
        raise Error("There's an error getting the recent tab levels :(")
    
    req = req[:req.find("#")].split("|")
    if id_only:
      for i in req:
        yield _raw_to_json(i, splitter=":")['1']
    else:
      for i in req:
        yield get_level_info(_raw_to_json(i, splitter=":")['1'])
