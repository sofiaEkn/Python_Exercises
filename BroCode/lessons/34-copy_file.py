# copyfile() = copies contents of a file
# copy() =     copyfile() + permission mode + destination can be a directory
# copy2() =    copy() + copies metadata (file's creation and modification times)

import shutil

#shutil.copyfile('testFile.txt','copy.txt') #src(source), dst(destination)
shutil.copyfile('testFile.txt','/home/sk/Python_Exercises/BroCode/filesInput/copy.txt') #src(source), dst(destination)
#shutil.copyfile('/home/sk/Python_Exercises/BroCode/filesInput/testFile.txt','/home/sk/Python_Exercises/BroCode/filesInput/copy.txt') if the destiny is different
#shutil.copy('testFile.txt','copy.txt') #src(source), dst(destination) # the same arguments
#shutil.copy2('testFile.txt','copy.txt') #src(source), dst(destination) # the same arguments