import copy

from swampy.World import World


class Rectangle(object):
    """ represents a rectangle """

class Polygon(object):
    """ represents a polygon """

class Circle(object):
    """ represents a circle """

class Point(object):
    """ represents point on 2D plane """


def draw_rectangle(canvas, rect):
    color = rect.color
    rect = [[rect.corner.x, rect.corner.y], [rect.corner.x + rect.width, rect.corner.y + rect.height]]

    canvas.rectangle(rect, outline=None, fill=color)


def draw_circle(canvas, circle):
    color = circle.color
    center = (circle.x, circle.y)

    canvas.circle(center, circle.radius, outline=None, fill=color)


def draw_polygon(canvas, p):
    color = p.color
    points = [[p.point1.x, p.point1.y], [p.point2.x, p.point2.y], [p.point3.x, p.point3.y],]

    canvas.polygon(points, outline=None, fill=color)


def draw_czech(canvas):
    """ draw the czech flag """
    # outline
    box = Rectangle()
    box.width = 600
    box.height = 400
    box.corner = Point()
    box.corner.x = -300
    box.corner.y = -200
    box.color = 'white'

    draw_rectangle(canvas, box)

    # red box
    box = copy.copy(box)
    box.width = 600
    box.height = 200
    box.color = 'red3'

    draw_rectangle(canvas, box)

    # blue polygon
    p = Polygon()
    p.point1 = Point()
    p.point2 = Point()
    p.point3 = Point()
    p.point1.x = -300
    p.point1.y = -200
    p.point2.x = -300
    p.point2.y = 200
    p.point3.x = 0
    p.point3.y = 0
    p.color = 'RoyalBlue4'

    draw_polygon(canvas, p)


world = World()
canvas = world.ca(width=800, height=600, background='white')

draw_czech(canvas)
world.mainloop()