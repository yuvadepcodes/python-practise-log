#exercise 1 area of a rectangle 
l=float(input("Enter The Length Of The Rectangle: "))
b=float(input("Enter the Bridth Of The Rectangle: "))
area=l*b
print(f"the area of the rectangle is {area}cm")

#exercise 2 shopping cart
item=input("what item would u like to buy ?")
price=float(input("whats the price of it  "))
quantity=float(input("how many would u like to have ? "))
total=price*quantity
print(f"your items are {item} for {price}*{quantity}")
print(f"your total come to {total}")

#exercise 3 madlibs game
place=input("enter a place which u like ")
person=input("enter the name of Your Friend ")
activity=input("Enter A Activity You Like The Most ")
place2=input("enter the place ")
print(f"Today i went to {place}")
print(f"there i saw {person}")
print(f"we both did some {activity} which we enjoyed of course ")
print(f"then we went to {place2}")