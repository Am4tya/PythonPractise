eng_marks = int(input("Enter marks of English: "))
math_marks = int(input("Enter marks of Math: "))

# if both are more than 80, print A Grade
if eng_marks > 80 and math_marks > 80:
    print("A Grade")

# if either of marks are more than 80, print B Grade 
elif eng_marks > 80 or math_marks > 80:
    print("B Grade")

# if neither of marks are more than 80
else:
    print("C Grade")