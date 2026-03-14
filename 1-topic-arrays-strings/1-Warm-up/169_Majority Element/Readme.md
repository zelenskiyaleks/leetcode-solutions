# 169. Majority Element

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than `n / 2` times.

You may assume that the majority element always exists in the array.

## Approach

For each number in the array:

- If the counter is zero, choose the current number as the new candidate
- If the number equals the candidate, increase the counter
- Otherwise, decrease the counter

Because the majority element appears more than `n / 2` times,
it cannot be completely cancelled out by other elements.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)