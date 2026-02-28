# 392. Is Subsequence

**Difficulty:** Easy  
**Topic:** Two Pointers, String  

## Problem

Given two strings `s` and `t`, return `true` if `s` is a subsequence of `t`, or `false` otherwise.

A subsequence is formed by deleting some characters (possibly none) without changing the relative order of the remaining characters.

---

## Example 1

Input:
s = "abc", t = "ahbgdc"

Output:
true

## Example 2

Input:
s = "axc", t = "ahbgdc"

Output:
false

---

## Approach (Reverse Scan)

- Convert `s` to a list to allow `pop()`
- Iterate over `t` in reverse
- When characters match → remove last character from `s`
- If `s` becomes empty → subsequence found

Time complexity: **O(n)**  
Space complexity: **O(n)**  

Where `n = len(t)`.

Note: Space is O(n) because we convert `s` into a list.