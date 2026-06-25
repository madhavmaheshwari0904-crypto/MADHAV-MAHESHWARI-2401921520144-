class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        m=[root.val]
        def solve(root):
            if root==None:
                return 0
            l=max(solve(root.left),0)
            r=max(solve(root.right),0)
            m[0]=max(m[0],root.val+l+r)
            return max(root.val+max(l,r),0)
        solve(root)
        return m[0]        