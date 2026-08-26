# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.right, subRoot) or self.isSubtree(root.left, subRoot)
    

    def isSameTree(self, one: Optional[TreeNode], two: Optional[TreeNode]):
        if not one and not two:
            return True
        if not one or not two:
            return False
        if one.val != two.val:
            return False
        
        return self.isSameTree(one.right, two.right) and self.isSameTree(one.left, two.left)



        
        