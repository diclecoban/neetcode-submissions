class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) < 3:
            return []
        elif len(nums) == 3:
            if(nums[0] + nums[1] + nums[2] == 0):
                result.append(nums)
                return result
        
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
                    triple = [num,othernum,rest2]
                    if(triple not in result):
                        result.append([num,othernum,rest2])
                seen.add(othernum)

        return result