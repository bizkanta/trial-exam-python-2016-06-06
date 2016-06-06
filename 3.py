# Create a class that represents a cuboid:
# It should take it's three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():
    def __init__(self, a, b, m):
        self.a = a
        self.b = b
        self.m = m

    def getSurface(self):
        return 2 * (self.a * self.b + self.a * self.m + self.b * self.m)

    def getVolume(self):
        return self.a * self.b * self.m

cuboid1 = Cuboid(1, 2, 4)
print(cuboid1.getSurface())
print(cuboid1.getVolume())
