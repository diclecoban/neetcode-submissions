class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     # O(n^2) solution
        # i = 0
        # j = 1
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if(nums[i] == nums[j]):
        #             return True
        # return False

    # O(n) example using set
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        

        