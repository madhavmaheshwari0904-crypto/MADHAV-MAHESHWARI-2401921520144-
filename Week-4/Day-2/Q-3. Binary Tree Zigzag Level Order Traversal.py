# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        if not root:
            return []
        q=deque([root])
        f=True
        while q:
            n=len(q)
            values=[0]*n
            for i in range(n):
                node=q.popleft()
                if(node.left):
                    q.append(node.left)
                if(node.right):
                    q.append(node.right)
                if f:
                    values[i]=node.val
                else:
                    values[n-i-1]=node.val
            f=not f
            ans.append(values)
        return ans                        