from data.data import Account
from faker import Faker

faker_ru = Faker('ru_RU')


def create_account():
    yield Account(
        email=faker_ru.email(),
        password=faker_ru.password(),
    )