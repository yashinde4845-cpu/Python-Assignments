# Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# Subclass Car
class Car(Vehicle):
    def move(self):   # overriding move() method
        print("Driving on the road")

# Subclass Bicycle
class Bicycle(Vehicle):
    def move(self):   # overriding move() method
        print("Pedaling on the road")

# Demonstrating polymorphism
v1 = Car()
v2 = Bicycle()

v1.move()   # calls Car's move()
v2.move()   # calls Bicycle's move()
