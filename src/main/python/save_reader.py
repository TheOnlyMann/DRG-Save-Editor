# handles reading the save files into bytes

from main.python.data.credits import Credits
from main.python.data.perkpoints import PerkPoints
from main.python.data.resources import Resources
from main.python.data.season import Season
from main.python.data.xp import XP


class Reader:
    def __init__(self) -> None:
        self.credits = Credits()
        self.perkpoints = PerkPoints()
        self.resources = Resources()
        self.season = Season()
        self.xp = XP
        # TODO: add weapon overclocks

    def read(self, file_name:str)->None:
        save_bytes:bytes
        # read file into bytes
        with open(file_name, "rb") as f:
            save_bytes = f.read()
        
        self.credits.read(save_bytes)
        self.perkpoints.read(save_bytes)
        self.resources.read(save_bytes)
        self.season.read(save_bytes)
        self.xp.read(save_bytes)