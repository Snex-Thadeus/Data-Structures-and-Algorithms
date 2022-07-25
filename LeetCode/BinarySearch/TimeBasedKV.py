#Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

#LeetCode 981

class TimeMap(object):

    def __init__(self):
        self.store = {} #key=string, value=[list of [value, timestamp]]

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])


    def get(self, key, timestamp):
        res = ""
        values = self.store.get(key, [])

        #Binary Search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0] #Closest value so far
                l = m + 1
            else:
                r = m - 1

        return res
