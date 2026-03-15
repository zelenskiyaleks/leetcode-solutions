# 257. Binary Tree Paths

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given the `root` of a binary tree, return all **root-to-leaf paths** in any order.

A **leaf** is a node with no children.

Each path should be represented as a string in the form:
node1->node2->node3
where the path starts at the root and ends at a leaf.

## Approach

I used **Depth-First Search (DFS)** with recursion.

During traversal I keep a string `path` that stores the current path
from the root to the current node.

When I reach a **leaf node** (a node with no left and right children),
the current path represents a complete root-to-leaf path and is added
to the result list.

When moving to the next node we create a **new path string** by adding:
"->" + node value
This prevents modifying the path used in other branches of recursion.

---

## Algorithm

1. Start DFS from the root with the initial path equal to `root.val`
2. If the node is a **leaf** → add the current path to the result
3. If the node has a left child → continue DFS with updated path
4. If the node has a right child → continue DFS with updated path
5. Return the list of collected paths

---

## Complexity

**Time complexity:** `O(n)`  
Each node is visited once.

**Space complexity:** `O(h)`  
Where `h` is the height of the tree due to recursion stack.