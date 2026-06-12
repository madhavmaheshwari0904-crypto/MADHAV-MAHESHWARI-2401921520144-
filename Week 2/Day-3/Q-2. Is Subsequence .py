class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        for i in s:
            c=t.find(i)
            if(c ==-1):
                return False
            else:    
                t=t[c+1:]    
        return True        