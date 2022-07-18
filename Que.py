#Using list as a queue

wmt_stock_price_queue = []
wmt_stock_price_queue.insert(0, 131.10)
wmt_stock_price_queue.insert(0, 132.12)
wmt_stock_price_queue.insert(0, 135)


print(wmt_stock_price_queue)

#Using collections.deque as a queue
from collections import deque

q = deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(10)

print(q)


#Implement queue class using collections.deque
import threading
import time

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

food_order_queue = Queue()

def place_orders(orders):
    for order in orders:
        print("Placing order for:",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = food_order_queue.dequeue()
        print("Now serving: ",order)
        time.sleep(2)


if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()


pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

pq.dequeue()

print(pq)