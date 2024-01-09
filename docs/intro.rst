Introduction
============

Hi, welcome to my second project, ``gdinfo``, which you can use to do stuffs in Geometry Dash but in Python!

Basics
======

Here are the function/classes in ``gdinfo`` that you should know!!

Level
=====

First things to know is the ``Level()`` instance, you may see this if you execute the :ref:`find_level <find_level>` function, here are the info for each attribute/method:

Attributes
----------

- ``acc_id`` (int) - The account ID of the author
- ``author`` (:ref:`User`) - Info about the author of the level
- ``coins_verified`` (bool) - If the level coins is verified (silver)
- ``coins`` (int) - How many coins are in the level
- ``copied_id`` (str) - The copied levelID of the level
- ``custom_song`` (int) - The custom song ID of the level (0 if a official song is applied)
- ``desc`` (str) - The description of the level
- ``diamonds`` (int) - How many diamonds are in the level (reward)
- ``difficulty`` (:ref:`LevelDifficulty`) - The level difficulty of the level
- ``disliked`` (bool) - Whether the level is disliked or not
- ``downloads`` (int) - How many players downloaded the level
- ``epic``/``mythic``/``legendary`` (bool) - Whether the level is rated epic/mythic/legendary
- ``featured`` (bool) - If the level is featured
- ``game_version`` (str) - The game version of the level, the version of the game when the level is uploaded/updated
- ``id`` (int) - The ID of the level
- ``ldm`` (bool) - If the level has Low Detail mode checkbox
- ``length`` (:ref:`LevelLength`) - The length of the level (Tiny, Short, Medium, Long, XL, or Platformer)
- ``likes`` (int) - How many likes are in the level
- ``name`` (str) - The name of the level
- ``objects`` (int) - How many objects are in the level, caps at 65536(or 65535), i have no idea why,
- ``official_song`` (int) - The official song ID for the level (0 if custom song is applied)
- ``orbs`` (int) - How many orbs are on the level (reward)
- ``platformer`` (bool) - True if the level is a platformer mode
- ``player_id`` (int) - The player ID of the author, no idea what does this value mean
- ``song_author``/``song_id``/``song_link``/``song_size``/``song_title`` (str/int/str/str/str) - Info about the song of the level
- ``two_player`` (bool) - True if the level is a two player
- ``version`` (int) - The version of the level

Methods
-------

- ``comment`` (comment: str) [str] - Comment to the level, need to login first via :ref:`login <login>`, returns a comment ID
- ``delete_comment`` (commentID: str/int) [True]- Deletes your comment, returns True if success
- ``get_comments`` (page=0: int) [generator -> :ref:`LevelComment <LevelComment>`/None]- Get the comments of the level, sorting from recent to old
- ``vote`` (like=1: int) [True] - Like the level, 0 for dislike, 1 for like, need to login, always returns True even if like/disliked or not (its Robtop's fault)

User
====

Self-explanatory, just the info for the user, yeah:)

Attributes
----------

- ``acc_id`` (str/int) - Account ID of the user
- ``ball``/``icon``/``jetpack``/``robot``/``ship``/``spider``/``swing``/``ufo``/``wave`` (int) - ID of the icons of the user
- ``coins`` (int)- Secret Coins of the user
- ``col1``/``col2``/``colGlow`` (int) - Color of the user (in Color ID)
- ``col1RGB``/``col2RGB``/``colGlowRGB`` (dict) - Color of the user (in RGB)
- ``comment_history`` (str) - ``off`` means the comment history is disabled, ``all`` means it shows all[?]
- ``creator_points`` (int) - Creator points of the user
- ``death_effect`` (int) - ID of the death effect of the user
- ``demons`` (int) - How many demons does the user has beaten
- ``diamonds`` (int) - How many diamonds does the user have?
- ``friend_requests`` (bool) - If the user allow friend requests[?]
- ``glow`` (bool) - If the user enables glow in their icon set
- ``messages`` (str) - [?]
- ``moderator`` (:ref:`Moderator <Moderator>`) - Moderator status of the user
- ``moons`` (int) - Moons of the user
- ``player_id`` (int/str) - Player ID of the user)
- ``rank`` (int) - Rank of the user in the leaderboard (sometimes inaccurate)
- ``twch_url`` (str/None) - Twitch URL of the user
- ``twtr_url`` (str/None) - Twitter(X) URL of the user
- ``user_coins`` (int) - User coins of the user
- ``username`` (str) - The username of the user, shown in-game

Methods
-------

- ``get_comments`` [generator -> :ref:`AccountComnent <AccountComment>`/None]- Get the comments of the user (Account comments)
- ``get_levels`` (page=0: int, id_only=False: bool) [generator -> Level/None] - Get the levels of the user (uploaded levels)

Account
=======

Represents your account
Returned by :ref:`login <login>`

Attributes
----------

- ``acc_id`` (str/int) - Account ID of your account
- ``info`` (:ref:`User`) - Info about your account
- ``player_id`` (str/int) - Your account's player ID
- ``username`` (str/int) - Your username

