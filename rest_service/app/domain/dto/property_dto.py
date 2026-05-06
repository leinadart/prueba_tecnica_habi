from datetime import datetime
from dataclasses import dataclass, field


@dataclass
class PropertyDto:
    address: str
    city: str
    state: str
    price: int
    description: str
    last_update: datetime

    def to_dict(self):
        return {
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "price": self.price,
            "description": self.description
        }