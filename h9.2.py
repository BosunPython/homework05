"""Создать класс Прямоугольник, который имеет свойства Ширина и Высота.
Также добавить свойство для нахождения площади.
Свойства реализовать через property"""

class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width
    @property
    def height(self):
        return self._height
    @property
    def width(self):
        return self._width
    @height.setter
    def height(self, new_height):
        self._height = new_height
    @width.setter
    def width(self, new_width):
        self._width = new_width
    def area(self):
        if self.width <= 0 or self.height <= 0:
            return "negative"
        else:
            return self.width * self.height


object1 = Rectangle(5, 7)
print(object1.area())
