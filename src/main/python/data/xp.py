# handles stuff related to the players xp and promotions

import struct

from main.python.data.data import Data, ReadFromBytes

class XP(ReadFromBytes):
    def __init__(self) -> None:
        self.__engineer   = __XpAndPromoInfo(b"\x85\xEF\x62\x6C\x65\xF1\x02\x4A\x8D\xFE\xB5\xD0\xF3\x90\x9D\x2E\x03\x00\x00\x00\x58\x50")
        self.__scout      = __XpAndPromoInfo(b"\x30\xD8\xEA\x17\xD8\xFB\xBA\x4C\x95\x30\x6D\xE9\x65\x5C\x2F\x8C\x03\x00\x00\x00\x58\x50")
        self.__driller    = __XpAndPromoInfo(b"\x9E\xDD\x56\xF1\xEE\xBC\xC5\x48\x8D\x5B\x5E\x5B\x80\xB6\x2D\xB4\x03\x00\x00\x00\x58\x50")
        self.__gunner     = __XpAndPromoInfo(b"\xAE\x56\xE1\x80\xFE\xC0\xC4\x4D\x96\xFA\x29\xC2\x83\x66\xB9\x7B\x03\x00\x00\x00\x58\x50")
        
    def read(self, save_bytes: bytes):
        self.__engineer.update(save_bytes)
        self.__scout.update(save_bytes)
        self.__driller.update(save_bytes)
        self.__gunner.update(save_bytes)
        
        return {
            "engineer": {"xp": self.__engineer.xp_value,  "promo": self.__engineer.promo_value},
            "scout":    {"xp": self.__scout.xp_value,     "promo": self.__scout.promo_value},
            "driller":  {"xp": self.__driller.xp_value,   "promo": self.__driller.promo_value},
            "gunner":   {"xp": self.__gunner.xp_value,    "promo": self.__gunner.promo_value},
        }
        
        
class __XpAndPromoInfo:
    def __init__(self, marker) -> None:
        self.xp:Data = __XpDataBuilder(marker)
        self.promo:Data = __PromoDataBuilder(self.xp)

    def __update_pos(self,save_bytes)->None:
        self.xp_pos = self.xp.get_position(save_bytes)
        self.promo_pos = self.promo.get_position(save_bytes)
        
    def __update_value(self,save_bytes)->None:
        value_len = 4
        self.xp_value:int = int(struct.unpack("i", save_bytes[self.xp_pos : self.xp_pos + value_len])[0])
        self.promo_value:int = int(struct.unpack(
            "i",
            save_bytes[
                self.promo_pos: self.promo_pos + 4
            ],
        )[0])
        
    def update(self,save_bytes)->None:
        self.__update_pos(save_bytes)
        self.__update_value(save_bytes)
        
def __XpDataBuilder(marker) -> Data:
    return Data(marker,48)

def __PromoDataBuilder(XpData:Data) -> Data:
    return Data(XpData.marker, XpData.offset + 108)

