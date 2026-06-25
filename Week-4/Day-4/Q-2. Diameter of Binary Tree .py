class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        m=[0]
        def height(root):
            if(root==None):
                return 0
            l=height(root.left)
            r=height(root.right)
            m[0]=max(m[0],l+r)
            return max(l,r)+1
        height(root)
        return m[0]     
        