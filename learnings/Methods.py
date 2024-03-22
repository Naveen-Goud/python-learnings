class MyClass:
    def say_hello(self):
        print("Hello!")

obj = MyClass()
obj.say_hello()



class Calculator:
    def add(self, num1, num2):
        return num1 + num2

calc = Calculator()
result = calc.add(5, 3)
print("Result of addition:", result)  


class MathUtility:
    @staticmethod
    def add(x, y):
        return x + y

result = MathUtility.add(5, 3)
print("Result of addition:", result)


class Car:
    num_cars = 0
    def __init__(self, name):
        self.name = name
        Car.num_cars += 1
    @classmethod
    def display_num_cars(cls):
        return cls.num_cars


car1 = Car("Toyota")
car2 = Car("Honda")
car3 = Car("BMW")
print("Number of cars created:", Car.display_num_cars())

