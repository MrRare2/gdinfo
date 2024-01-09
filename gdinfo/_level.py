import attr
import json
import requests
from ._vars import base, base_bl, headers
from ._comment_get import LevelComment
from ._comment import _post_lvl, _del_lvl
from . import _abc
from . import user
from . import _except
from . import _login

@attr.s
class Level:
    name = attr.ib(type=str)
    id = attr.ib(type=int)
    desc = attr.ib(type=str)
    author = attr.ib()
    player_id = attr.ib(type=str)
    acc_id = attr.ib(type=str)
    difficulty = attr.ib(type=str)
    downloads = attr.ib(type=int)
    likes = attr.ib(type=int)
    disliked = attr.ib(type=bool)
    length = attr.ib(type=str)
    platformer = attr.ib(type=bool)
    stars = attr.ib(type=int)
    orbs = attr.ib(type=int)
    diamonds = attr.ib(type=int)
    featured = attr.ib(type=bool)
    epic = attr.ib(type=bool)
    legendary = attr.ib(type=bool)
    mythic = attr.ib(type=bool)
    game_version = attr.ib(type=str)
    version = attr.ib(type=int)
    copied_id = attr.ib(type=str)
    #copyable = attr.ib(type=int) # TODO: what is cp?
    two_player = attr.ib(type=bool)
    official_song = attr.ib(type=int)
    custom_song = attr.ib(type=int)
    coins = attr.ib(type=int)
    coin_verified = attr.ib(type=bool)
    stars_requested = attr.ib()
    ldm = attr.ib(type=bool)
    objects = attr.ib(type=int)

    song_title = attr.ib(type=str)
    song_author = attr.ib(type=str)
    song_size = attr.ib(type=str)
    song_id = attr.ib(type=str)
    song_link = attr.ib(type=str)

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
                "itemID": self.id,
                "like": like,
                "type": 1 # this is a like level type
                }
        url = base_bl+"likeGJItem211.php"
        req = requests.post(url, data=data, headers=headers).text
        
        return True

    def get_comments(self,page=0):
        data = {
                "page": page
                }

        url = base+"comments/"+str(self.id)

        req = requests.get(url, data=data, headers=headers).json()

        for comment in req:
            yield LevelComment._parse(comment)

    def comment(self, comment): # TODO: make percentage work, as of Jan 5 2023, i cant get it to work
        return _post_lvl(comment, self.id, 0, _login._username, _login._accID, _login._gjp)

    def delete_comment(self, commentID):
        return _del_lvl(commentID, self.id, _login._accID, _login._gjp)


    @classmethod
    def _parse(cls, data):
        return cls(
            name=data['name'],
            id=int(data['id']),
            desc=data['description'],
            author=user.get_user_info(data['author']),
            player_id=data['playerID'],
            acc_id=data['accountID'],
            difficulty=getattr(_abc.LevelDifficulty, data['difficulty'].replace(" ","_").upper()),
            downloads=data['downloads'],
            likes=int(data['likes']),
            disliked=data['disliked'],
            length=next(mem for mem in _abc.LevelLength if mem.value == data['length']),
            platformer=data['platformer'],
            stars=int(data['stars']),
            orbs=int(data['orbs']),
            diamonds=int(data['diamonds']),
            featured=data['featured'],
            epic=data['epic'],
            legendary=data['legendary'],
            mythic=data['mythic'],
            game_version=data['gameVersion'],
            version=int(data['version']),
            copied_id=data['copiedID'],
            two_player=data['twoPlayer'],
            official_song=int(data['officialSong']),
            custom_song=int(data['customSong']),
            coins=int(data['coins']),
            coin_verified=data['verifiedCoins'],
            stars_requested=next(mem for mem in _abc.StarsRequested if data['starsRequested'] in mem.value),
            ldm=data['ldm'],
            objects=int(data['objects']),
            song_title=data['songName'],
            song_author=data['songAuthor'],
            song_size=data['songSize'],
            song_id=data['songID'],
            song_link=data.get('songLink'),
            #copyable=data.get("cp")
        )

