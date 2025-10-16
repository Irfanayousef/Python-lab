sq_ar=lambda a:a**2
re_ar=lambda l,b:l*b
tri_ar=lambda ba,h:0.5 * ba *h
a=int(input("enter the length"))
print("area of the square:",sq_ar(a))

l=int(input("enter the length:"))
b=int(input("enter the breadth:"))
print("area of the rectangle:",re_ar(l,b))

ba=int(input("enter a base:"))
h=int(input("enter the height:"))
print("area of the triangle",tri_ar(ba,h))
