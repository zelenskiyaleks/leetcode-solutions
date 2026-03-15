class Solution:
    def func(self, root, s):
        if not root.left and not root.right:
            self.res.append(s)
            return

        if root.left:
            self.func(root.left, s + "->" + str(root.left.val))

        if root.right:
            self.func(root.right, s + "->" + str(root.right.val))

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.res = []
        s = str(root.val)
        self.func(root, s)
        return self.res