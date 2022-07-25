# list1 = [10, 15, 4, 23, 0] # O(n^2) time complexity O(1) space complexity
list1 = []
num = int(input("How many numbers do you want to enter:"))
print("Enter Values:")
for k in range(num):
    list1.append(int(input()))
print("Unsorted List:", list1)

for j in range(len(list1)-1):
    swapped =False
    for i in range(len(list1)-1-j): #Ignore the last 2 elements which are already sorted
        if list1[i] > list1[i+1]: #Ascending order
            list1[i], list1[i+1] = list1[i+1], list1[i]
            swapped = True

        else:
            print(list1)
    if not swapped:
        break
    print()

print("Sorted List:", list1)
