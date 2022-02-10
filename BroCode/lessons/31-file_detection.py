import os

#path = "C:\\Users\\Cakow\\Desktop\\test.txt"
path = "/home/sk/Python_Exercises/BroCode/filesInput/test.txt"

if os.path.exists(path):
  print("That location exists!")
  if os.path.isfile(path):
    print("That is a file")
  elif os.path.isdir(path):
    print("That is a directory!")
else:
  print("That location doesn't exist!")