# handles stuff related to the players money

import struct

from main.python.data.data import Data, ReadFromBytes

class credits(ReadFromBytes):
    def __init__(self) -> None:
        self.data = Data(b"Credits",33)
        
    def read(self, save_bytes: bytes) -> int:
        pos = self.data.get_position(save_bytes)
        return int(struct.unpack("i", save_bytes[pos : pos + 4])[0])