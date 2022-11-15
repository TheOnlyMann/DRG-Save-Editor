

import re
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, NamedTuple, Optional, Protocol

GUID_RE = re.compile(r".*\(([0-9A-F]*)\)")

class ReadFromBytes(Protocol):
    @staticmethod
    def read(save_bytes:bytes) -> None:
        """implement the ReadFromBytes protocol, returns an empty dict if position couldn't be found
        also saves any read data to a static variable accessed with .data()
        
        
        Args:
            save_bytes (bytes): bytes content of save file

        Returns:
            _type_: _description_
        """
        ...

    @staticmethod
    def data() -> None|Any:
        """returns the data read by read()

        Returns:
            None|Any: data, if it was found
        """
        ...

@dataclass(frozen=True,init=True)
class DataSource(ABC):
    marker:bytes
    offset:int
    
    @abstractmethod 
    def get_position(self, save_bytes:bytes, start_pos:Optional[int], end_pos:Optional[int]) -> int | None:
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
        return None if marker_pos == -1 or marker_pos > len(save_bytes) else marker_pos + self.offset
    