# Note: Variables do not need to be declared with any particular type in Python.

# String
name = "Amatya"
print(type(name))

# Integer
roll_number = 37
print(type(roll_number))

# Floating Number
percentage = 95.8
print(type(percentage))

# Boolean
is_student = True
print(type(is_student))

print(name, roll_number, percentage, is_student)

print("My name is "+ name + " and my roll number is", roll_number)
print("I scored", percentage, "% in my final exams. I am a student is", is_student)

# percentage = 94.5

# print(name, roll_number, percentage, is_student)

# print expressions
print("My percentage has changed to", percentage - 5.0)

#print with seperator
print(name, roll_number, percentage, is_student, sep="-")

x = 1
y = 2
z = 3
print(x,y,z,sep="-->")