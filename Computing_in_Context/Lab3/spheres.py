# The sphere module has functions that perform
# calculations related to spheres.
import math

pi=math.pi

# The surface function accepts a sphere's radius as 
# an argument and returns the sphere's surface area.
def surface(radius):
    return 4 * math.pi * (radius**2)

# The volume function accepts a sphere's radius as an
# argument and returns the volume of the sphere.
def volume(radius):
    return (4/3) * math.pi * (radius ** 3)