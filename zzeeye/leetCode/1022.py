# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        answer = 0
        if root :
            if root.left :
                root.left.val += (root.val*10)
                answer += self.sumRootToLeaf(root.left)
            if root.right :
                root.right.val += (root.val*10)
                answer += self.sumRootToLeaf(root.right)

            if root.left is None and root.right is None :
                answer += int(str(root.val), 2)
            
        
        return answer