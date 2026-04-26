# for number in range(3):
#     # print(number)
#     print('Attempting to log in', number, (number + 1) * '.')

# for number in range(1, 10, 2):
#     print('Attempting', number, number * '.')


successful = True

for number in range(3):
    print('Attempt')
    if successful:
        print('Welcome')
        break
else:
      print('Incorrect credentials')
