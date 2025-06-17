from abc import ABC, abstractmethod
from typing import List, Dict, Any


class CommandHandler(ABC):
    @abstractmethod
    def handle(self, data: List[Dict], args: Any) -> List[Dict]:
        pass
