from aenum import Enum as default_Enum

class Enum(default_Enum):
    def __repr__(self):
        return "{}.{}".format(type(self).__name__, self.name)

class LevelDifficulty(Enum):
    UNRATED = "Unrated"
    AUTO = "Auto"
    EASY = "Easy"
    NORMAL = "Normal"
    HARD = "Hard"
    HARDER = "Harder"
    INSANE = "Insane"
    EASY_DEMON = "Easy Demon"
    MEDIUM_DEMON = "Medium Demon"
    HARD_DEMON = "Hard Demon"
    INSANE_DEMON = "Insane Demon"
    EXTREME_DEMON = "Extreme Demon"

class LevelDifficultyInt(Enum):
    DEMONS = -2
    NA = -1
    AUTO = 0
    EASY = 1
    NORMAL = 2
    HARD = 3
    HARDER = 4
    INSANE = 5

class StarsRequested(Enum):
    NULL = (0,)
    AUTO = (1,)
    EASY = (2,)
    NORMAL = (3,)
    HARD = (4,5)
    HARDER = (6,7)
    INSANE = (8,9)
    DEMON = (10,)


class DemonDifficultyInt(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    INSANE = 4
    EXTREME = 5

class LevelLengthInt(Enum):
    TINY = 0
    SHORT = 1
    MEDIUM = 2
    LONG = 3
    XL = 4

class LevelLength(Enum):
    TINY = "Tiny"
    SHORT = "Short"
    MEDIUM = "Medium"
    LONG = "Long"
    XL = "XL"
    PLATFORMER = "Plat"

class Moderator(Enum):
    NONE = 0
    NORMAL = 1
    ELDER = 2

