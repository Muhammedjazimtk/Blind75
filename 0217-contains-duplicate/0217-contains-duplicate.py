class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ## return true if value exists 2x +
        ## return false if value exists 1 time only
        hashset = set()
        for n in nums:
            if n in hashset: 
                return True 
            hashset.add(n)
        return False