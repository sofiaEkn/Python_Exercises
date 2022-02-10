
#text = "Yooooooo\nThis is some text\nHave a good one!\n"
text = "Have a nice day! See ya\n"  # sobreescribe texto anterior

#with open('testFile.txt','r') as file:
with open('testFile.txt','a') as file:  #para no sobreescribir texto
#with open('testFile.txt','w') as file:
  file.write(text)