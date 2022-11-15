# handles reading the save files into bytes

from main.python.data.credits import Credits
from main.python.data.perkpoints import PerkPoints
from main.python.data.resources import Resources
from main.python.data.season import Season
from main.python.data.xp import XP


class __Reader:
    def __init__(self) -> None:
        self.credits 
        self.perkpoints 
        self.resources
        self.season
        self.xp
        # TODO: add weapon overclocks

    def __read(self, file_name:str)->None:
        save_bytes:bytes
        # read file into bytes
        with open(file_name, "rb") as f:
            save_bytes = f.read()
        
        Credits.read(save_bytes)
        PerkPoints.read(save_bytes)
        Resources.read(save_bytes)
        Season.read(save_bytes)
        XP.read(save_bytes)
        
        self.credits = Credits.data()
        self.perkpoints = PerkPoints.data()
        self.resources = Resources.data()
        self.season = Season.data()
        self.xp = XP.data()
    
    def read(self, file_name:str)->None:
        self.filename = file_name
        self.__read(file_name)
        
    def restore_from_backup(self) -> None:
        self.__read(f"{self.filename}.old")
        
Reader_Singleton = __Reader()