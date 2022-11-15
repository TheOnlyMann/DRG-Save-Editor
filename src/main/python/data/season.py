# handles stuff relating to the current season (i.e. season XP, scrip, etc.)

import struct

from main.python.data.data import Data, ReadFromBytes

SEASON_GUIDS: dict[int, str] = {
    1: "A47D407EC0E4364892CE2E03DE7DF0B3",
    2: "B860B55F1D1BB54D8EE2E41FDA9F5838",
    3: "D8810F6C76D374419AE6A18EF5B3BA26",
}

XP_PER_SEASON_LEVEL: int = 5000

class Season(ReadFromBytes):
    def __init__(self) -> None:
        self.xp:Data = XP() 
        self.scrip: Data = Scrip()
        
    # TODO: doesn't disable corresponding widget
    def read(self, save_bytes: bytes):
        """implement the ReadFromBytes protocol, returns an empty dict if position couldn't be found

        Args:
            save_bytes (bytes): bytes content of save file

        Returns:
            _type_: _description_
        """
        xp_pos = self.xp.get_position(save_bytes)
        scrip_pos = self.scrip.get_position(save_bytes)
        
        if xp_pos == -1 and scrip_pos == -1:
            return dict()
        
        xp:int = struct.unpack("i", save_bytes[xp_pos : xp_pos + 4])[0]
        scrip:int = struct.unpack("i", save_bytes[scrip_pos : scrip_pos + 4])[0]

        return {"xp": xp, "scrip": scrip}

class XP(Data):
    marker=bytes.fromhex(SEASON_GUIDS[3]),
    offset=44
    
    def get_position(self, save_bytes: bytes) -> int:
        return super().get_position(save_bytes)
    
class Scrip(Data):
    marker: bytes=bytes.fromhex(SEASON_GUIDS[3])
    offset=88
    
    def get_position(self, save_bytes: bytes) -> int:
        return super().get_position(save_bytes)