class Point(object):
    """ represents point in 2D space """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            return self.add_point(other)
        else:
            return self.add_tuple(other)

    def add_point(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def add_tuple(self, other):
        x, y = other
        x += self.x
        y += self.y
        return Point(x, y)

p1 = Point(1.2, 5.4)
p2 = Point(3.4, 3.8)
print((2.4, 6.6) + p2)
print(getattr(p1, 'x'))