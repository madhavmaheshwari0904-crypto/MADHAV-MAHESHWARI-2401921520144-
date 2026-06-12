class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m=0
        ans=""
        for i in s:
            if(i not in ans):
                ans+=i
            else:
                ans=ans[ans.index(i)+1:]+i
            m=max(m,len(ans))
        return m            