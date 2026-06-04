class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ APPROACH 1
        ans=[i*i for i in nums]
        ans.sort()
        return ans"""
        return sorted(i**2 for i in nums)