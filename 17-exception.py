# expcetion  = an event that occurs during the execution of a program that disrupts the normal flow of instructions
#              1.try 2.except 3.finally

try:
    a = int(input("enter a number: "))
    print(1/a)
except ZeroDivisionError: 
    print('you cant divide by zero')
except ValueError:
    print('you must enter a number')

except Exception:
    print('something went wrong')

finally:
    print('this will always execute')