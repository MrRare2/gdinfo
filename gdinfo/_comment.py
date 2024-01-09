import base64
import requests
from ._vars import base_bl, headers
from ._except import NotLoggedIn, Error
from ._xor import xor_cipher
from hashlib import sha1

def _encode(text):
    return base64.urlsafe_b64encode(text).decode()

def chk(values: [int, str] = [], key: str = "", salt: str = "") -> str:
    values.append(salt)

    string = ("").join(map(str, values))

    hashed = sha1(string.encode()).hexdigest()
    xored = xor_cipher(hashed, key)
    final = base64.urlsafe_b64encode(xored.encode()).decode()

    return final

def _post_acc(comment, _accID, _gjp):
    if _gjp is None or _accID is None:
        raise NotLoggedIn("You must be logged in to comment")

    data = {
            "accountID": _accID,
            "gjp": _gjp,
            "comment": _encode(comment.encode()),
            "secret": "Wmfd2893gb7"
           }

    url = base_bl+"uploadGJAccComment20.php"

    req = requests.post(url, data=data, headers=headers)
    if req.text == "-1":
        raise Error("There was an error posting your comment")
    elif req.text == "-10":
        raise Error("Your account has been permanently banned from commenting")
    elif req.text.startswitg("temp"):
        _, time, reason = req.text.split("_")
        raise Error(f"Your account has been temporarily banned from commenting for {time} because of: {reason}")
    if req.status_code == 500:
        raise Error(r"Server returned a {req.status_code} response, the comment might not be uploaded properly")
    return req.text

def _del_acc(commentID, _accID, _gjp):
    if _gjp is None or _accID is None:                      raise NotLoggedIn("You must be logged in to delete a comment")

    data = {
            "accountID": _accID,
            "gjp": _gjp,
            "commentID": commentID,
            "secret": "Wmfd2893gb7"
           }

    url = base_bl+"deleteGJAccComment20.php"

    req = requests.post(url, data=data, headers=headers).text

    if req == "-1":
        raise Error("There was an error while deleting your comment")

    return True

def _post_lvl(comment, lvlID, percent, _username, _accID,_gjp):
    if _gjp is None or _accID is None:
        raise NotLoggedIn("You must be logged in to comment")
    comment = _encode(comment.encode())

    data = {
            "accountID": _accID,
            "gjp": _gjp,
            "comment": comment,
            "userName": _username,
            "levelID": lvlID,
            "secret": "Wmfd2893gb7",
            "percentage": percent,
            "chk": chk(values=[_username, comment, lvlID, percent], key="29481", salt="0xPT6iUrtws0J")
           }

    url = base_bl+"uploadGJComment21.php"

    req = requests.post(url, data=data, headers=headers).text

    if req == "-1":
        raise Error("There was an error posting your comment")
    elif req == "-10":
        raise Error("Your account has been permanently banned from commenting") 
    elif req.startswith("temp"):
        _, time, reason = req.text.split("_")
        raise Error(f"Your account has been temporarily banned from commenting for {time} because of: {reason}")

    return req

def _del_lvl(commentID, lvlID, _accID, _gjp):
    if _accID is None or _gjp is None:
        raise NotLoggedIn("You must be logged in to comment")

    data = {
            "accountID": _accID,
            "gjp": _gjp,
            "commentID": commentID,
            "levelID": lvlID,
            "secret": "Wmfd2893gb7"
           }

    url = base_bl+"deleteGJComment20.php"

    req = requests.post(url, data=data, headers=headers).text
    if req == "-1":
        raise Error("There was an error deleting your comment")
    return True
