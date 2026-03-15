class Solution:
    
    def func(self, root):
        if not root:
            return
        self.func(root.left)
        self.res.append(root.val)
        self.func(root.right)
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.func(root)
        return self.res