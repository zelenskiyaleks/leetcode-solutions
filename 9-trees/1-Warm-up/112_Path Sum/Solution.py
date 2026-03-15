class Solution:

    def func(self, root, targetSum):

        if not root or self.res:
            return

        targetSum -= root.val

        if not root.left and not root.right:
            if targetSum == 0:
                self.res = True
            return

        self.func(root.left, targetSum)
        self.func(root.right, targetSum)


    def hasPathSum(self, root: Optional['TreeNode'], targetSum: int) -> bool:

        self.res = False
        self.func(root, targetSum)

        return self.res