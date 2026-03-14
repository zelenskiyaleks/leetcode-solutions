# 268. Missing Number

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

Given an array `nums` containing `n` distinct numbers in the range `[0, n]`,
return the only number in the range that is missing from the array.

## Approach

The sum of numbers from `0` to `n` can be computed using the formula:

n * (n + 1) / 2

We calculate the expected sum of the range `[0, n]`
and subtract every element in the array.

The remaining value is the missing number.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)