import attr
import json
from ._vars import base, base_bl, headers
from ._comment_get import AccountComment
from .level import get_level_info
from ._except import Error
from enum import Enum
from . import _abc
import requests

def _raw_to_json(data_str, splitter="~"):
    data_pairs = data_str.split(splitter)
    json_data = {}

    for i in range(0, len(data_pairs), 2):
        key = data_pairs[i]
        value = data_pairs[i + 1] if i + 1 < len(data_pairs) else None

        # Handling missing values
        if value is None or value == '':
            value = ""

        json_data[key] = value

    return json_data

@attr.s
class User:
    username = attr.ib(type=str)
    player_id = attr.ib(type=str)
    acc_id = attr.ib(type=str)
    rank = attr.ib(type=int)
    stars = attr.ib(type=int)
    coins = attr.ib(type=int)
    diamonds = attr.ib(type=int)
    moons = attr.ib(type=int)
    user_coins = attr.ib(type=int)
    demons = attr.ib(type=int)
    creator_points = attr.ib(type=int)
    icon = attr.ib(type=int)
    ship = attr.ib(type=int)
    ball = attr.ib(type=int)
    ufo = attr.ib(type=int)
    wave = attr.ib(type=int)
    robot = attr.ib(type=int)
    spider = attr.ib(type=int)
    swing = attr.ib(type=int)
    jetpack = attr.ib(type=int)
    friend_requests = attr.ib(type=bool)
    messages = attr.ib(type=bool)
    comment_history = attr.ib(type=str)
    moderator = attr.ib(type=str)
    yt_url = attr.ib()
    twch_url = attr.ib()
    twtr_url = attr.ib()
    col1 = attr.ib(type=int)
    col2 = attr.ib(type=int)
    colGlow = attr.ib(type=int)
    death_effect = attr.ib(type=int)
    glow = attr.ib(type=bool)
    col1RGB = attr.ib(type=dict)
    col2RGB = attr.ib(type=dict)
    colGlowRGB = attr.ib(type=dict)

    def get_comments(self, page=0):
        data = {
                "secret": "Wmfd2893gb7",
                "page": page,
                "accountID": self.acc_id
            }

        url = base_bl+"getGJAccountComments20.php"
        req = requests.post(url, data=data, headers=headers).text
        hash_index = req.find("#")
        if req[:hash_index] == "":
            return None
        for comment_obj in req[:hash_index].split("|"):
            j = _raw_to_json(comment_obj)
            j['userName'] = self.username
            yield AccountComment._parse(j)

    def get_levels(self, page=0, id_only=False):
        data = {
                "secret": "Wmfd2893gb7",
                "type": 5,
                "str": self.player_id,
                "page": page,
                "local": 0
               }
        url = base_bl + "getGJLevels21.php"
        req = requests.post(url, data=data, headers=headers).text

        if req == "-1":
            raise Error("Error when getting the user's level")

        req = req[:req.find("#")].split("|")

        for i in req:
            info = _raw_to_json(i, splitter=":")
            lvl_id = info['1']
            if id_only:
                yield lvl_id
            else:
                yield get_level_info(lvl_id)

    @classmethod
    def _parse(cls, data):

        return cls(
            username=data['username'],
            player_id=data['playerID'],
            acc_id=data['accountID'],
            rank=int(data['rank']),
            stars=int(data['stars']),
            diamonds=int(data['diamonds']),
            coins=int(data['coins']),
            user_coins=int(data['userCoins']),
            demons=int(data['demons']),
            moons=int(data['moons']),
            icon=int(data['icon']),
            ball=int(data['ball']),
            ship=int(data['ship']),
            wave=int(data['wave']),
            ufo=int(data['ufo']),
            robot=int(data['robot']),
            spider=int(data['swing']),
            swing=int(data['swing']),
            jetpack=int(data['jetpack']),
            col1=int(data['col1']),
            col2=int(data['col2']),
            colGlow=int(data['colG']),
            death_effect=int(data['deathEffect']),
            glow=data['glow'],
            col1RGB=data['col1RGB'],
            col2RGB=data['col2RGB'],
            colGlowRGB=data['colGRGB'],

            friend_requests=data['friendRequests'],
            messages=data['messages'],
            comment_history=data['commentHistory'],
            moderator=next(mem for mem in _abc.Moderator if mem.value == data['moderator']),
            yt_url=data['youtube'],
            twch_url=data['twitch'],
            twtr_url=data['twitter'],
            creator_points=data['cp']
        )
