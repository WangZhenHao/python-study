
# class variables  = shared among all instances of a class 
#                    defined outside of __init__ 
#                    allow you to share data among all objects created from the class

class Car:

    wheels = 4
    miles = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        self.miles += 10
        print(f'you driving the {self.model}')

    def stop(self):
        print(f'you stopped the {self.model}')

    def describe(self):
        print(f'This car is a {self.year} {self.make} {self.model}')
    
    

car1 = Car('Honda', 'Civic', 2015)
car2 = Car('Toyota', 'Corolla', 2016)

# print(Car.wheels)
# car1.drive()