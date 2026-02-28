# 31. Next Permutation

**Difficulty:** Medium  
**Topic:** Arrays, Two Pointers, Sorting

## Problem
Implement next lexicographical permutation in-place.

If no next permutation exists (array is in descending order), rearrange it into the lowest possible order.

## Approach

1. Traverse from right to left to find the first decreasing element (pivot).
2. Find the smallest number greater than pivot on the right side.
3. Swap them.
4. Reverse the suffix.

## Complexity
**Time complexity:** O(n)
**Space complexity:** O(1)