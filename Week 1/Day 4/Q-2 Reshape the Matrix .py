class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m=len(mat)
        n=len(mat[0])
        if(m*n!=r*c):
            return mat
        ans=[[0]*c for _ in range(r)]
        no=0
        for i in range(m):
            for j in range(n):
                ans[no//c][no%c]=mat[i][j]
                no+=1    
        return ans        