from Graphics.RectFunctions import RectArea
from Graphics.RectFunctions import RectPerimeter
from Graphics.CirFunctions import CirArea
from Graphics.CirFunctions import CirPerimeter
from Graphics.DGraphics.SphereFunctions import SpArea
from Graphics.DGraphics.SphereFunctions import SpPerimeter
from Graphics.DGraphics.CuboidFunctions import CubArea
from Graphics.DGraphics.CuboidFunctions import CubPerimeter
l=int(input("enter length:"))
b=int(input("enter breadth:"))
print("Rectangle Area=",RectArea(l,b))
print("Rectangle Perimeter=",RectPerimeter(l,b))

r=int(input("enter radius of Circle:"))
print("Circle Area=",CirArea(r))
print("Circle Perimeter=",CirPerimeter(r))

r=int(input("enter radius of sphere:"))
print("Sphere Area=",SpArea(r))
print("Sphere Volume=",SpPerimeter(r))

l=int(input("enter cuboid length:"))
b=int(input("enter cuboid breadth:"))
h=int(input("enter cuboid height:"))
print("Cuboid Area=",CubArea(l,b,h))
print("Cuboid Perimeter=",CubPerimeter(l,b,h))
