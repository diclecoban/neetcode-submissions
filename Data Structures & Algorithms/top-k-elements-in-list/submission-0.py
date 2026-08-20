class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        data = list(freq.items())
        data.sort(key = lambda x: x[1], reverse=True)

        result = []

        for i in range(k):
            result.append(data[i][0])
        
        return result
        