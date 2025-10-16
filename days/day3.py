#arithmetic operators
friend=5
friend+=1
print(friend)
friend-=2
print(friend)
friend*=2
print(friend)
friend/=2
print(friend)
friend**=2
print(friend)
remainder=friend%3
print(remainder)

#functions
x=3.4
y=-4
z=5
result=round(x)
print(result)

is_y=abs(y)
print(is_y)

result=pow(4,3)
print(result)

result=max(x, y, z)
print(result)

result=min(x,y,z)
print(result)

import math
print(math.pi)

#square root 
x=16.9
result=math.sqrt(x)
print(result)

#floor and ceil
result=math.floor(x)
print(result)
result =math.ceil(x)
print(result)

#circumference of a circle 2pir
radius=float(input("Enter The Radius Of The Circle"))
circumference=2*math.pi*radius
print(f"the circumference of the circle is {round(circumference)} cm")

#area of the circle pi r square
radius=float(input("Enter The Radius Of The Circele: "))
area=math.pi*radius
print(f"The Area Of Your Circle Is: {round(area,2)}")

#finding the hypotenuse
a=float(input("Enter The First Side Of Your Triangle: "))
b=float(input("Enter The Secound Side Of Your Triangle: "))
c=math.sqrt(pow(a,2)+pow(b,2))
print(f"The Hypotenuse Of The Given Triangle Is {c}cm ")