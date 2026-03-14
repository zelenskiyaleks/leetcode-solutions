# 349. Intersection of Two Arrays

**Difficulty:** Easy  
**Topic:** Arrays

## Problem

Given two integer arrays `nums1` and `nums2`, return an array of their intersection.

Each element in the result must be **unique**, and you may return the result in any order.

## Approach

I use Python sets.

First, I convert both arrays into sets to remove duplicates.

Then I compute the intersection of the two sets using the `&` operator.

Finally, I convert the result back into a list.

## Complexity

**Time complexity:** O(n + m)  
**Space complexity:** O(n + m)