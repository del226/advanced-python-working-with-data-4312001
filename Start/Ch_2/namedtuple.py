# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
Point = collections.namedtuple("Point", "x y")
p1 = Point(10,20)
p2 = Point(4, 5)
p3 = Point(p1.x+p2.x, p1.y+p2.y)
print(p3)
# TODO: use _replace to create a new instance
p1 = p1._replace(x=100)
print(p1)
