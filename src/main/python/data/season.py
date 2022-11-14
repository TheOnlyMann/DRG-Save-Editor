# handles stuff relating to the current season (i.e. season XP, scrip, etc.)

import struct
from typing import Type
from main.python.data.data import Data,ReadFromBytes


SEASON_GUIDS: dict[int, str] = {
    1: "A47D407EC0E4364892CE2E03DE7DF0B3",
    2: "B860B55F1D1BB54D8EE2E41FDA9F5838",
    3: "D8810F6C76D374419AE6A18EF5B3BA26",
}

XP_PER_SEASON_LEVEL: int = 5000

class Season(ReadFromBytes):
    data: Type[Data] = Data
    
    def __init__(
        self
    ) -> None:
        self.season_guid = SEASON_GUIDS[3]
        self.xp = Season.data(
            marker=bytes.fromhex(self.season_guid),
            offset=44,
        ) 
        self.scrip = Season.data(
            marker=self.xp.marker,
            offset=88,
        )
        

    def read(self, save_bytes: bytes):
        """implement the ReadFromBytes protocol, returns an empty dict if position couldn't be found

        Args:
            save_bytes (bytes): bytes content of save file

        Returns:
            _type_: _description_
        """
        xp_marker_pos: int = save_bytes.find(self.xp.marker)
        scrip_marker_pos: int = save_bytes.find(self.xp.marker)
        
        if xp_marker_pos == -1 and scrip_marker_pos == -1:
            return dict()
        
        xp_pos = xp_marker_pos + self.xp.offset
        scrip_pos = scrip_marker_pos + self.scrip.offset

        xp:int = struct.unpack("i", save_bytes[xp_pos : xp_pos + 4])[0]
        scrip:int = struct.unpack("i", save_bytes[scrip_pos : scrip_pos + 4])[0]

        return {"xp": xp, "scrip": scrip}
        