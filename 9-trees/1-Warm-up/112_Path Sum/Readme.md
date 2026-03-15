# 112. Path Sum

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given the `root` of a binary tree and an integer `targetSum`,
return `true` if the tree has a **root-to-leaf path** such that
adding up all the values along the path equals `targetSum`.

A **leaf** is a node with no children.

## Approach

I solved this problem using **Depth-First Search (DFS)**.

During traversal I subtracted the current node value from `targetSum`.
When we reach a leaf node, we check whether the remaining sum equals zero.

If such a path exists, we mark the result as `True`.

To avoid unnecessary work, the recursion stops early once a valid path is found.

## Algorithm

1. If the current node is `None` → stop recursion
2. Subtract the current node value from `targetSum`
3. If the node is a leaf:
   - check whether `targetSum == 0`
4. Recursively traverse:
   - left subtree
   - right subtree

## Complexity

**Time complexity:** O(n)  
Each node is visited at most once.

**Space complexity:** O(h)  
Where `h` is the height of the tree due to recursion stack.