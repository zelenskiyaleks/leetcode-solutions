# 111. Minimum Depth of Binary Tree

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path
from the root node down to the nearest leaf node.

A **leaf** is a node with no children.

## Approach

I solved the problem using **Depth-First Search (DFS)**.

For each node I recursively computed the depth of the left and right
subtrees.

A special case occurs when one of the children is missing.  
If one subtree is empty, the minimum depth must be calculated
using the depth of the existing subtree.

## Algorithm

1. If the current node is `None` → return `0`
2. Recursively compute:
   - `left_depth`
   - `right_depth`
3. If one subtree is missing:
   - return `1 + max(left_depth, right_depth)`
4. Otherwise:
   - return `1 + min(left_depth, right_depth)`

## Complexity

**Time complexity:** O(n)  
Each node is visited once.

**Space complexity:** O(h)  
Where `h` is the height of the tree due to recursion stack.