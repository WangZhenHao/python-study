import os
import json
def file_detection():
    file_path = './status/text.txt'

    if os.path.exists(file_path):
        print('File exists')
    else:
        print('File does not exist')

# file_detection()


def write_file():
    employee = ['John', 'Doe', 'Male']
    employee2 = {
        'name': 'John',
        'age': 20,
        'gender': 'Male'
    }
    text = 'This is a test1'
    file_path = './status/output.txt'
    file_path2 = './status/output.json'

    with open(file = file_path2, mode = 'w') as file:
        json.dump(employee2, file, indent=4)

        # for item in employee:
        #     file.write(item + '\n')

        # file.write(text)
        print('File written')

# write_file()

def read_file():
    file_path = './status/output.txt';
    with open(file_path, mode = 'r') as file:
        contnet = file.read()
        print(contnet)

read_file()