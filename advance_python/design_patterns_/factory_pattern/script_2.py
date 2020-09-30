
"""
Let's start with the kid's game. It is called FrogWorld. The main hera is frog who
enjoys eating bugs. Every hero needs a good name, and our case the name is give by
the user in runtime. The interact_with() method is used to describe the interaction
for the frog with an obstacle
"""
class Frog:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle):
        print(f'{self} the frog encounters {obstacle} and {obstacle.action()}')

"""
There can be many different kinds of obstacles but for our example an obstacle
can only be a Bug . When the frog encounters a bug, only one action is supported:
it eats it!
"""
class Bug:
    def __str__(self) -> str:
        return 'a bug'

    def action(self):
        return 'eats it'

"""
The FrogWorld class is an Abstract Factory. Its main responsibilities are creating
the main character and the obstacle(s) of the game. Keeping the creation methods
separate and their names generic (for example, make_character() , make_obstacle() )
allows us to dynamically change the active factory (and therefore the active game)
without any code changes.
"""
class FrogWorld:
    def __init__(self, name) -> None:
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return '\n\n\t------ Frog World -------'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


"""
The WizardWorld game is similar. The only differences are that the wizard battles against
monsters like orks instead of eating bugs!
"""
class Wizard:
    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name

    def interact_with(self, obstacle):
        print(f'{self} the wizard battles against {obstacle} and {obstacle.action()}')

class Ork:
    def __str__(self) -> str:
        return 'an evil ork'

    def action(self):
        return 'kills it'

class WizardWorld:
    def __init__(self, name) -> None:
        print(self)
        self.player_name = name

    def __str__(self) -> str:
        return '\n\n\t------ Wizard World -------'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()

"""
The GameEnvironment is the main entry point of our game. It accepts factory as an input,
and use it to create the world of the game. The play() method initiates the interaction
between the created hero and the obstacle as follows
"""
class GameEnvironment:
    def __init__(self, factory) -> None:
        self.hero     = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)

"""
The validate_age() function prompts the user to give a valid age. If the age is not valid,
it returns a tuple with the first element set to False. If the age is fine, the first element
of the tuple is set to True and that's the case where we actually care about the second element
of the tuple, which is the age given by the user as follows
"""
def validate_age(name):
    age = None
    try:
        age = int(input(f"Welcome {name}. How old are you ? "))
    except ValueError as err:
        print(f"Age {age} is invalid, please try again...")
        return False, age
    return True, age

"""
Last but not the lease comes the main() function. It asks for the user's name and age, and
decides which game should be played by the age of the user as follows
"""
def main():
    name = input("Hello, What's your name ? ")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = FrogWorld if age < 18 else WizardWorld
    environment = GameEnvironment(game(name))
    environment.play()

if __name__ == '__main__':
    main()
