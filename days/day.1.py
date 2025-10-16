print("hello world")
name="Yuvadep"
food="Biriyani"


print(name)         #using f string
print(f"hello {name}") 
print(f"How Have you Been {name}")
print(f"You Like {food}")

#boolean variable 
is_student=True
grad=False
if is_student:
    print("you are a student")
else :
    print("you are not a student ")    
if grad:
    print("he is a good student ")
else:
    print("he is not a good student ")

#type casting 
name= "brocode" 
a=123
b=3.56
c=True

print(type(name))   
print(type(a))
print(type(c))

a=float(a)
print(a)

print(type(a))
name=bool(name)
print(name)

#input funtion input()
name=input("what is your name: ")
age=int(input("what is your age"))
age=age+1
print(f"hello {name} How Are You")
print(f"Happ Birthday You are {age} Years old")
#day 1 in setting up, creating a repo, cloning it and started with basis like data types, variables and input function. 
#practise session 

is_name=bool(name)
if is_name:
    print("ok go ahead ")
else:
    print("please give a name:")
if age >=18:
    print ("you are eligible ")
else:
    print("sorry ! you are not eligible:")
if age >=18:
    a=input("What Are You Studtying")
is_a=bool(a)
if is_a:
    print("Good Study Well. All The Best!")
else:
    print("you are a crackhead!")
