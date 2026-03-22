# 102. Binary Tree Level Order Traversal

**Difficulty:** Medium  
**Topic:** Trees / BFS

## Problem

Given the `root` of a binary tree, return the level order traversal
of its nodes' values (i.e., from left to right, level by level).

## Approach

I solved this problem using **Breadth-First Search (BFS)**.

I use a queue to traverse the tree level by level.
Each element in the queue stores:
- the current node
- its level (depth)

While traversing:
- if I reach a new level → I create a new list
- otherwise → I append to the existing level

## Algorithm

1. If the root is `None` → return empty list
2. Initialize a queue with `(root, level=0)`
3. While the queue is not empty:
   - pop the first element
   - if current level does not exist → create it
   - append node value to the corresponding level
   - push children with level + 1

## Complexity

**Time complexity:** O(n)  
Each node is visited once.

**Space complexity:** O(n)  
The queue can contain up to one full level of nodes.