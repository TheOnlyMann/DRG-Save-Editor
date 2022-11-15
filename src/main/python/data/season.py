# handles stuff relating to the current season (i.e. season XP, scrip, etc.)

import struct

from main.python.data.data import DataSource, ReadFromBytes

SEASON_GUIDS: dict[int, str] = {
    1: "A47D407EC0E4364892CE2E03DE7DF0B3",
    2: "B860B55F1D1BB54D8EE2E41FDA9F5838",
    3: "D8810F6C76D374419AE6A18EF5B3BA26",
}

XP_PER_SEASON_LEVEL: int = 5000

def __SeasonDataBuilder(season_num:int,offset:int) -> DataSource:
    return DataSource(bytes.fromhex(SEASON_GUIDS[season_num]),offset)

class Season(ReadFromBytes):
    __xp: DataSource = __SeasonDataBuilder(3,44) 
    __scrip: DataSource = __SeasonDataBuilder(3,88)
    __data:dict[str,int]|None = None
    
    # TODO: doesn't disable corresponding widget
    @staticmethod
    def read(save_bytes: bytes) -> None:
        value_len = 4
        xp_pos = Season.__xp.get_position(save_bytes)
        scrip_pos = Season.__scrip.get_position(save_bytes)
        
        if xp_pos == -1 and scrip_pos == -1:
            return None
        
        xp:int = int(struct.unpack("i", save_bytes[xp_pos : xp_pos + value_len])[0])
        scrip:int = int(struct.unpack("i", save_bytes[scrip_pos : scrip_pos + value_len])[0])

        Season.__data = {"xp": xp, "scrip": scrip}
    
    @staticmethod
    def data() -> dict[str, int] | None:
        return Season.__data