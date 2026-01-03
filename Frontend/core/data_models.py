from dataclasses import dataclass
from typing import Optional, Dict

@dataclass
class MultimodalInput:
    text: Optional[str]
    cursor_position: Optional[tuple]
    active_app: Optional[str]
    confidence: float
