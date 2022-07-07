import random
# To get the correct position of the pivot element
# left <= right, a[left] <= pivot, a[right] >= pivot


def pivot_place(list1, first, last):
    rindex = random.randint(first, last)
    list1[rindex], list1[last] = list1[last], list1[rindex]
    pivot = list1[first]
    left = first+1
    right = last
    while True:
        while left <= right and list1[left] <= pivot:
            left = left+1 #Increment left
        while left <= right and list1[right] >= pivot:
            right = right-1 #Move to the right
        if right < left:
            break
        else:
            list1[left], list1[right] = list1[right], list1[left]
    list1[first], list1[right] = list1[right], list1[first]  # Swapping
    return right


def quicksort(list1, first, last):
    if first < last: #Excepting the single element
        p = pivot_place(list1, first, last)
        quicksort(list1, first, p-1)
        quicksort(list1, p+1, last)


list1 = [56,26, 93, 17, 31, 44]
n = len(list1)
quicksort(list1, 0, n-1)
print(list1)
