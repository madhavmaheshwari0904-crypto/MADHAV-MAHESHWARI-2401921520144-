class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        # APPROCH 1
        """ans=[]
        for i in range(len(mat)):
            for j in range(len(mat)):
                if(i==j and mat[i][j] ):
                    ans.append(mat[i][j])
                elif(i+j+1==len(mat)):
                    ans.append(mat[i][j])
        return sum(ans)"""
        #APPROCH 2
        ans=0
        n=len(mat)
        for i in range(n):
            ans+=mat[i][i]
            if(i!=n-1-i):
                ans+=mat[i][n-i-1]
        return ans                       
