
try:
  #with open('/home/sk/Python_Exercises/BroCode/filesInput/test.txt') as file:
  with open('testFile.txt') as file:  # in the same path as a 32-read_file.py
    print(file.read())
except FileNotFoundError:
  print("That file was not found :(")

#print(file.closed)