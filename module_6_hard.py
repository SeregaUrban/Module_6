class Figure:
    sides_count = 0
    __sides = []
    __color = []
    filled = False

    def __init__(self, colors, *side):
        self.colors = list(colors)
        self.side = side[0]
        self.filled = True

    def get_color(self):
        self.__color = self.color
        self.filled = True
        return self.__color

    def __is_valid_color(self,r,g,b):
        self.r = r
        self.g = g
        self.b = b
        if 0 <= self.r and self.g and self.b <= 255:
            return True
        else:
            return False

    def set_color(self,r,g,b):
        if self.__is_valid_color(r,g,b):
             self.color = [self.r, self.g, self.b]
        else:
            return self.set_color()

    def __is_valid_sides (self,*number_of_sides):
        if isinstance(number_of_sides,int) and number_of_sides == len(self.__sides):
            return True
        else:
            return False

    def get_sides(self):
        self.__sides = self.sides
        return self.__sides

    def __len__ (self):
        return self.side * self.sides_count

    def set_sides(self, *sides):
        massive = []
        self.sides = list(sides)
        if self.__is_valid_sides(self, *sides):
            self.get_sides()
        else:
            for i in range(self.sides_count):
                massive.append(self.side)
            self.sides = massive
            self.get_sides()


class Circle(Figure):
    sides_count = 1
    __radius = None

    def get_square(self):
        self.__radius = self.__len__() / (2 * 3.14)
        return self.__radius


class Triangle(Figure):
    sides_count = 3
    __heignt = None

    def get_square(self):
        return (self.side ** 2) * (3 ** 0.5) / 4

    def set_height(self):
        self.__height = self.side * (3 ** 0.5) / 2
        return self.__height
class Cube(Figure):
    sides_count = 12

    def new__sides(self):
        new__sides = []
        if element in range(self.sides_count):
            new__sides.append(self.side)
        self.__sides = new__sides
        return self.__sides

    def get_volume(self): 
        return self.side ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(10) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())