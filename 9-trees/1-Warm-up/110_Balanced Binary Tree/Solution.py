class Solution:
    def func(self, root):

        if not root:
            return 0

        l = self.func(root.left)
        r = self.func(root.right)

        if abs(l - r) > 1:
            self.res = False

        return 1 + max(l, r)


    def isBalanced(self, root: Optional['TreeNode']) -> bool:

        self.res = True
        self.func(root)

        return self.res