# 110. Balanced Binary Tree

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given a binary tree, determine if it is height-balanced.

A binary tree is considered height-balanced if for every node
the difference between the heights of the left and right subtrees
is no more than 1.

## Approach

I solved the problem using **Depth-First Search (DFS)**.

For each node we compute:

height = 1 + max(height of left subtree, height of right subtree)

At the same time I checked whether the tree is balanced:

|left_height - right_height| ≤ 1

If any node violates this condition, the tree is not balanced.

To avoid recomputing heights multiple times,
I calculated heights during the DFS traversal.

## Algorithm

1. Recursively compute the height of the left subtree.
2. Recursively compute the height of the right subtree.
3. Check if the difference in heights is greater than 1.
4. If so, mark the tree as unbalanced.
5. Return the height of the current node.

## Complexity

**Time complexity:** O(n)  
Each node is visited once.

**Space complexity:** O(h)  
Where `h` is the height of the tree due to recursion stack.