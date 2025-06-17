# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from queue import Queue
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue = []
        result = []

        queue.append(root)
        while len(queue) > 0:
            count =  len(queue)
            currLevel = []
            for i in range(count):
                node = queue.pop(0) # Need to specify its popping from the beginning of the list
                currLevel.append(node.val)

                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)
                    
            result.append(currLevel)
        return result