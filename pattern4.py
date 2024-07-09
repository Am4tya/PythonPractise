n = int(input("Enter n: "))

for i in range(1, n + 1):  # loop for rows
    for j in range(65, 65 + i):  # loop for columns (65 corresponds to ASCII 'A')
        print(chr(j), end="")
    print()
