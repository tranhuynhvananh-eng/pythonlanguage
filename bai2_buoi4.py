class Shape:
    def describe(self):
        return "This is a generic shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def describe(self):
        return f"This is a circle with radius = {self.radius}."


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def describe(self):
        return f"This is a rectangle with length = {self.length} and width = {self.width}."

shapes = [
    Circle(5),
    Rectangle(4, 7),
    Circle(10),
    Rectangle(2, 3),
]
for s in shapes:
    print(s.describe())