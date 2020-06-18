import math

from turtle_classes import *

class Tagger(Wobbler):
    """ represents a tagger class """
    def steer(self):
        print(self.color)
        print(self.heading)
        j = None
        z = None
        for t in self.world.animals:
            if t == self:
                continue

            d = math.sqrt((t.x - self.x)** 2 + (t.y - self.y)** 2)
            
            if j == None:
                self.heading = (math.degrees(math.atan2(t.y, t.x)))
                j = d
                z = t

            elif d < j:
                self.heading = (math.degrees(math.atan2(t.y, t.x)))
                j = d
                z = t

        print(z.color)
        print()


        if (abs(self.x) >= 180 or abs(self.y) >= 180):
            self.heading = (math.degrees(math.atan2(self.y, self.x))) + 180





world = make_world(Tagger)
world.mainloop()