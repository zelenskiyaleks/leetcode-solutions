# 27. Remove Element

**Difficulty:** Easy  
**Topic:** Arrays, Two Pointers

## Problem

Given an integer array `nums` and an integer `val`,
remove all occurrences of `val` in-place.

Return the number of elements in `nums` which are not equal to `val`.

The order of elements may be changed.
The first `k` elements of `nums` should contain valid values.

## Approach

We use a two-pointer technique:

- `k` tracks the position for the next valid element
- Iterate through the array
- Copy elements not equal to `val` to the front

This modifies the array in-place.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)