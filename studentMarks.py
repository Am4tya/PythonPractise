marks = float(input("Enter the Marks:"))

# if marks are between 81 and 100
if marks > 80:
    print("The marks is very Good")

# if marks are between 61 and 80
elif marks > 60:
    print("The marks is Good")

# if marks are between 41 and 60
elif marks > 40:
    print("The marks is Average")

# if marks are less than or equal to 40
else:
    print("Fail")
