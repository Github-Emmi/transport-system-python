# transport_system.py

# Base Class
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} is moving at {self.speed} km/h.")

# Derived Classes (Polymorphism)
class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving smoothly on the road at {self.speed} km/h. 🚗")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying in the sky at {self.speed} km/h. ✈️")

class Ship(Vehicle):
    def move(self):
        print(f"{self.name} is sailing across the sea at {self.speed} km/h. 🚢")

# Encapsulation Example
class Ticket:
    def __init__(self, passenger_name, vehicle: Vehicle, seat_number):
        self.__passenger_name = passenger_name  # private attribute
        self.__vehicle = vehicle
        self.__seat_number = seat_number

    def get_ticket_details(self):
        return f"Passenger: {self.__passenger_name}\n" \
               f"Vehicle: {self.__vehicle.name}\n" \
               f"Seat No: {self.__seat_number}"

# Instantiate vehicles
car = Car("Tesla", 120)
plane = Plane("Boeing 747", 850)
ship = Ship("Titanic", 40)

# Demonstrate Polymorphism
vehicles = [car, plane, ship]
for v in vehicles:
    v.move()

# Create a ticket
ticket = Ticket("Aghason Emmanuel", plane, "A21")
print("\n--- Ticket Details ---")
print(ticket.get_ticket_details())
