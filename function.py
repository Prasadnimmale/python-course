# functions in python - block of reusable code created using def
# function types
#                 -simple function
#                 -parameter function
#                 -return function
#def greet():   
#    print("welcome to office!")    

#greet()

#simple function
#def good():
#    print("Hi")

#good()
#good()

#parameter function
#def m(a,b):
#   print(a+b)
#m(10,20)
#m(40,60)

#return function
#def gret(a,b):
#    return a+b
#print(gret(10,20))

#print(gret(70,30))


# Other function types

#  -default arguments
#  -keyword arguments
#  -multiple return values
#  -list as argument
#  -lambda function

#def greek(name):
   # print("hello",name)
#greek("pesi")

#default argument

#def greek(name = "student"):
 #   print("hello",name)
#greek()

# keyword argument

#def greek(name,age):
 #   print(name,age)
#greek(age = 21,name = "pesi")


#multiple return values

#def calc(a,b):
 #   return a+b,a-b,a*b

# add,sub,mul = calc(10,20)
# print(add,sub,mul)

# list as argument

#list1 = [10,20,30]

#def calc(numbers):
 #   print(max(numbers))
#calc(list1)

#lambda function

square = lambda x: x *x

print(square(6))
