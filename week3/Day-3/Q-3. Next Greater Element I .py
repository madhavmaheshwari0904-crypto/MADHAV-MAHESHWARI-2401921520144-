class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l=[-1]*len(nums1)
        for i in range(0,len(nums1)):
            if(nums1[i] in nums2):
                a=nums2.index(nums1[i])
                for j in range(a + 1, len(nums2)):
                    if nums2[j] > nums1[i]:
                        l[i] = nums2[j]
                        break     
            else:
                l[i]=-1
        return l                