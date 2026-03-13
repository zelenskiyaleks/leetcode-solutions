# 88. Merge Sorted Array

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

You are given two sorted integer arrays `nums1` and `nums2`, and two integers `m` and `n`.

The first `m` elements of `nums1` are valid, and the last `n` elements are placeholders (`0`).

Merge `nums2` into `nums1` so that `nums1` becomes one sorted array.

The result must be stored inside `nums1`.

## Approach

We use two pointers starting from the end of the arrays.

Pointers:
- `i` — last valid element of `nums1`
- `j` — last element of `nums2`
- `k` — last position of `nums1`

For each step:

- Compare `nums1[i]` and `nums2[j]`
- Place the larger value at position `k`
- Move the corresponding pointer

If elements remain in `nums2`, copy them to the beginning of `nums1`.

This avoids overwriting elements in `nums1`.

## Complexity

**Time complexity:** O(m + n)  
**Space complexity:** O(1)