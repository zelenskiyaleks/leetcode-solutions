# 189. Rotate Array

**Difficulty:** Medium  
**Topic:** Arrays

## Problem

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

You must modify the array in-place.

### Example 1

Input: nums = [1,2,3,4,5,6,7], k = 3  
Output: [5,6,7,1,2,3,4]

### Example 2

Input: nums = [-1,-100,3,99], k = 2  
Output: [3,99,-1,-100]

---

## Approach 1 — In-place Reversal

- Reverse the entire array
- Reverse first `k` elements
- Reverse the remaining `n-k` elements

This achieves rotation in-place.

**Time complexity:** O(n)  
**Space complexity:** O(1)

---

## Approach 2 — Python Slicing

- Normalize `k`
- Rebuild array using slicing

This is more Pythonic but uses extra memory.

**Time complexity:** O(n)  
**Space complexity:** O(n)