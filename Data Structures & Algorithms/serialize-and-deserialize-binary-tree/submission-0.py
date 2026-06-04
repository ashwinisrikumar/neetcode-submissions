# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(res)
        """
        COUGH
        COUGH

        class Test:
            a: int
            b: str

        t = Test(a = 1, b = 'hello')
        serialie this data -> json.dumps(t)
        rqeuest.post(t)

        deeralize -> JSON -> json.loads(Test, t) -> class test

        1,2,NULL,NULL,3,4,NULL,NULL,5,NULL,NULL
        
        def dfs(root):
            if root is None
                res.append("N")
                return
            
            res.append(root.val)
            res.append(dfs(root.left))
            res.append(dfs(root.right))

            ",".join([1,2, N, N, 3, 4, N, N, 5, N, N])
        """


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals=data.split(",")
        self.i=0
        def dfs():
            if vals[self.i]=='N':
                self.i=self.i+1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i+=1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

        

        """
        split(",") -> list
        hello world
        hello#world

        def dfs(root):

            if al == 'N':
                i+=1
                return None
            node TreeNode(root.val)
            node.left = dfs(root.left)
            node.right = dfs(root.right)
        
            i += 1

        """