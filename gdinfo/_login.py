from . import _vars
from . import _except
from . import user
from . import _xor
from ._comment import _post_acc, _del_acc
import requests
import attr
import random
import base64

def _generate_udid():
    return "S" + str(random.randint(10_000_000, 1_000_000_000))

def _gjp_encrypt(password: str) -> str:
    # put it through the xor cipher with the key "37526")
    encoded = _xor.xor_cipher(password, "37526")
    # encode the password to base64
    encoded_base64 = base64.b64encode(encoded.encode()).decode()
    encoded_base64 = encoded_base64.replace("+", "-")
    encoded_base64 = encoded_base64.replace("/", "_")
    return encoded_base64

@attr.s
class Account:
    acc_id = attr.ib()
    player_id = attr.ib()
    username = attr.ib()
    info = attr.ib()

    def post_comment(self, comment):
        return _post_acc(comment, _accID, _gjp)

    def delete_comment(self, commentID):
        return _del_acc(commentID, _accID, _gjp)

    @classmethod
    def _parse(cls, url, data):
        if url.startswith(_vars.base_acc):
          return cls(
            acc_id = data["accID"],
            player_id = data["playerID"],
            username = data["userName"],
            info = user.get_user_info(data['accID'])
          )

_username = None
_password = None
_gjp = None
_accID = None

def _login(username: str, password: str) -> Account:
    global _username, _password, _gjp, _accID
    data = {"userName": username, "password": password, "secret": "Wmfv3899gc9", "udid": _generate_udid}# i dont want to put the `secret` in _vars lol
    data_rec = {"accID":None, "playerID": None, "userName": username}
    url = _vars.base_acc+"loginGJAccount.php"
    req = requests.post(url, data=data, headers=_vars.headers).text
    if req == "-1":
        raise _except.LoginError("Login error, please check your username and password")
    else:
        acc_id, player_id = req.split(",")
        data_rec['accID'] = acc_id
        data_rec['playerID'] = player_id

    _username = username
    _password = base64.b64encode(password.encode())
    _gjp = _gjp_encrypt(password)
    _accID = data_rec.get("accID")

    return Account._parse(url, data_rec)
