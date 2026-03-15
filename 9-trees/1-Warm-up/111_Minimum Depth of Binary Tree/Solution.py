class Solution:

    def minDepth(self, root: Optional['TreeNode']) -> int:

        if not root:
            return 0

        left_d = self.minDepth(root.left)
        right_d = self.minDepth(root.right)

        if left_d == 0 or right_d == 0:
            current_depth = max(left_d, right_d) + 1
        else:
            current_depth = min(left_d, right_d) + 1

        return current_depth