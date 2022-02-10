import os

#source = "filesInput"
destination = '/home/sk/Python_Exercises/BroCode/filesInput'
source = "testFile.txt"
destination = '/home/sk/Python_Exercises/BroCode/filesInput/testFile2.txt'

#source = "folder"
#destination = '/home/sk/Python_Exercises/BroCode/filesInput/folder'

try:
  if os.path.exists(destination):
    print("There is already a file there")
  else:
    os.replace(source,destination)
    print(source+" was moved")
except FileNotFoundError:
  print(source+" was not found")