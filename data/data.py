from dataclasses import dataclass


@dataclass
class Account:
    email: str = None
    password: str = None


@dataclass
class Register:
    first_name: str = None
    last_name: str = None
    phone_number: str = None
    email: str = None
    password: str = None
