from abc import ABC
from dataclasses import dataclass
from typing import TypeVar, Generic

from domain.events.base import BaseEvent

ET = TypeVar('ET', bound=BaseEvent)
ER = TypeVar('ER', bound=BaseEvent)

@dataclass
class EventHandler(ABC, Generic[ET]):
    def handle(self, event: ET) -> ER:
        ...