n1 = int(input("Enter number1: "))
n2 = int(input("Enter number2: "))
n3 = int(input("Enter number3: "))

# using Nested if else statement
# comparing n1 and n2

if n1 > n2:
    # either n1 and n2 is greatest
    if n1 > n3:
        print(n1, "is the greatest element")
    else:
        print(n3, "is the greatest element")
else:
    # either n2 and n3 is greatest
    if n2 > n3:
        print(n2, "is the greatest element")
    else:
        print(n3, "is the greatest element")