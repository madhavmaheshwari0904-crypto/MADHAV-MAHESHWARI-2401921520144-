class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #print(s[1:])
        #print(s[:-1])
        return s in s[1:]+s[:-1]