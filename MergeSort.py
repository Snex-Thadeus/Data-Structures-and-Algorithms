def mergesort(list1): #complexity of O(nlogn)
    if len(list1) > 1:
        mid = len(list1)//2
        left_sublist = list1[:mid] #From beginning till mid
        right_sublist = list1[mid:]
        mergesort(left_sublist)
        mergesort(right_sublist)
        i = 0 #Left_sublist
        j = 0 #right_sublist
        k = 0 #list1
        while i < len(left_sublist) and j < len(right_sublist): #For merging
            if left_sublist[i] < right_sublist[j]:
                list1[k] = left_sublist[i]
                i = i+1
                k = k+1
            else:
                list1[k] = right_sublist[j]
                j = j+1
                k = k+1
        while i < len(left_sublist): #Checks if any values are left out
            list1[k] = left_sublist[i]
            i = i + 1
            k = k + 1

        while j < len(right_sublist):
            list1[k] = right_sublist[j]
            j = j + 1
            k = k + 1


num = int(input("How many elements do you want in list?"))
list1 = [int(input()) for x in range(num)]
mergesort(list1)
print("Sorted list is:", list1)
