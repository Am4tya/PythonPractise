def printNto1(n):

    #base case
    if n == 0:
        return

    # print(n)
    # recursive case
    printNto1(n-1)
    print(n) 

n = int(input("Enter N: "))
printNto1(n)