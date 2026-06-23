# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes_count = 0
        q=collections.deque()
        q.append((root,root.val)) #(node,max_so_far)
        while q:
            node,max_so_far = q.popleft()
            if node.val>=max_so_far:
                good_nodes_count +=1
                max_so_far = node.val
            if node.left:
                q.append((node.left,max_so_far))
            if node.right:
                q.append((node.right,max_so_far))
        return good_nodes_count

        