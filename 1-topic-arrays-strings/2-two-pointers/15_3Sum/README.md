# 15. 3Sum

**Difficulty:** Medium  
**Topic:** Arrays, Two Pointers, Sorting

## Problem

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, j != k, and nums[i] + nums[j] + nums[k] == 0.

The solution set must not contain duplicate triplets.

## Approach

- Sort the array
- Fix first element
- Use two pointers
- Skip duplicates

**Time complexity:** O(n²)  
**Space complexity:** O(1) (excluding output)