from swampy.World import World

class Rectangle(object):
    """ represents a rectangle """

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


def draw_point(canvas, point):
    canvas.circle((point.x, point.y), 2, outline=None, fill='black')


world = World()
box = Rectangle()
box.width = 300
box.height = 200
box.corner = Point()
box.corner.x = -150
box.corner.y = -100
box.color = 'red'

c = Circle()
c.x = 0
c.y = 0
c.radius = 50
c.color = 'blue'

canvas = world.ca(width=800, height=600, background='white')

draw_rectangle(canvas, box)
draw_circle(canvas, c)
world.mainloop()