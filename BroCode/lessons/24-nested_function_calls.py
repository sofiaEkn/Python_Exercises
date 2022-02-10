# nested functions calls = function calls inside other function calls
#                          innermost function calls are resolved first
#                          returned value is used as argument for the next outer function

# num = input("Enter a whole positive number: ") input: -3.14
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)         print: 3

print(round(abs(float(input("Enter a whole positive number: ")))))
