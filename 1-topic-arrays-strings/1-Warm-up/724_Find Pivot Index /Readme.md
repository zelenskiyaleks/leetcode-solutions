# 724. Find Pivot Index

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

Given an array of integers `nums`, calculate the **pivot index** of this array.

The pivot index is the index where the sum of all the numbers strictly to the left
of the index is equal to the sum of all the numbers strictly to the right of the index.

If the index is on the left edge of the array, then the left sum is `0`.
This also applies to the right edge of the array.

Return the **leftmost pivot index**. If no such index exists, return `-1`.

## Approach

We maintain two running sums:

- `sum_l` — sum of elements to the left of the current index
- `sum_r` — sum of elements to the right of the current index

Initially:

- `sum_l = 0`
- `sum_r = sum(nums[1:])`

Then we iterate through the array and update both sums:

- Move the current element from the right side to the left side
- Compare `sum_l` and `sum_r`

If they are equal, we found the pivot index.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)