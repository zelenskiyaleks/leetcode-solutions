# 53. Maximum Subarray

**Difficulty:** Medium  
**Topic:** Arrays, Dynamic Programming, Prefix Sum

## Problem

Given an integer array `nums`, find the contiguous subarray 
(with at least one number) which has the largest sum and return its sum.

## Approach

use **Kadane's Algorithm**.

At each position:
- Extend previous subarray
- Or start a new subarray
- cur = max(cur + nums[i], nums[i])
- maintain a global maximum during iteration.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)