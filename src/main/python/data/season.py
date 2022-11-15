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
        self.__xp: Data = __SeasonDataBuilder(3,44) 
        self.__scrip: Data = __SeasonDataBuilder(3,88)
        
    # TODO: doesn't disable corresponding widget
    def read(self, save_bytes: bytes) -> dict[str, int] | None:
        value_len = 4
        xp_pos = self.__xp.get_position(save_bytes)
        scrip_pos = self.__scrip.get_position(save_bytes)
        
        if xp_pos == -1 and scrip_pos == -1:
            return None
        
        xp:int = int(struct.unpack("i", save_bytes[xp_pos : xp_pos + value_len])[0])
        scrip:int = int(struct.unpack("i", save_bytes[scrip_pos : scrip_pos + value_len])[0])

        return {"xp": xp, "scrip": scrip}

def __SeasonDataBuilder(season_num:int,offset:int) -> Data:
    return Data(bytes.fromhex(SEASON_GUIDS[season_num]),offset)