

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, NamedTuple, Protocol

GUID_RE = re.compile(r".*\(([0-9A-F]*)\)")

class ReadFromBytes(Protocol):
    def read(self, save_bytes:bytes) -> Any:
        ...

@dataclass(frozen=True,init=True)
class Data(ABC):
    marker:bytes
    offset:int
    
    @abstractmethod 
    def get_position(self, save_bytes:bytes) -> int:
        """
        Args:
            save_bytes (bytes): save data to look through

        Returns:
            int: position of this piece of data, if it's found in the save data, otherwise -1 if missing
        """
        marker_pos = save_bytes.find(self.marker)
        return -1 if marker_pos == -1 or marker_pos > len(save_bytes) else marker_pos + self.offset
    