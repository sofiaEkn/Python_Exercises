
# str.format() = optional method that gives users more control
#                when displaying output

number = 3.14159

print("The number pi is {:.2f}".format(number))  # The number pi is 3.14
print("The number pi is {:.3f}".format(number))  # The number pi is 3.142

number = 1000

print("The number pi is {:.3f}".format(number)) # 1000.000
print("The number pi is {:,}".format(number))  # 1,000
print("The number pi is {:b}".format(number))  # 1111101000
print("The number pi is {:o}".format(number))  # 1750
print("The number pi is {:X}".format(number))  # 3E8
print("The number pi is {:x}".format(number))  # 3e8
print("The number pi is {:E}".format(number))  # 1.000000E+03
print("The number pi is {:e}".format(number))  # 1.000000e+03