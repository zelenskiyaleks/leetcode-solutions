# 100. Same Tree

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given the roots of two binary trees `p` and `q`,
write a function to check if they are the same or not.

Two binary trees are considered the same if they are
**structurally identical** and the nodes have the **same value**.

## Approach

I compared the two trees using **Depth-First Search (DFS)** with recursion.

At each step I compared two nodes from the trees.

The trees are the same if:

1. Both nodes are `None`
2. The node values are equal
3. The left subtrees are the same
4. The right subtrees are the same

If any of these conditions fail, the trees are different.

The recursion traverses both trees simultaneously.

## Algorithm

1. If both nodes are `None` → return `True`
2. If only one node is `None` → return `False`
3. If node values differ → return `False`
4. Recursively compare:
   - left subtrees
   - right subtrees

## Complexity

**Time complexity:** O(n)  
Each node is visited once.

**Space complexity:** O(h)  
Where `h` is the height of the tree due to recursion stack.