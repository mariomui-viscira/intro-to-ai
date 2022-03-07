from typing import Sequence
from dataclasses import dataclass


def kick_dog(type_of_dog: str):
    print('you kicked a {}'.format(type_of_dog))


def kick_cat(type_of_cat: str):
    print('you kicked a {}'.format(type_of_cat))


class Mario:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            # self.kick_dog = kwargs.get('kick_dog')
            print(name)
            setattr(self, name, value)


@dataclass
class NewShit:
    brown_shit: str
    green_shit: str
    wallet: Sequence[int]


class Table:
    def __init__(self, identifier, seat_count):
        self.identifier = identifier  # str
        self.seat_count = seat_count  # int


def tablesWithEnoughSeats(tables: Table, minSeats: int) -> str:
    pass


def main():
    baby = Mario(kick_dog=kick_dog, kick_cat=kick_cat)
    baby.kick_dog('werew')
    baby.kick_cat('dkjfdkj')
    myshit = NewShit(brown_shit='green', green_shit='brown', wallet=(1, 2, 3))
    print(myshit.wallet)


if __name__ == '__main__':
    main()
