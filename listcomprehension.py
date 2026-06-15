
# list comprehension is a short way to create a list
# it uses one line instead of a loop
# it makes code short and easy to read
# we can also add conditions inside it.

#nums = []

#for i in range(1,6):
 #   nums.append(i)
#print(nums)


#nums = [i for i in range(1,11)]
#print(nums)


#even number


nums = []

#for i in range(1,6):
  #  if i % 2 == 0:
 #       nums.append(i)
#print(nums)


#odd number

#nums = []

#for i in range(1,6):
 #   if i % 2 !=0:
  #      nums.append(i)
#print(nums)


#nums = [i for i in range(1,11) if i % 2 == 0]
#print(nums)

nums = [i for i in range(1,11) if i%2 !=0]
print(nums)
