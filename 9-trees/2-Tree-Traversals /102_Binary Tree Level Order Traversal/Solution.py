class Solution:

    def levelOrder(self, root: Optional['TreeNode']) -> List[List[int]]:

        res = []
        queue = []

        if not root:
            return []

        queue.append([root, 0])

        while queue:
            node, level = queue.pop(0)

            if len(res) == level:
                res.append([node.val])
            else:
                res[level].append(node.val)

            if node.left:
                queue.append([node.left, level + 1])
            if node.right:
                queue.append([node.right, level + 1])

        return res