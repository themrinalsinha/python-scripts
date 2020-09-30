"""
We start with importing the required modules and declaring a few Enum parameters plus
a constant that is used many times in the application. The STEP_DELAY constant is used
to add a time delay between the different steps of preparing a pizza as follows
"""
from time import sleep
from enum import Enum

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough    = Enum('PizzaDough',    'thin thick')
PizzaSauce    = Enum('PizzaSauce',    'tomato creme_fraiche')
PizzaTopping  = Enum('PizzaTopping',  'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')

STEP_DELAY    = 3 # in seconds for the sake of the example

"""
Our end product is a pizza, which is described by the Pizza class. When using the Builder
pattern, the end product does not have many responsibilities, since it is not supposed to be
instantiated directly. A builder creates an instance of the end product and makes sure that
is properly prepared.
"""
class Pizza:
    def __init__(self, name) -> None:
        self.name    = name
        self.dough   = None
        self.sauce   = None
        self.topping = []

    def __str__(self) -> str:
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f"Preparing the {self.dough.name} dough of your {self}...")
        sleep(STEP_DELAY)
        print(f"Done with the {self.dough.name} dough !! :)")

"""
There are two builders: one for creating a margrita pizza (MargaritaBuilder) and another
for creating a creamy bacon pizza (CreamyBaconBulder) Each builder creates a Pizza instance
and contains methods that follow the pizza-making procedure: prepare_dough(), add_sauce()
add_topping() and bake()
"""

class MargaritaBuilder:
    def __init__(self) -> None:
        self.pizza       = Pizza("margarita")
        self.progress    = PizzaProgress.queued
        self.baking_time = 5 # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print("adding the tomato sauce to your margrita...")
        self.pizza.sauce = PizzaSauce.tomato
        sleep(STEP_DELAY)
        print("done with the tomato sauce")

    def add_topping(self):
        print("adding the topping (double mozarella, oregano) to your margarita")
        self.pizza.topping.append([i for i in (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        sleep(STEP_DELAY)
        print("done...")

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder:
    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7 # in seconds for the sake of the example

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the crème fraîche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        sleep(STEP_DELAY)
        print('done with the crème fraîche sauce')

    def add_topping(self):
        print('adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon')
        self.pizza.topping.append([t for t in (PizzaTopping.mozzarella, PizzaTopping.bacon,
                                                PizzaTopping.ham,PizzaTopping.mushrooms, PizzaTopping.red_onion, PizzaTopping.oregano)])
        sleep(STEP_DELAY)
        print('done with the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')

"""
The director in this example is waiter. The core of the Waiter class is the construct_pizza() method,
which accepts a builder as a parameter and executes all the pizza preparation steps in the right order.
Choosing the appropriate builder, which can even be done in running, gives us the ability to create
different pizza styles without modifying any code of the director (Waiter). The Waiter class
also contains the pizza() method, which returns the end product (prepared pizza)
"""
class Waiter:
    def __init__(self) -> None:
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough,
                             builder.add_sauce,
                             builder.add_topping,
                             builder.bake)]

    @property
    def pizza(self):
        return self.builder.pizza

"""
The validate_style() function is similar to validate_age() function as described in factory method
It is used to make sure that the user gives valid input, which in this case is a character that
is mapped to a pizza builder. The m character uses the MargaritaBuilder class and the c character
uses CreamyBaconBuilder class. These mapping are in the builder parameter. A tuple is returned, with
the first element set to True if the input is valid, or False if it is invalid.
"""
def validate_style(builders):
    try:
        pizza_style = input("What pizza would you like, [m]argarita or [c]reamy bacon: ")
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print("Sorry, only m or c are available")
        return (False, None)
    return (True, builder)

"""
The last part is the main() function. The main() function contains a code for instantiating
a pizza builder. It uses Waiter director for preparing the pizza.
"""
builder = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
valid_input = False
while not valid_input:
    valid_input, builder = validate_style(builder)
print()
waiter = Waiter()
waiter.construct_pizza(builder)
pizza = waiter.pizza
print()
print(f"Enjoy your {pizza}!")
print('- ' * 50)
# =================================================================================

"""
FLUTENT BUILDER
An interesting variation of the builder pattern where calls to builder methods are chained.
The is accomplished by defining the builder itself as an inner class and returning itself from
each of the setter-like methods on it. The build() method returns the final object
The pattern is called Fluent builder.
"""

class Pizza:
    def __init__(self, builder) -> None:
        self.garlic       = builder.garlic
        self.extra_cheese = builder.extra_cheese

    def __str__(self) -> str:
        garlic = 'yes' if self.garlic else 'no'
        cheese = 'yes' if self.extra_cheese else 'no'
        info   = (f'Garlic: {garlic}', f'Extra cheese: {cheese}')
        return '\n'.join(info)

    class PizzaBuilder:
        def __init__(self) -> None:
            self.extra_cheese = False
            self.garlic       = False

        def add_garlic(self):
            self.garlic = True
            return self

        def add_extra_cheese(self):
            self.extra_cheese = True
            return self

        def build(self):
            return Pizza(self)

pizza = Pizza.PizzaBuilder().add_garlic().add_extra_cheese().build()
print(pizza)
