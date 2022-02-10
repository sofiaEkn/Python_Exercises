# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

#def add(*args):
#  sum = 0
#  for i in args:
#    sum +=1
#  return sum

#print(add(1,2,3,4,5,6))   print: 21

def add(*stuff):
  sum = 0
  stuff = list(stuff)  # convert stuff to list, to access element of stuff
  stuff[0] = 0
  for i in stuff:
    sum +=1
  return sum


print(add(1,2,3,4,5,6))  #print: 20