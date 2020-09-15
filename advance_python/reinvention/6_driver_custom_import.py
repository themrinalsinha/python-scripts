from reinvention.custom_import import PositiveInteger
from custom_import import Base

dx: PositiveInteger

# complete type checking python
class Player(Base):
    # python 3.6+ class annotation feature
    name: NonEmptyString
    x   : Integer
    y   : Integer

    # def left(self, dx: PositiveInteger):
    def left(self, dx):
        self.x -= dx

    # def right(self, dx: PositiveInteger):
    def right(self, dx):
        self.x += dx

print(Player.__annotations__)
