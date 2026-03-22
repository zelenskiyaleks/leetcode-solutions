# 103. Binary Tree Zigzag Level Order Traversal

**Difficulty:** Medium  
**Topic:** Trees / BFS

## Problem

Given the `root` of a binary tree, return the zigzag level order traversal
of its nodes' values (i.e., from left to right, then right to left for the next level).

## Approach

I solved this problem using **Breadth-First Search (BFS)**.

I traverse the tree level by level using a queue.
For each level, I alternate the order in which values are added:

- left → right
- right → left

I use a boolean flag `left_to_right` to control the direction.

## Algorithm

1. If the root is `None` → return empty list
2. Initialize a queue with the root node
3. While the queue is not empty:
   - iterate over all nodes in the current level
   - if direction is left-to-right → append values
   - otherwise → insert values at the beginning
   - push children to the queue
4. Toggle direction after each level

## Complexity

**Time complexity:** O(n)  
Each node is visited once.

**Space complexity:** O(n)  
The queue stores nodes level by level.