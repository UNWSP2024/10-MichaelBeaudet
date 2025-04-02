# Author: Michael Beaudet
# Title: Program 2 Week 10: Car Class
# Date: 4/1/25

class Car:
    
# Initialize each variable
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0
# Increase the speed by 5
    def accelerate(self):
        self.__speed += 5
# Decrease the speed by 5  
    def brake(self):
        if self.__speed >= 5:
            self.__speed -= 5
        else:
            self.__speed = 0
# Return the current speed of the car
    def get_speed(self):
        return self.__speed
    
# Create the Car object program
my_car = Car(2023, "Bugatti Chiron")
# Accelerate 5 times
print('Accelerating:')
for _ in range(5):
    my_car.accelerate()
    print('Speed', my_car.get_speed())
# Brake 5 times
print('\nBraking:')
for _ in range(5):
    my_car.brake()
    print('Speed:', my_car.get_speed())



