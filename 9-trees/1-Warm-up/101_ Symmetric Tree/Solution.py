class Solution:

    def func(self, l, r):

        if not l and not r:
            return True

        if not l or not r:
            return False

        if l.val != r.val:
            return False

        return (
            self.func(l.left, r.right) and
            self.func(l.right, r.left)
        )


    def isSymmetric(self, root: Optional['TreeNode']) -> bool:

        return self.func(root.left, root.right)