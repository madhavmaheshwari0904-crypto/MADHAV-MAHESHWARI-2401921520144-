class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m=len(s)
        n=len(p)
        ans=[]
        sdict={}
        pdict={}
        for i in range(n):
            pdict[p[i]]=pdict.get(p[i],0)+1
            sdict[s[i]]=sdict.get(s[i],0)+1
        if(sdict==pdict):
            ans.append(0)
        for i in range(n,m):
            sdict[s[i]]=sdict.get(s[i],0)+1
            sdict[s[i-n]]-=1
            if(sdict[s[i-n]]==0):
                del sdict[s[i-n]]
            if(sdict==pdict):
                ans.append(i-n+1)
        return ans