# index operator [] = gives access to a sequence's element (str,list,tuples)

name = "bro Code!"
#name = "bro Code!"

if(name[0].islower()):
  name = name.capitalize()
print(name)

first_name = name[:3].upper() #print: BRO
last_name = name[4:].lower()  #print: code!
last_character = name[-1]     #print: !

print(first_name)
print(last_name)
print(last_character)