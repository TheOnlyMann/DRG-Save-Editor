

import re
from typing import Any, NamedTuple, Protocol

GUID_RE = re.compile(r".*\(([0-9A-F]*)\)")

class ReadFromBytes(Protocol):
    def read(self, save_bytes:bytes) -> Any:
        ...

class Data(NamedTuple):
    marker:bytes
    offset:int 
    