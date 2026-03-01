# 75. Sort Colors

**Difficulty:** Medium  
**Topic:** Arrays, Two Pointers, Sorting

## Problem
Sort an array containing only 0, 1, and 2 in-place without using the built-in sort.

## Approach:

- Used three pointers (low - boundary for 0, high - boundary for 2, i - current pointer)
- If 0 → swap with `low`
- If 1 → move forward
- If 2 → swap with `high`

## Complexity

**Time complexity:** O(n)
**Space complexity:** O(1)