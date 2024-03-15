print("hello")
print(123)
print("navven" + " 123")
print(123+234)


#example of classes and its implementation
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    @classmethod
    def set_pi(cls, new_pi):
        cls.pi = new_pi

circle1 = Circle(5)
circle2 = Circle(7)
print(circle1.area())
print(circle2.area())

Circle.set_pi(3.14159)
print(circle1.area())
print(circle2.area())


#comparision operators
#equal to operator
a = 5
b = 5
print(a == b)

#Not Equal to
a = 5
b = 10
print(a != b)

#Greater than
a = 10
b = 5
print(a > b)

#less than operator
a = 5
b = 10
print(a < b)

#Greater than or equal to
a = 10
b = 10
print(a >= b)

#less than or equal to
a = 5
b = 10
print(a <= b)
