



# Assignment 2: Demonstrating OOP Concepts in Python
# Objective:
# Create a Python program that demonstrates inheritance, polymorphism, and the use of global, module, object, and local variables using real-world classes.
# Instructions:
# Inheritance and Polymorphism:
# Create a base class Vehicle with a method start_engine that prints "Engine started."
# Create a derived class Car that inherits from Vehicle and overrides the start_engine method to print "Car engine started."
# Create another derived class Bike that inherits from Vehicle and overrides the start_engine method to print "Bike engine started."
# Global Variable:
# Define a global variable traffic_light with the value "Green".
# Module Variable:
# Define a module-level variable speed_limit with the value 60.
# Object Variable:
# In the Car class, define an object variable make that stores the make of the car.
# In the Bike class, define an object variable type that stores the type of bike.
# Local Variable:
# In each start_engine method, define a local variable message that stores the respective message to be printed
class Vehicle:

    # traffic_light = "Green"

    def __init__(self, speed_limit):
        self.speed_limit = speed_limit

    def start_engine(self):
        print("Engine started")


class Car(Vehicle):

    def __init__(self): Vehicle(self)

    def start_engine(self):
        print("Car engine started")


class Bike(Vehicle):
    def __init__(self): Vehicle(self)

    def start_engine(self):
        print("Bike engine started")


v1 = Vehicle(60)
v1.start_engine()

c1 = Car()
c1.start_engine()
b1 = Bike()
b1.start_engine()

        
        
        