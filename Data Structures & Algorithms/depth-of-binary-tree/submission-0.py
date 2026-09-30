# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        cnt1 = 1
        cnt2 = 1 

        if root.left:
            cnt1 += self.maxDepth(root.left)
        if root.right:
            cnt2 += self.maxDepth(root.right)
        return max(cnt1,cnt2)