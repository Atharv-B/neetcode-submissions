# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # for a binary tree
        # 2 * i + 1 represents a left node
        # 2 * i + 2 represents a right node
        if not root:
            return 0
        # depth = 0
        max_l = self.maxDepth(root.left)
        max_r = self.maxDepth(root.right)
        depth = max(max_l, max_r)
        return 1+depth



        