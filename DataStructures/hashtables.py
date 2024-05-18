#using hashtable
class MyHashMap(object):
    def __init__(self):
        self.capacity = 1000001
        self.hashmap = [[] for _ in range(self.capacity)]

    def hash(self, key):
        return key % self.capacity

    def put(self, key, value):
        index = self.hash(key)
        for i in range(len(self.hashmap[index])):
            if self.hashmap[index][i][0] == key:
                self.hashmap[index][i] = (key, value)
                return
        self.hashmap[index].append((key,value))

    def get(self, key):
        index = self.hash(key)
        for k, v in self.hashmap[index]:
            if k == key:
                return v
        return -1

    def remove(self, key):
        index = self.hash(key)
        for i in range(len(self.hashmap[index])):
            if self.hashmap[index][i][0] == key:
                self.hashmap[index].pop(i)
                return
        

#using array
# class MyHashMap(object):
#     def __init__(self):
#         self.data = [None]*100000001

#     def put(self, key, value):
#         self.data[key] =value

#     def get(self, key):
#         val = self.data[key]
#         print(val)
#         if val == None:
#             print("inside",val)
#             return -1
#         else: 
#             return val

#     def remove(self, key):
#         self.data[key] = None
        


# class MyHashMap(object):
#     def __init__(self):
#         self.hashmap = []

#     def put(self, key, value):
#         for i in range(len(self.hashmap)):
#             if self.hashmap[i][0] == key:
#                 self.hashmap[i] = (key, value)
#                 return
#         self.hashmap.append((key,value))

#     def get(self, key):
#         for k, v in self.hashmap:
#             if k == key:
#                 return v
#         return -1

#     def remove(self, key):
#         for i in range(len(self.hashmap)):
#             if self.hashmap[i][0] == key:
#                 self.hashmap.pop(i)
#                 return






# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)