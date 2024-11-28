import math


class Figure():
    sides_count = 0
    def __init__(self,color, *sides, fille = False):
        self.__sides = list(sides)
        self.__color = list(color)
        self.fille = fille

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        type = 0 <= r <= 255 and 0<= g <= 255 and 0<= b <= 255
        isi = isinstance(r,int) and isinstance(g,int) and isinstance(b,int)
        return type and isi

    def set_color (self,r,g,b):
        if self.__is_valid_color(r,g ,b):
             self.__color = [r ,g ,b]

    def __is_valid_sides(self, *sides):
        for side in sides:
            if not isinstance(side, int) or side <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
         return sum(self.__sides)

    def set_sides(self, *sides):
        if len(sides) == len(self.__sides) and self.__is_valid_sides(*sides):
            self.__sides = list(sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self,color, lend,  fille=False):
        super().__init__(color,  lend, fille=fille)
        self.__radius = lend/(2 * math.pi)

    def get_square(self):
        return len(self) **2 / (4 * math.pi)

class Triangle(Figure):
    sides_count = 3
    def __init__(self,color,*sides,fille=False):
        super().__init__(color,*sides, fille = fille )

    def get_square(self):
        p = self.__len__() * 0.5
        self.get_sides()
        s = math.sqrt(p*(p-self.sides[1])*(p-self.sides[2])*(p-self.sides[3]))

class Cube(Figure):
    sides_count = 12
    def __init__(self,color,sides, fille = False):
        cube_sides = [sides] * 12
        super().__init__(color, *cube_sides, fille = fille)

    def get_volume(self):
        return self.get_sides()[0] ** 3

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
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



