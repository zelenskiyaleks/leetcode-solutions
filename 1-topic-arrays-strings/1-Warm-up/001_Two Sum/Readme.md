# 1. Two Sum

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

Given an array of integers `nums` and an integer `target`,
return indices of the two numbers such that they add up to `target`.

You may assume that each input has exactly one solution,
and you may not use the same element twice.

## Approach

We use a hash map to store:

value → index

For each number:
- Compute complement = target - current
- Check if complement exists in dictionary
- If yes → return indices

This allows solving the problem in one pass.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(n)