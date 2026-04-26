age = 22

message = "Eligible" if age >= 18 else "Not Eligible"

print(message)


# logincal operator: and or not 
high_income = True
good_credit = False
student = False

# if high_income or good_credit:
if not student and (high_income or good_credit):
    print("Eligible")
else:
    print("Not Eligible")


# chain compiserator 

age = 22

if age >= 18 and age <= 65:
    print("age >= 18 and age <= 65:Eligible")

if 18 <= age < 65:
    print(" 8 <= age < 65: Eligible")


print("bag" > "cat")