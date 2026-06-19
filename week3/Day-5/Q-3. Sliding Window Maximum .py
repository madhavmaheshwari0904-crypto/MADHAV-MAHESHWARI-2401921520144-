class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        q=deque()
        ans=[]
        i=0
        for j in range(len(nums)):
            while( q and nums[q[-1]]<nums[j]):
                q.pop()
            q.append(j)
            if(j-i+1)==k:
                ans.append(nums[q[0]])
                if(q[0]==i):
                    q.popleft()
                i+=1
        return ans                