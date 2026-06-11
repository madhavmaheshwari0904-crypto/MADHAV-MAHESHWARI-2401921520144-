class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        c=0
        ans=""
        for i in s:
            if(i.isdigit()):
                c=c*10+int(i)
            elif(i=="["):
                stack.append((ans,c))
                ans=""
                c=0
            elif(i=="]"):
                new,n=stack.pop()
                ans=new+ans*n
            else:
                ans+=i
        return ans                    