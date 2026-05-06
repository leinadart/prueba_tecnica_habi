from dataclasses import dataclass


@dataclass
class QueryDataDto:
    year: str
    city: str
    state: str
