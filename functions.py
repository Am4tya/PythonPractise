# Writing a function for calculating sum from 1 to n
def sumOneToN(n):
    sum = 0
    for i in range(1, n+1):
        sum += i

    return sum

n = int(input("Enter the number till you wnt to count: "))
# Call function
output = sumOneToN(n)
print("Sum of all numbers till ",n," is", output)

# Again using function
n1 = int(input("Enter n: "))
output1 = sumOneToN(n1)
print("Sum of all numbers till ",n," is", output1)

