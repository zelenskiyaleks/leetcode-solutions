# 11. Container With Most Water

**Difficulty:** Medium  
**Topic:** Arrays, Two Pointers

## Problem

Given an integer array height of length n, find two lines that together with the x-axis form a container such that the container contains the most water.

Return the maximum amount of water a container can store.

## Approach

- Use two pointers (left and right)
- Compute area at each step
- Move the pointer with smaller height
- Keep track of maximum area

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)