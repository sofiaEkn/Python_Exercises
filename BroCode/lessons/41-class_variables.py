from car import Car

car_1 = Car("Chevy","Corvette","2021","blue")
car_2 = Car("Ford","Mustang","2022","red")

#print(car_1.wheels) #4
#print(car_2.wheels) #4

#car_1.wheels = 2

#print(car_1.wheels) #2
#print(car_2.wheels) #4

#print(Car.wheels)

Car.wheels = 2

print(car_1.wheels) #2
print(car_2.wheels) #2