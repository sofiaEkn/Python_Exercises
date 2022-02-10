
# str.format() = optional method that gives users more control
#                when displaying output

name = "Bro"

print("Hello, my name is {}".format(name))
print("Hello, my name is {:10}. Nice to meet you".format(name)) # tiene 10 espacios en blanco despues del "name". Hello, my name is Bro.          Nice to meet you.
print("Hello, my name is {:<10}. Nice to meet you".format(name))  # left alined
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # Hello, my name is          Bro. Nice to meet you. (right alined)
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # Hello, my name is     Bro     . Nice to meet you. (centre alined)