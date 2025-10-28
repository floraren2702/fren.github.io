# The cylinder module has functions that perform
# calculations related to cylinders.
import math

pi=math.pi

# The surface function accepts a cylinder's radius and height as
# arguments and returns the surface area of the cylinder.
def surface(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius**2

# The volume function accepts a cylinder's radius and height as
# arguments and returns the cylinder's volume.
def volume(radius, height):
    return math.pi * radius ** 2 * height