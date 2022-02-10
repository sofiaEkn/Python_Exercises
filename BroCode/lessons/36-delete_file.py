import os
import shutil

path = "copyTestFile2.txt"  # if stay in the same path
#path = "empty_folder"
#path = '/home/sk/Python_Exercises/BroCode/filesInput/copyTestFile2.txt' if exists in the other path

try:
  os.remove(path) #delete a file
  #os.rmdir(path) #delete a file or empty folder
  #shutil.rmtree(path) #delete files and/or folders, very careful with this function
except FileNotFoundError:
  print("That file was not found")
except PermissionError:
  print("You do not have permission to delete that")
#except OSError:
  #print("You cannot delete that using that function")
except OSError:
  print("That folder contains files")
else:
  print(path+" was deleted")