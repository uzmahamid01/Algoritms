class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        hashmap = {}
        for i in range(len(words)):
            if words[i] in hashmap:
                hashmap[words[i]] += 1
            else:
                hashmap[words[i]] = 1

        print(hashmap)
        sorted_hashmap = sorted(hashmap.keys(), key=lambda x: (-hashmap[x], x))
        
        return sorted_hashmap[:k]

        