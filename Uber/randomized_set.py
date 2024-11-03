import random
class RandomizedSet(object):

    def __init__(self):
        self.data = set()
        self.data_list = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data:
            self.data.add(val)
            self.data_list.append(val)
            return True
        return False
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data:
            self.data.remove(val)

            # Remove from list by finding the index of val
            index = self.data_list.index(val)
            last_element = self.data_list[-1]
            
            # Move the last element to the 'index' position and pop the last element
            self.data_list[index] = last_element
            self.data_list.pop()
            
            return True
        return False   

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.data_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()