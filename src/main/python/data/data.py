

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, NamedTuple, Optional, Protocol

GUID_RE = re.compile(r".*\(([0-9A-F]*)\)")

class ReadFromBytes(Protocol):
    def read(self, save_bytes:bytes) -> Any:
        """implement the ReadFromBytes protocol, returns an empty dict if position couldn't be found

        Args:
            save_bytes (bytes): bytes content of save file

        Returns:
            _type_: _description_
        """
        ...

@dataclass(frozen=True,init=True)
class Data(ABC):
    marker:bytes
    offset:int
    
    @abstractmethod 
    def get_position(self, save_bytes:bytes, start_pos:Optional[int], end_pos:Optional[int]) -> int:
        """
        Args:
            save_bytes (bytes): save data to look through
            start_pos (int | None): optional start position for search
            end_pos (int | None): optional end position for search

        Returns:
            int: position of this piece of data, if it's found in the save data, otherwise -1 if missing
        """
        marker_pos:int = save_bytes.find(
            self.marker,
            start_pos if start_pos else None,
            end_pos if end_pos else None
        )
        return -1 if marker_pos == -1 or marker_pos > len(save_bytes) else marker_pos + self.offset
    