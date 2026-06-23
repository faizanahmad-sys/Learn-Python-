# ============================================================
#   Python OOP - Chapter Notes
#   Author  : Faizan Ahmad (@CodeByFaizan)
#   Topic   : Object-Oriented Programming in Python
# ============================================================


# ------------------------------------------------------------
# CONCEPT: What is OOP?
# Mapping real-world scenarios to code using objects.
# ------------------------------------------------------------


# ------------------------------------------------------------
# 1. CLASS & OBJECT
# ------------------------------------------------------------

class Student:
    name = "Faizan Ahmad"

s1 = Student()
print(s1.name)


# ------------------------------------------------------------
# 2. CONSTRUCTOR (__init__)
# __init__ runs automatically when an object is created.
# 'self' = reference to the current instance of the class.
# ------------------------------------------------------------

class Worker:
    def __init__(self, name, age):
        self.name = name
        self.age = age

w1 = Worker("Faizan", 23)
print(w1.name, w1.age)

w2 = Worker("Ali", 12)
print(w2.name, w2.age)


# ------------------------------------------------------------
# 3. CONSTRUCTOR PRACTICE — Student with department
# ------------------------------------------------------------

class StudentInfo:
    def __init__(self, name, id, department):
        self.name = name
        self.id = id
        self.department = department

s1 = StudentInfo("Faizan", 123, "Software Engineering")
print(s1.name, s1.id, s1.department)


# ------------------------------------------------------------
# 4. PRACTICE QUESTION
# Student class — takes name + marks of 3 subjects
# Method to print average marks
# ------------------------------------------------------------

class StudentMarks:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        total = sum(self.marks)
        avg = total / len(self.marks)
        print(f"Student: {self.name} | Average Marks: {avg}")

s1 = StudentMarks("Faizan", [80, 90, 70])
s1.average()


# ------------------------------------------------------------
# 5. STATIC METHODS
# Methods that don't use 'self' — work at class level.
# Decorated with @staticmethod
# ------------------------------------------------------------

class CollegeStudent:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def department():
        print("ABC College - Software Engineering")

CollegeStudent.department()


# ------------------------------------------------------------
# 6. ENCAPSULATION & ABSTRACTION
#
# Encapsulation : wrapping data + functions into a single unit (object)
# Abstraction   : hiding implementation, showing only what's needed
# ------------------------------------------------------------


# ------------------------------------------------------------
# 7. PRACTICE QUESTION — Bank Account
# Attributes : balance, account number
# Methods    : debit, credit, get_balance
# ------------------------------------------------------------

class Account:
    def __init__(self, balance, acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"RS {amount} debited.")
            print(f"Remaining Balance: RS {self.balance}")

    def credit(self, amount):
        self.balance += amount
        print(f"RS {amount} credited.")
        print(f"Remaining Balance: RS {self.balance}")

    def get_balance(self):
        print(f"Current Balance: RS {self.balance}")
        return self.balance


acc1 = Account(10000, 12344)
acc1.debit(1000)
acc1.credit(500)
acc1.get_balance()