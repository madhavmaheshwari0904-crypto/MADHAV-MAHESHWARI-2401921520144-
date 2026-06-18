class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        a=0
        s=[-1]
        for i in range(len(heights)):
            while(heights[i]<heights[s[-1]]):
                h=heights[s.pop()]
                w=i-s[-1]-1
                a=max(a,h*w) 
            s.append(i) 
            #print(s)
        heights.pop()
        return a          
        