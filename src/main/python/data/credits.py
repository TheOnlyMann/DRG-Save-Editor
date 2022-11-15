# handles stuff related to the players money

import struct

from main.python.data.data import DataSource, ReadFromBytes

class Credits(ReadFromBytes):
    __datasource: DataSource = DataSource(b"Credits",33)
    __data:int|None = None
    
    @staticmethod
    def read(save_bytes: bytes) -> None:
        pos = Credits.__datasource.get_position(save_bytes)
        Credits.__data = int(struct.unpack("i", save_bytes[pos : pos + 4])[0])
    
    @staticmethod
    def data() -> int|None:
        return Credits.__data