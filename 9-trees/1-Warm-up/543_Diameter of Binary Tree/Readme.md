# 543. Diameter of Binary Tree

**Difficulty:** Easy  
**Topic:** Trees / DFS

## Problem

Given the `root` of a binary tree, return the **length of the diameter** of the tree.

The **diameter** of a binary tree is the length of the longest path between any two nodes in the tree.  
This path may or may not pass through the root.

The length of the path is measured by the **number of edges** between nodes.

---

## Approach

I used **Depth-First Search (DFS)**.

For each node we compute the **height of its left and right subtrees**.

The diameter passing through the current node is:

```
left_height + right_height
```

While performing DFS we update the maximum diameter found so far.

The recursive function returns the **height of the subtree**:

```
1 + max(left_height, right_height)
```

This allows us to compute both the height and the diameter during a single traversal.

---

## Algorithm

1. Traverse the tree using DFS
2. For each node compute:
   - height of the left subtree
   - height of the right subtree
3. Update the diameter:

```
diameter = max(diameter, left_height + right_height)
```

4. Return the height of the current node:

```
1 + max(left_height, right_height)
```

---

## Complexity

**Time complexity:** `O(n)`  
Each node is visited once.

**Space complexity:** `O(h)`  
Where `h` is the height of the tree due to recursion stack.