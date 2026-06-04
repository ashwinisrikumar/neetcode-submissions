# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return
        root.left,root.right = root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

        """
        left
        right
        swap -> node

        swap
        left
        right

        a,b = b,a -> swapping two numbers without using temp var
        temp = b
        b = a
        a = temp

        node.left, node.right = node.right, node.left
        node.left -> recursive
        node.right -> recursive

        """





        