Methods
-------

- ``delete_comment`` (comnentID) [True] - Deletes your comment (Account Comment)
- ``post_comment`` (text) [str] - Post a comnent (Account Comment)

_abc
====

This is one of the components in ``gdinfo`` where some things are stored

LevelDifficulty
---------------

- UNRATED = "Unrated" (i.e. N/A)
- AUTO = "Auto"
- EASY = "Easy"
- NORMAL = "Normal"
- HARD = "Hard"
- HARDER = "Harder"
- INSANE = "Insane"
- EASY_DEMON = "Easy Demon"
- MEDIUM_DEMON = "Medium Demon"
- HARD_DEMON = "Hard Demon"
- INSANE_DEMON = "Insane Demon"
- EXTREME_DEMON = "Extreme Demon"

Moderator
---------

- NONE = 0 - means not a moderator
- NORMAL = 1 - just a normal moderator
- ELDER = 2 - more powerful than normal mod

LevelComment
============

Represents a level comment

Attributes
----------

- ``acc_id`` (str/int) - Account ID of the user
- ``age`` (str) - Approximate upload date of the comment
- ``col1``/``col2``/``colGlow`` (int/None) - Color info for the commenter
- ``col1GRB``/``col2RGB`` (dict) - Color info but RGB
- ``glow`` (bool) - If the icon has glow
- ``icon`` (int) - Icon ID shown before the username
- ``level_id`` (str/int) - Level ID of where the comment was uploaded
- ``likes`` (int) - How many likes the comment get
- ``message_id`` (int) - Message ID of the comment, used to delete the comment (if the comment is made by yours)
- ``moderator`` (:ref:`Moderator <Moderator>`) - Moderator status of the commenter
- ``player_id`` (int) - Player ID of the commenter
- ``text`` (str) - The actual comment text
- ``user`` (:ref:`User <User>`) - User info of the commenter

Methods
-------

- ``vote`` (like=1: int) [True] - Like/dislike the level, need to log in, always returns True even the comment is actually liked/disliked or not (no idea why)

AccountComment
==============

Represent an account comment, shown inside the user profile in-game

Attributes
----------

- ``age`` (str) - Approximate upload date of the comment
- ``likes`` (int) - How many likes the comment get
- ``message_id`` (str/int) - Message IF of the comment, used to delete the comnent (if the comment is made by you)
- ``text`` (str) - The comment text
- ``user`` (:ref:`User <User>`) - User info about the commenter

Methods
-------

- ``votw`` (like=1: int) [True] - Like/dislike the level, need to log in, always returns True even the comment is actually liked/disliked or not (no idea why)

Main
====

Here is now the functions in ``gdinfo``

find_level
----------

Finds the level

Arguments:

- ``LevelID`` (str/int) - The level ID you want to get info

Returns:

A :ref:`Level <Level>` object

Raises:

:ref:`LevelNotExist <LevelNotExist>` if the level does not exist

find_user
---------

Finds the info for the user

Arguments:

- ``username`` (str/int) - Allows username and accountID

Returns:

A :ref:`User <User>` object

Raises:

:ref:`UserNotExist <UserNotExist>` if the user dosent exist

login
-----

Login so you can comment and vote? maybe i'll add more soon:)

Arguments:

- ``username`` - Your GD username
- ``password`` - Your GD password

Returns:

A :ref:`Account <Account>` object

Raises:

:ref:`Error <Error>` if username or password is incorrect

note that im not collecting any of your passwords, this project is entirely **open-source**, so you can see the files used to make this program work.

recent_tab
----------

Basically the recent tab

Arguments:

- ``page`` (int): 0 - Page
- ``id_only`` (bool): False - set to True if you only want the IDs

Returns:

A generator object
``str/int`` if you set ``id_only`` to True
:ref:`Level <Level>` if you set ``id_only`` to False (default)

search_level
------------

Search for a level

Arguments:

- ``query`` (str) - The level you want to search
- ``page`` (int): 0 - page basically
- ``id_only`` (bool): False - set to True if you only want the IDs                
Returns:

A generator object
``str/int`` if you set ``id_only`` to True
:ref:`Level <Level>` if you set ``id_only`` to False (default)

Exceptions
==========

Some errors may happen while using ``gdinfo``, so i will explain what are those

LevelNotExist
-------------

Raised by :ref:`find_level <find_level>` if the level does not exist, maybe you gave the wrong level ID?

UserNotExist
------------

Similar to ``LevelNotExist``, raised by :ref:`find_user <find_user>` if the user dosent exist on the Geometry Dash server

Error
-----

Raised by some methods, its basically self-explanatory so yeh

Sources/Credits
===============

Yey, basically just credits

`GDBrowser <https://github.com/GDColon/GDBrowser/>`__ by `GDColon <https://github.com/GDColon/>`__

`Boomlings server <https://www.boomlings.com/>`__ by RobTop

`GDDocs <https://wyliemaster.github.io/gddocs/#>`__ by `WylieMaster <https://github.com/wyliemaster>`__

Read `FAQ <./faq.html>`__ for more.
