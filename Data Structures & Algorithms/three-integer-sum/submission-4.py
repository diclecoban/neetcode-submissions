class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()

        if len(nums) < 3:
            return []
        
        nums.sort()

        for i,num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            seen = set()
            rest1 = 0 - num
            for j in range(i + 1, len(nums)):
                othernum = nums[j]
                rest2 = rest1 - othernum
                if(rest2 in seen):
                    triplet = [num, othernum, rest2]
                    result.add(tuple(sorted(triplet)))
                seen.add(othernum)

        return [list(triple) for triple in result]