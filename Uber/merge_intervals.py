class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        #edge case 
        if not intervals:
            return []
        
        #sort the array intervals by start time
        sorted_intervals = sorted(intervals, key=lambda i: i[0])
        print(sorted_intervals)

        merged = []

        
        for i in sorted_intervals:
            if merged and i[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], i[1])

            else:
                merged.append(i)
        return merged


        