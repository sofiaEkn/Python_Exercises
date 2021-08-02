import time
# for loop = a statement that will execute it's block of code
#            a limited amount of times
#
#            while loop = unlimited
#            for loop = limited

for i in range(10):
  print(i+1)         # start print from 0 to 9, so i+1 to start from 1 to 10

for i in range (50,100+1,2):
  print(i)

for i in "Bro Code":
  print(i)

for seconds in range(10,0,-1):
  print(seconds)
  time.sleep(1)
print("Happy New Year!")
