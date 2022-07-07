n = int(input("Enter how many numbers you want in a series:"))
first = 0
second = 1
for i in range(n):
    print(first, end=" , ")
    temp = first
    first = second
    second = temp + second