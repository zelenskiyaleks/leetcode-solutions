# 167. Two Sum II - Input Array Is Sorted

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

Given a **1-indexed** array of integers `numbers` that is already sorted in non-decreasing order,  
find two numbers such that they add up to a specific `target`.

Let these two numbers be `numbers[index1]` and `numbers[index2]` where 1 ≤ index1 < index2 ≤ numbers.length.

Return the indices of the two numbers, `index1` and `index2`,  
each incremented by one as an integer array `[index1, index2]`.

The tests are generated such that there is exactly one solution, and you may not use the same element twice.

## Approach

Since the array is **sorted**, we can use the **two pointers technique**.

We place one pointer at the beginning of the array and another pointer at the end.

At each step:

- Compute the sum of the two numbers
- If the sum equals the target → return the indices
- If the sum is smaller than the target → move the left pointer
- If the sum is greater than the target → move the right pointer

Because the array is sorted, adjusting the pointers guarantees
we move closer to the correct sum.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)