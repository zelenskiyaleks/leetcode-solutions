# 104. Maximum Depth of Binary Tree

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given the `root` of a binary tree, return its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

## Approach

I solved this problem using **Depth-First Search (DFS)** with recursion.

For each node, the depth of the tree is:

1 + max(depth of left subtree, depth of right subtree)

If the node is `None`, its depth is `0`.

The recursion explores the tree until it reaches the leaves
and then computes the maximum depth while returning up the call stack.

## Algorithm

1. If the node is `None` → return `0`
2. Recursively compute:
   - depth of the left subtree
   - depth of the right subtree
3. Return:

1 + max(left_depth, right_depth)

## Complexity

**Time complexity:** O(n)  
Each node is visited once.

**Space complexity:** O(h)  
Where `h` is the height of the tree due to recursion stack.