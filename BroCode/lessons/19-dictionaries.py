# dictionary = A changeable, unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'USA':'Washington DC',
            'India':'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}

#print(capitals['Russia'])
#print(capitals.get('Japan')) print 'None' because not in the diccionary

#print(capitals.keys()) print: dict_keys(['USA', 'India', 'China', 'Russia'])
#print(capitals.values()) print: dict_values(['Washington DC', 'New Dehli', 'Beijing', 'Moscow'])
#print(capitals.items())  print: dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

for key,value in capitals.items():
  print(key,value)

#capitals.update({'Germany':'Berlin'})
#capitals.update({'USA':'Las Vegas'})
#capitals.pop('China')
#capitals.clear()

#print(capitals['Germany'])
#print(capitals.get('Germany'))  return 'None' when doesn't exist in diccionary
#print(capitals)