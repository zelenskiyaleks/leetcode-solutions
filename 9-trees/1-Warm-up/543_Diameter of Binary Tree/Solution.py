class Solution:
    def func(self, root):
        if not root:
            return 0

        left = self.func(root.left)
        right = self.func(root.right)

        self.res = max(self.res, left + right)

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.func(root)
        return self.res