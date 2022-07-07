def insertion_sort(my_list):
    for index in range(1, len(my_list)):
        current_element = my_list[index]
        pos = index
        while current_element < my_list[pos-1] and pos > 0: #Checking current element with element at a given position
            my_list[pos] = my_list[pos-1]
            pos = pos-1

        my_list[pos] = current_element

list1 = [2, 4, 3, 7, 5]
insertion_sort(list1)
print(list1)
