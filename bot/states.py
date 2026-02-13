# bot/states.py
from dataclasses import dataclass
from typing import Optional

@dataclass
class RegState:
    step: str
    travel_id: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    father_name: Optional[str] = None
    phone_number: Optional[str] = None
    passport_file_id: Optional[str] = None

USER_STATE: dict[int, RegState] = {}
