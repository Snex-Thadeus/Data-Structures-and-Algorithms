import heapq

heap = []
heapq.heappush(heap, 10) #Insert into the heap
heapq.heappush(heap, 50)
heapq.heappush(heap, 21)
heapq.heappush(heap, 5)
# heapq.heappop(heap) #Returns the smallest value and deletes it from the heap
heapq.heapify(heap) # Convert the given list to Binary heap
# heapq.heappushpop(heap, 58) #Removes the smallest and add the item
heapq.heapreplace(heap, 33) #Pops the least item then adds the given item
print(heapq.nsmallest(2, heap))
print(heapq.nlargest(3, heap))
print(heap)

list1 = [(1, "Ria"), (4, "sia"), (3, "gia")] #Smallest value, highest priority
heapq.heapify(list1)
print(list1)
for i in range(len(list1)):
    print(heapq.heappop(list1))