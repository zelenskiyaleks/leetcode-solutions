# 26. Remove Duplicates from Sorted Array

**Difficulty:** Easy  
**Topic:** Arrays, Two Pointers

## Problem

Given an integer array `nums` sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.

Return the number of unique elements `k`.

The first `k` elements of `nums` should contain the unique elements in sorted order.

## Approach

We use the **Two Pointers** technique.

- `k` tracks the position of the last unique element
- Iterate through the array
- When a new value is found:
  - move pointer `k`
  - overwrite position `k`

This keeps the array modified in-place.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)