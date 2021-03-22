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


print(f'{"Advance default feature":=^50}')
"""
Say that you want to give a default value to a Deck. It would for example be convenient
if Deck() created a regular french deck of 52 playing cards.
"""
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = 'H C S A'.split()

def make_french_deck():
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]
print(make_french_deck())

# Now, In theory, you could now use this function to specify a default value of Deck.cards
"""
@dataclass
class Deck: # will NOT work
    cards: List[PlayingCard] = make_french_deck()

Don't do this! It introduces one of the most common anti-patterns in Python: using mutable default
arguments. The problem is that all instance of Deck will use the same list object as the default
value of the .card property. This means that if, say, one card is removed from one Deck, then it
disappears from all the other instances of Deck as well.

Actually, data classes try to prevent you from doing this, and the code above will raise a valueError
Instead, data classes use something called a default_factory to handle mutable default values. To use
default_factory(and many other cool features of data classes), you need to use the field() specifier
"""
from typing      import List
from dataclasses import dataclass, field

@dataclass
class Deck:
    cards: List[PlayingCard] = field(default_factory=make_french_deck)
# NOTE: The argument of default_factory can be any zero parameter callable. Now it is easy to
#       create a full deck of playing cards
print(Deck())


# The field() specifier is used to customize each field of a data class individually. You will see
# some other examples later. For reference, these are the parameters field() supports:

# default: Default value of the field
# default_factory: Function that returns the initial value of the field
# init - use field in .__init__() method? (default=True)
# repr: Use field in repr of the object? (default=True)
# compare: Include the field in comparison ? (default=True)
# hash: Include the field when calculating hash()
# metadata: A mapping with information about the field


# In the Position example, we saw how to add simple default values by writing lat: float = 0.0.
# However, if you also want to customize the field, for instance to hid it in the repr, you need
# to use the default parameter: lat: float = field(default=0.0, repr=False) you many not specify
# both default and default_factory.

# The metadata parameter is not used by the data classes themselves but is available for you
# (or third party packages) to attach information to fields. In the Position example, you  could
# instance specify that latitude and longitude should be given in degrees.
print(f'{"Working with fields":=^50}')

@dataclass
class Position:
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})

# The metadata (and other information about a field) can be retrieved using the fields()
# function (not the plural s)
from dataclasses import fields
print(fields(Position))
lat_unit = fields(Position)[2].metadata['unit']
print(lat_unit)
