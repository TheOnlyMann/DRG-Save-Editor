# handles stuff related to the players perk points

import struct

from main.python.data.data import DataSource, ReadFromBytes

class PerkPoints(ReadFromBytes):
    __datasource = DataSource(b"PerkPoints",36)
    __data:int|None = None
        
    @staticmethod
    def read(save_bytes: bytes) -> int:
        pos = PerkPoints.__datasource.get_position(save_bytes)
        return int(struct.unpack("i", save_bytes[pos : pos + 4])[0]) if pos else 0
    
    @staticmethod
    def data() -> None | int:
        return PerkPoints.__data