# 80. Remove Duplicates from Sorted Array II

**Difficulty:** Medium  
**Topic:** Arrays, Two Pointers

## Problem
Given a sorted array `nums`, remove duplicates in-place such that each unique element appears at most twice.

Return `k` — the number of valid elements after modification.  
The first `k` elements of `nums` should contain the final result.

## Approach:

- Use two pointers:
  - `i` → iterates through the array
  - `k` → write pointer (length of valid prefix)
- The first two elements are always valid
- Starting from index 2:
  - Compare current element with `nums[k-2]`
  - If equal → skip (would create third duplicate)
  - If different → write to position `k` and increment `k`

This guarantees each element appears at most twice.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)