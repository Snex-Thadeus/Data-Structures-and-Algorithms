# list1 = [56, 5, 3, 2, 78, 6, 0]
#
# for i in range(len(list1)-1):
#     min_val = min(list1[i:]) #max to arrange in descending order
#     min_index = list1.index(min_val, i) #I mention the start
#     if list1[i] != list1[min_index]: #No need of swapping i elements are in the same position
#         list1[i], list1[min_index] = list1[min_index], list1[i] #Swapping the 2 numbers
#
# print(list1)

print()
num = int(input("How many numbers do you want to enter:"))
list1 = [int(input("Enter Number:")) for x in range(num)]
for i in range(len(list1)-1): #O(n^2)
    min_val = list1[i]
    for j in range(i+1, len(list1)):
        if list1[j] < min_val:
            min_val = list1[j]
    min_index = list1.index(min_val, i) #I mention the start
    if list1[i] != list1[min_index]: #No need of swapping i elements are in the same position
        list1[i], list1[min_index] = list1[min_index], list1[i] #Swapping the 2 numbers

print(list1)