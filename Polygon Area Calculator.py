class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.area = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        self.area = self.width * self.height
        return self.area

    def get_perimeter(self):
        perimeter = (2 * self.height) + (2 * self.width)
        return perimeter

    def get_diagonal(self):
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            img = ''
            width = '*' * self.width
            img += width
            for i in range(self.height - 1):
                img += '\n' + width
            img += '\n'
            return img

    def get_amount_inside(self, shape):
        self.get_area()
        shape.get_area()
        if self.area < shape.area or self.width < shape.width or self.height < shape.height:
            return 0
        else:
            fit = int(self.area/shape.area)
            return fit

    def __str__(self):
        height = str(self.height)
        width = str(self.width)
        show = f'Rectangle(width={width}, height={height})'
        return show


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width=side, height=side)
        self.side = side

    def set_side(self, side):
        super().set_width(width=side)
        super().set_height(height=side)
        self.side = side

    def set_width(self, width):
        super().set_width(width=width)
        self.side = width

    def set_height(self, height):
        super().set_height(width=height)
        # self.side = height

    def __str__(self):
        res = f'Square(side={str(self.side)})'
        return res


rect = Rectangle(10, 5)
sq = Square(9)
rect.set_width(7)
rect.set_height(8)
sq.set_side(2)
print(sq.get_picture())
print('------')
f = "**\n**\n"
print(f)
print('-------')
