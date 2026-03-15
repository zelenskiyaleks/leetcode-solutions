# 226. Invert Binary Tree

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given the `root` of a binary tree, invert the tree and return its root.

Inverting a binary tree means swapping the left and right children
of every node in the tree.

## Approach

I used **Depth-First Search (DFS)** with recursion.

For each node I swap its left and right children:
    node.left, node.right = node.right, node.left

After the swap we recursively apply the same operation to the left
and right subtrees.

## Algorithm

1. If the node is `None` → return `None`
2. Swap `left` and `right` children
3. Recursively invert:
   - left subtree
   - right subtree
4. Return the root

## Complexity

**Time complexity:** O(n)  
Each node is visited once.

**Space complexity:** O(h)  
Where `h` is the height of the tree due to recursion stack.