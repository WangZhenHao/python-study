
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



# Inheritance = Allows a class to inherit attributes and methods from another class 
#               Helps with code reusability and extensibility 
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} is sleeping')

class Dog(Animal):
    def bark(self):
        print(f'{self.name} is barking')

class Cat(Animal):
    def meow(self):
        print(f'{self.name} is meowing')

dog = Dog('Buddy')
cat = Cat('Fluffy')

# dog.bark()
# cat.meow()


# mulitple inheritance = inheritance from more than one parent class
#                         class Child(Parent1, Parent2) 

# muiltilevel inheritance = inheritance from a parent class which inherits from another parent class
#                            C(B) <- B(A) <- A