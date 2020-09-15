from custom_import import Base

# complete type checking python
class Player(Base):
    # python 3.6+ class annotation feature
    name: NonEmptyString
    x   : Integer
    y   : Integer

    def left(self, dx: PositiveInteger):
        self.x -= dx

    def right(self, dx: PositiveInteger):
        self.x += dx

print(Player.__annotations__)
