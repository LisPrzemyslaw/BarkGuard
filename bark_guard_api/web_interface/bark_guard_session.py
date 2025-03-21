from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from collections import deque

streaming_sessions: dict[int: Stream] = {}  # user_id: Stream


@dataclass
class Stream:
    start_time: datetime = field(default_factory=lambda: datetime.now())
    records: deque = field(default_factory=lambda: deque())
    is_session_end: bool = False
