# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        
        if root :
            if root.val in range(low, high+1) :
                answer += root.val

            answer += (self.rangeSumBST(root.left, low, high)+self.rangeSumBST(root.right, low, high))
        
        return answer