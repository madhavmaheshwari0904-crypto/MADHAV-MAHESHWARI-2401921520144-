class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gen(s,l,r,ans=[]):
            if l: gen(s+'(',l-1,r)
            if r>l:gen(s+')',l,r-1)
            if not r:
                ans.append(s)
            return ans
        return gen('',n,n)