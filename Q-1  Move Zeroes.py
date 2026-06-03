class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        c=0
        for i in nums:
            if(i!=0):
                nums[c]=i
                c+=1
        while(c<n):
            nums[c]=0
            c+=1           