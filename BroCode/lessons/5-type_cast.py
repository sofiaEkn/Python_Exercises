# type casting = convert the data type of a value to another data type.

x = 1    #int
y = 2.0  #float
z = "3"  #str

#y = int(y)
#z = int(z)

#x = float(x)  # print(x) -> 1.0
#y = float(y)  # print(y) -> 2.0
#z = float(z)  # print(z) -> 3.0

#x = str(x)  # print(x) -> 1
#y = str(y)  # print(y) -> 2.0
#z = str(z)  # print(z) -> 3

print("X is "+str(x))       # print("X is "+x) give error, because x isn't str
print("Y is "+str(y))       # print("Y is "+y) give error, because y isn't str
print(z*3)

#X is 1
#Y is 2.0
#333

#print(x)
#print(y)
#print(z) # 3
#print(int(y)) # 2
#print(z*3)  # 333 if z = "3"
#print(z*3)    # 9 if z = int(z), 9.0 if z = float(z)
