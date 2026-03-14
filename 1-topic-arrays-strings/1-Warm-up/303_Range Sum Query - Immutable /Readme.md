# 303. Range Sum Query - Immutable

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

Given an integer array `nums`, handle multiple queries of the following type:

Calculate the sum of the elements of `nums` between indices `left` and `right` inclusive.

Implement the `NumArray` class:

- `NumArray(int[] nums)` initializes the object with the integer array `nums`
- `int sumRange(int left, int right)` returns the sum of the elements of `nums`
  between indices `left` and `right` inclusive

## Approach

We use the **prefix sum** technique.

During initialization we compute a prefix sum array where:

prefix[i] = nums[0] + nums[1] + ... + nums[i]

This allows us to answer each query in constant time.

To compute the sum of the range `[left, right]`:

- If `left > 0`:
  
  sum = prefix[right] - prefix[left - 1]

- Otherwise:

  sum = prefix[right]

## Complexity

**Time complexity:**

Initialization: O(n)  
Query: O(1)

**Space complexity:** O(n)