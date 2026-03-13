# 125. Valid Palindrome

**Difficulty:** Easy  
**Topic:** Strings

## Problem

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Approach

We build a new string that contains only lowercase alphanumeric characters.

For each character in the string:
- Check if the character is alphanumeric using `isalnum()`
- Convert it to lowercase
- Append it to a new string

After cleaning the string, we compare it with its reversed version.

If both strings are equal, the string is a palindrome.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(n)