from dataclasses import dataclass


@dataclass
class Account:
    email: str = None
    password: str = None