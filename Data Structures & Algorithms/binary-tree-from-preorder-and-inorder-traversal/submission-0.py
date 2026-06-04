# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        inorderMap = {val:i for i,val in enumerate(inorder)}
        def construct(pre_start,pre_end,in_start,in_end):

            if pre_start >= pre_end or in_start >= in_end:
                return None

            root_val = preorder[pre_start]
            root_node = TreeNode(root_val)

            root_index = inorderMap[root_val]
            left_size = root_index-in_start
            root_node.left = construct(pre_start+1,pre_start+1+left_size,in_start,root_index)

            root_node.right = construct(pre_start+1+left_size,pre_end,root_index+1,in_end)
            return root_node
        return construct(0, len(preorder), 0, len(inorder)) 

        





        
        
        
       