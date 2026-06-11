class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split(" ")
        new=[]
        for i in l:
            new.append(i[-1::-1])
        return " ".join(new)    