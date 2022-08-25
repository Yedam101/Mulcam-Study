"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        answer = []
        if root :
            answer = [root.val]
            for child in root.children :
                answer.extend(self.preorder(child))
            
        
        return answer