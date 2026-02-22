# 18. 4Sum

**Difficulty:** Medium  
**Topic:** Arrays, Two Pointers, Sorting

## Problem

Given an array nums of n integers, return all unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

- 0 <= a, b, c, d < n
- a, b, c, and d are distinct
- nums[a] + nums[b] + nums[c] + nums[d] == target

## Approach:

- Sort the array
- Fix two elements
- Use two pointers for the remaining part
- Skip duplicates at every level

## Complexity

**Time complexity:** O(n³)
**Space complexity:** O(1)