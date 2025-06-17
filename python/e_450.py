# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        elif key > root.val:
            # I don't think you need to specifiy the right or the left node what it becomes
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            #Found the node
            #Return either left or right if the other is empty
            # Single Child to Node
            if (root.left == None):
                return root.right
            if (root.right == None):
                return root.left

            #Two Children to Node
            t = root
            root = self.min(t.right)
            root.right = self.deleteMin(t.right)
            root.left = t.left

        return root

    def min(self, x):
        print(x.val)
        if x.left is None:
            return x
        return self.min(x.left)

    def deleteMin(self, root):
        return self.__deleteMin(root)

    def __deleteMin(self, x):
        if x.left == None:
            return x.right
        x.left = self.__deleteMin(x.left)
        return x
        # Should recursively go left and return the ndoe to the left
        

        