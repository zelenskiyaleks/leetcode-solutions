# 350. Intersection of Two Arrays II

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

Given two integer arrays `nums1` and `nums2`, return an array of their intersection.

Each element in the result must appear as many times as it shows in both arrays,
and you may return the result in any order.

## Approach

First I sorted both arrays.

Then I used the **two pointers technique** to iterate through the arrays.

Two pointers `i` and `j` traverse `nums1` and `nums2`:

- If `nums1[i] == nums2[j]`, the element belongs to the intersection.  
  I added it to the result and moved both pointers.
- If `nums1[i] < nums2[j]`, I moved pointer `i`.
- Otherwise, I moved pointer `j`.

This technique works because the arrays I sorted before.

## Complexity

**Time complexity:** O(n log n + m log m)  
**Space complexity:** O(1)