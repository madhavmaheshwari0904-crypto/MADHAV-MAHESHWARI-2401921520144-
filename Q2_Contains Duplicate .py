class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s=len(nums)
        s1=len(set(nums))
        if(s1!=s):
            return True
        return False            