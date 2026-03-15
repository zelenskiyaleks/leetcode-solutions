# 94. Binary Tree Inorder Traversal

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given the `root` of a binary tree, return the **inorder traversal** of its nodes' values.

Inorder traversal visits nodes in the following order:

```
left → root → right
```

## Approach

I used **Depth-First Search (DFS)** with recursion.

In inorder traversal we process nodes in the following order:

1. Traverse the left subtree
2. Visit the current node
3. Traverse the right subtree

During traversal we append the node values to the result list.

---

## Algorithm

1. If the node is `None` → return
2. Recursively traverse the left subtree
3. Add the current node value to the result list
4. Recursively traverse the right subtree

---

## Complexity

**Time complexity:** `O(n)`  
Each node is visited once.

**Space complexity:** `O(h)`  
Where `h` is the height of the tree due to recursion stack.