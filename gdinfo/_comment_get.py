import attr
import json
from ._vars import base, base_bl, headers
from . import _login
from . import _except
from . import user
from enum import Enum
from base64 import b64decode
import requests

@attr.s
class LevelComment:
    text = attr.ib(type=str)
    user = attr.ib()
    player_id = attr.ib(type=str)
    acc_id = attr.ib(type=str)
    level_id = attr.ib(type=str)
    likes = attr.ib(type=int)
    icon = attr.ib(type=int)
    moderator = attr.ib(type=str)
    col1 = attr.ib(type=int)
    col2 = attr.ib(type=int)
    colGlow = attr.ib()
    glow = attr.ib(type=bool)
    col1RGB = attr.ib(type=dict)
    col2RGB = attr.ib(type=dict)
    age = attr.ib(type=str)
    message_id = attr.ib()

    def vote(self, like):
        if _login._username is None or _login._gjp is None:
            raise _except.NotLoggedIn("You must be logged in to like/dislike this comment")
        if like not in (0, 1):
            raise _except.InvalidLike("like value must be 0 and 1 only")
    
        data = {
            "secret": "Wmfd2893gb7",
            "accountID": _login._accID,
            "gjp": _login._gjp,
            "userName": _login._username,
            "itemID": self.message_id,
            "like": like,
            "type": 2  # this is a like level comment type
        }
    
        url = base_bl + "likeGJItem211.php"
        req = requests.post(url, data=data, headers=headers).text
    
        return True

    @classmethod
    def _parse(cls, data):

        return cls(
            text=data['content'],
            user=user.get_user_info(data['username']),
            player_id=data['playerID'],
            acc_id=data['accountID'],
            level_id=data['levelID'],
            icon=int(data['icon']['icon']),
            col1=int(data['icon']['col1']),
            col2=int(data['icon']['col2']),
            colGlow=data['icon']['colG'],
            glow=data['icon']['glow'],
            col1RGB=data['col1RGB'],
            col2RGB=data['col2RGB'],
            moderator=data['moderator'],
            age=data['date'],
            message_id=data['ID'],
            likes=data['likes']
        )

@attr.s
class AccountComment:
    text = attr.ib(type=str)
    user = attr.ib()
    likes = attr.ib(type=int)
    age = attr.ib(type=str)
    message_id = attr.ib()

    def vote(self, like):
        if _login._username is None or _login._gjp is None:
            raise _except.NotLoggedIn("You must be logged in to like/dislike this level")
        if like not in (0, 1):
            raise _except.InvalidLike("like value must be 0 and 1 only")

        data = {
            "secret": "Wmfd2893gb7",
            "accountID": _login._accID,
            "gjp": _login._gjp,
            "userName": _login._username,
            "itemID": self.message_id,
            "like": like,
            "type": 3  # this is a like level type
        }

        url = base_bl + "likeGJItem211.php"
        req = requests.post(url, data=data, headers=headers).text

        return True

    @classmethod
    def _parse(cls, data):
        return cls(
            text=b64decode(data['2']),
            user=user.get_user_info(data['userName']),
            likes=int(data['4']),
            age=data['9'],
            message_id=data['6']
        )
