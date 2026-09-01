# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float("-inf"), float("+inf"))

    def isValid(self, node: Optional[TreeNode], min, max):
        if not node:
            return True
        if node.val >= max or node.val <= min:
            return False

        return self.isValid(node.left, min, node.val) and self.isValid(node.right, node.val, max)
        

        


        