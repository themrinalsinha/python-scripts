"""
Cohesion and Coupling
---------------------
Cohesion and Coupling deals with the quality of an Object Oriented design, generally good
OO design should be loosely coupled and highly cohesive.

    Coupling: It is the degree to which once class knows about another class. Let's consider
    two classes A and B. If class A knows class B through its interface only i.e it interacts
    with class B through its API then class A and class B are said to be loosely coupled.

    Cohesion: It is used to indicate the degree to which a class has a single, well-focused purpose.
    Coupling is all about how classes interact with each other, on the other hand cohesion focuses
    on how single class is designed. Higher the cohesiveness of the class, better the OO design.
"""

# Cohesion and Coupling example code
# ----------------------------------
import string, random


class VehicleRegistry:

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.ascii_uppercase + string.digits, k=3))}-{''.join(random.choices(string.ascii_uppercase + string.digits, k=3))}"


class Application:

    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license place for the vehicle using the first two characters
        # of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)

        # compute the catalogue price
        catalogue_price = 0
        if brand == "Toyota":
            catalogue_price = 100000
        elif brand == "Ford":
            catalogue_price = 200000
        elif brand == "BMW":
            catalogue_price = 300000
        elif brand == "Mercedes":
            catalogue_price = 400000

        tax_percentage = 0.05

        payable_tax = tax_percentage * catalogue_price

        print(
            "Registration complete. Vehicle information\n"
            f"Brand: {brand}\n"
            f"ID: {vehicle_id}\n"
            f"License Plate: {license_plate}\n"
            f"Catalogue Price: {catalogue_price}\n"
            f"Tax: {payable_tax}\n"
        )

app = Application()
app.register_vehicle("Toyota")

"""
As we can see in the above code, in Application class register_vehicle method, we have created
it is doing a lot of things, like generating a vehicle id, generating a license plate, computing
the catalogue price, computing the tax. etc etc. This is a lot of work and it is not a good. Means
this method has very low cohesion, way too many responsibility, it is also very high coupling
means it is directly relying on VehicleRegistration class. Also adding new brand of car
is a problem etc etc.

Let's try to make this code better.
"""

class VehicleInfo:
    brand: str
    electric: bool
    catalog_price: int

    def __init__(self, brand: str, electric: bool, catalog_price: int):
        self.brand = brand
        self.catalog_price = catalog_price
        self.electric = electric

    def compute_tax(self, tax_percentage: float = 0.5):
        if self.electric:
            tax_percentage = 0.1
        return tax_percentage * self.catalog_price

    def print(self):
        print(
            f"Brand: {self.brand}\n",
            f"Payable tax: {self.compute_tax()}"
        )

class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id: str, license_plate: str, info: VehicleInfo):
        self.id = id
        self.license_plate = license_plate
        self.info = info

    def print(self):
        print(
            f"ID: {self.id}\n",
            f"License Plate: {self.license_plate}\n",
            self.info.print()
        )

class VehicleRegistry:

    def __init__(self) -> None:
        self.add_vehicle_info("Tesla", True, 50000000)
        self.add_vehicle_info("Toyota", False, 100000)
        self.add_vehicle_info("Ford", False, 200000)
        self.add_vehicle_info("BMW", False, 300000)


    vehicle_info = {}

    def add_vehicle_info(self, brand, electric, catalogue_price):
        self.vehicle_info[brand] = VehicleInfo(brand, electric, catalogue_price)

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.ascii_uppercase + string.digits, k=3))}-{''.join(random.choices(string.ascii_uppercase + string.digits, k=3))}"

    def create_vehicle(self, brand: str):
        vehicle_id = self.generate_vehicle_id(12)
        license_plate = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, license_plate, self.vehicle_info[brand])

class Application:
    def register_vehicle(self, brand: str):
        registry = VehicleRegistry()
        vehicle = registry.create_vehicle(brand)
        vehicle.print()

app = Application()
app.register_vehicle("Toyota")

