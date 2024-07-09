# Write a function that print hello world

# def amatya():
#     # body of function
#     print("Hello world!")


# amatya()


# function which takes 2 numbers as input and returns their sum
def add(n1 = 0, n2 = 0):  #n1 and n2 are parameter
    print("n1:", n1)
    print("n2:", n2)
    sum = n1 + n2
    return sum

# Positional Argument
# print("The sum is", add(2,3))

# keyword argument (named arguments)
# print("The sum is", add(n2 = 2, n1 = 3))

# Default Arguments
# print("The sum is", add())

# Arbitary Arguments
def addAllNumbers(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
    
# output = addAllNumbers(1,2,3,4,5)
# print("The sum is", output)

def studentInfo(**kwords):
    for x,y in kwords.items():
        print(x,"is",y)

studentInfo(name="Sahil", age=19, city="Pokhara")
studentInfo(name="Elliot", age=22, city="New York")
