class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def pal(a,i,j):
            if(i>=j):
                return True
            if(a[i]==a[j]):
                return pal(a,i+1,j-1)
            return False        
        n=len(s)
        m=0
        sp=0
        for i in range(n):
            for j in range(i,n):
                if(j-i+1)>m:
                    if(pal(s,i,j)==True):
                        m=j-i+1
                        sp=i
        return s[sp:sp+m]            