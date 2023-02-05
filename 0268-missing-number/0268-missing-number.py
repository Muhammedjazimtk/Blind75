class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=0
        s=sum(nums)
        for i in range(len(nums)+1):
            n+=i
        return n-s

        