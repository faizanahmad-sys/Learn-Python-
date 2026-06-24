


# TOPIC 1: del KEYWORD
# ============================================================

# del keyword is used to delete an object or attribute from memory

class Car:
    def __init__(self, name):
        self.name = name

c1 = Car("BMW")
print(c1.name)   # Output: BMW

del c1.name      # Deletes the 'name' attribute

# print(c1.name) # This will throw AttributeError because name is deleted


# ============================================================
# TOPIC 2: PRIVATE AND PUBLIC ATTRIBUTES/METHODS
# ============================================================

# Public  -> accessible from anywhere (default in Python)
# Private -> only accessible inside the class (add __ before name)

class CarPrivate:
    __name = "BMW"          # Private attribute (double underscore)

    def __start(self):      # Private method
        print(self.__name)

    def public_info(self):  # Public method (can call private stuff inside)
        self.__start()

obj = CarPrivate()
obj.public_info()           # Works fine

# obj.__name    # ERROR - cannot access private attribute from outside
# obj.__start() # ERROR - cannot access private method from outside


# ============================================================
# TOPIC 3: INHERITANCE
# ============================================================

# Inheritance = Child class derives properties & methods from Parent class
#
# Syntax:
#   class Parent:
#       ...
#   class Child(Parent):
#       ...


# --- Single Inheritance ---

class Vehicle:
    @staticmethod
    def start():
        print("Vehicle is running")

class BMW(Vehicle):
    def __init__(self, price):
        self.price = price

class RollsRoyce(Vehicle):
    def __init__(self, price):
        self.price = price

    @staticmethod
    def stop():
        print("Car is stopped")


bmw = BMW("$100,000")
bmw.start()                         # Inherited from Vehicle
print(f"BMW Price: {bmw.price}")

print("-" * 30)

rr = RollsRoyce("$500,000")
rr.start()                          # Inherited from Vehicle
rr.stop()                           # Own method
print(f"Rolls Royce Price: {rr.price}")


# --- Multi-level Inheritance ---
# Vehicle -> BMW -> RollsRoyce (chain)

class Vehicle2:
    @staticmethod
    def start():
        print("Vehicle is running")

class BMW2(Vehicle2):
    def __init__(self, price):
        self.price = price

class RollsRoyce2(BMW2):            # Inherits from BMW2 which inherits from Vehicle2
    def __init__(self, price):
        super().__init__(price)     # Calls BMW2's constructor

    @staticmethod
    def stop():
        print("Car is stopped")


customer = RollsRoyce2("$500,000")
customer.start()                    # From Vehicle2 (inherited through BMW2)
customer.stop()                     # Own method
print(f"Price: {customer.price}")   # From BMW2 via super()


# ============================================================
# TOPIC 4: super() METHOD
# ============================================================

# super() is used to call parent class methods/constructor inside child class

class Vehicle3:
    def __init__(self):
        self.wheels = 4             # Shared property for all child classes

    @staticmethod
    def start():
        print("Vehicle is running")

class BMW3(Vehicle3):
    def __init__(self, price):
        super().__init__()          # Calls Vehicle3's __init__ -> sets self.wheels
        self.price = price

class RollsRoyce3(Vehicle3):
    def __init__(self, price):
        super().__init__()          # Calls Vehicle3's __init__ -> sets self.wheels
        self.price = price

    @staticmethod
    def stop():
        print("Car is stopped")


bmw3 = BMW3("$100,000")
bmw3.start()
print(f"BMW Price: {bmw3.price}")
print(f"BMW Wheels: {bmw3.wheels}")     # From parent class via super()

print("-" * 30)

rr3 = RollsRoyce3("$500,000")
rr3.start()
rr3.stop()
print(f"RR Price: {rr3.price}")
print(f"RR Wheels: {rr3.wheels}")       # From parent class via super()

# You can also call a specific parent method using super():
# super().start()  -> calls parent's start method inside child


# ============================================================
# TOPIC 5: STATIC METHOD vs CLASS METHOD
# ============================================================

# --- @staticmethod ---
# - Does NOT receive self or cls
# - Cannot access or modify class/instance state
# - Used for utility functions that belong to the class logically

# --- @classmethod ---
# - Receives cls (the class itself) as first argument
# - Can access and modify class-level variables
# - Used when you need to modify class state

# Example - Modifying class variable 3 ways:

# Way 1: Using class name directly
class Person1:
    name = "Default"

    def change(self, name):
        Person1.name = name

p1 = Person1()
p1.change("Ali")
print(p1.name)          # Ali
print(Person1.name)     # Ali


# Way 2: Using self.__class__
class Person2:
    name = "Default"

    def change(self, name):
        self.__class__.name = name

p2 = Person2()
p2.change("Ahmed")
print(p2.name)          # Ahmed
print(Person2.name)     # Ahmed


# Way 3: Using @classmethod (BEST PRACTICE)
class Person3:
    name = "Default"

    @classmethod
    def change(cls, name):
        cls.name = name

p3 = Person3()
p3.change("Faizan")
print(p3.name)          # Faizan
print(Person3.name)     # Faizan


# @property se method ko attribute ki tarah use kar sakte hain
# Aur har baar access karo toh fresh calculate hoti hai

class Student_v2:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def per(self):                                          # Method hai but property ki tarah use hogi
        total = self.phy + self.chem + self.math
        return str(round(total / 300 * 100, 2)) + "%"


s2 = Student_v2(22, 3, 44)
print(s2.per)       # 23.0%  -- s2.per() nahi, sirf s2.per (no brackets needed)

s2.phy = 90         # Marks change kiye
print(s2.per)       # 46.33% -- Automatically update ho gayi!



#know we laern about the polymorphism also operator overloading
"""
when the same operator is allowed to have foffernt meaning according yo the context

"""
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()



#another question
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

def describe_shape(shape):
    print(f"Area: {shape.area()}")

describe_shape(Circle(5))
describe_shape(Rectangle(4, 6))


#another example
class Dog:
    def sound(self):
        print("Woof! 🐶")

class Cat:
    def sound(self):
        print("Meow! 🐱")

class Cow:
    def sound(self):
        print("Moo! 🐄")

# Ab ek hi loop mein sab handle ho gaya ✅
animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()