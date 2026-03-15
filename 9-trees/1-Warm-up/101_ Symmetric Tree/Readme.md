# 101. Symmetric Tree

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given the `root` of a binary tree, check whether it is a mirror of itself  
(i.e., symmetric around its center).

A tree is symmetric if the left subtree is a mirror reflection of the right subtree.

## Approach

We solve this problem using **Depth-First Search (DFS)** with recursion.

Two nodes are mirrors of each other if:

1. Both nodes are `None`
2. Their values are equal
3. The **left child of the first node** equals the **right child of the second node**
4. The **right child of the first node** equals the **left child of the second node**

The recursion compares the left and right subtrees simultaneously.

## Algorithm

1. If both nodes are `None` → return `True`
2. If only one node is `None` → return `False`
3. If node values differ → return `False`
4. Recursively compare:
   - `l.left` with `r.right`
   - `l.right` with `r.left`

## Complexity

**Time complexity:** O(n)  
Each node is visited once.

**Space complexity:** O(h)  
Where `h` is the height of the tree due to recursion stack.