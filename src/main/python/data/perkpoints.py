# handles stuff related to the players perk points

import struct

from main.python.data.data import Data, ReadFromBytes

class PerkPoints(ReadFromBytes):
    def __init__(self) -> None:
        self.data = Data(b"PerkPoints",36)
        
    def read(self, save_bytes: bytes) -> int:
        pos = self.data.get_position(save_bytes)
        return int(struct.unpack("i", save_bytes[pos : pos + 4])[0]) if pos else 0