# slicing = create a substring by extracting elements from another string
#           indexing[] or slicing()
#           [start:stop:step]

name = "Bro Code"

first_name = name[:3]        # [0:3]
last_name = name[4:]         # [4:end]
funky_name = name[0:8:2]
funky_name2 = name[::3]      # [0:end:3]
reversed_name = name[::-1]   # [0:end:-1]

#print(first_name)  # Bro
#print(last_name)   # Code
#print(funky_name)  # BoCd - each 2nd character
#print(funky_name2)  # B d - each 3rd character
#print(reversed_name) # edoC orB

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])
