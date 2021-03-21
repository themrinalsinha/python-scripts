"""
Data Classes in Python 3.7+

A dataclass is a class typically containing mainly data, although there aren't
really any restrictions. It is created using the new @dataclass decorator
"""

from dataclasses import dataclass, make_dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str

# a data class comes with basic functionality already implemented. For instance, you
# can instantiate, print, and compare data class instances straight out of the box

queen_of_hearts = DataClassCard('Q', 'Hearts')
print(f'{"DataClass":=^50}')
print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == DataClassCard('Q', 'Hearts'))

# compare that to a regular class. A minimal regular class would look something like this:
class RegularClass:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

# while this is not much code to write, you can already see signs of the boilerplate pain:
# rank and suits both repeated three times simply to initialize an object. Furthermore, if
# you try to use this plain class, you'll notice that the representation of the objects is
# not very descriptive, and for some reason a queen of hears is not the same as queen of hearts...
queen_of_hearts = RegularClass('Q', 'Hearts')
print(f'{"RegularClass":=^50}')
print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == RegularClass('Q', 'Hearts'))

# Seems like data classes are helping us out behind the scenes. By default, data classes implement
# a.__repr__() method to provide a nice string representation and an .__eq__() method that can do basic
# object comparisons. For the RegularCard class to imitate the data class above, you need to add these
# methods as well.
class RegularClass:
    def __init__(self, rank, suit) -> None:
        self.rank = rank
        self.suit = suit

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, o: object) -> bool:
        if o.__class__ is not self.__class__:
            return NotImplementedError
        return (self.rank, self.suit) == (o.rank, o.suit)

queen_of_hearts = RegularClass('Q', 'Hearts')
print(f'{"RegularClass [UPDATED]":=^50}')
print(queen_of_hearts.rank)
print(queen_of_hearts)
print(queen_of_hearts == RegularClass('Q', 'Hearts'))

# install attrs -< pip install attrs

# ======================================================
# Alternative
# ======================================================
import attr

@attr.s
class AttrCard:
    rank = attr.ib()
    suit = attr.ib()

# ======================================================
# Basic Data Classes
# ======================================================
from dataclasses import dataclass

@dataclass
class Position:
    name: str
    lon: float
    lat: float

# What makes this a class is the @dataclass decorator
print(f'{"Basic Data Class":=^50}')
pos = Position('oslo', 10.8, 59.9)
print(pos)
print(pos.name, pos.lon, pos.lat)

# you can also create data classes similarly to how namedtuples are created.
print(f'{"make_dataclass":=^50}')
Position = make_dataclass('Position', ['name', 'lat', 'lon'])
print(Position)

# dataclass with default value
@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

# Type Hints
from typing import Any

@dataclass
class WithoutExplicitTypes:
    name: Any
    value: Any = 42


print(f'{"Adding methods in dataclass":=^50}')

from dataclasses import dataclass
from math import asin, cos, radians, sin, sqrt

@dataclass
class Position:
    name: str
    lon: float = 0.0
    lat: float = 0.0

    def distance_to(self, other):
        r = 6371 # Earth radius in kilometers
        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)

        h = (sin((phi_2 - phi_1) / 2) ** 2 + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2) ** 2)
        return 2 * r * asin(sqrt(h))

oslo = Position('oslo', 10.8, 59.0)
vanc = Position('Vanc', -123.1, 49.3)
print(oslo.distance_to(vanc))
# ---------------------------------------------------------------------------------------------------
print(f'{"More Flexible data classes":=^50}')

# More Flexible Data Classes
# --------------------------
from dataclasses import dataclass
from typing import List

@dataclass
class PlayingCard:
    rank: str
    suit: str

@dataclass
class Deck:
    cards: List[PlayingCard]

qoh = PlayingCard('Q', 'Hearts')
aos = PlayingCard('A', 'Spade')

two_cards = Deck([qoh, aos])
print(qoh)
print(aos)
print(two_cards)
