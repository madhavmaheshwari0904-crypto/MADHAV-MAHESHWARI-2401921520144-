class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        """ l=len(temperatures)
        n=[]
        for i in range(0,l):
            c=0
            for j in range(i+1,l):
                if(temperatures[i]<temperatures[j]):
                    c=c+1
                    n.append(c)
                    break
                else:
                    c=c+1 
                    continue   
            else:
                n.append(0)        
        return n"""
        s=[]
        r=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while s and temperatures[i]>temperatures[s[-1]]:
                ind=s.pop()
                r[ind]=i-ind
            s.append(i)
        return r       
        