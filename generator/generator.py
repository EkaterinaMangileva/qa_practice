from data.data import Account, Register
from faker import Faker

faker_ru = Faker('ru_RU')


def create_account():
    yield Account(
        email=faker_ru.email(),
        password=faker_ru.password(),
    )


def register_account():
    yield Register(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        phone_number=faker_ru.phone_number(),
        email=faker_ru.country(),
        password=faker_ru.password()
    )
