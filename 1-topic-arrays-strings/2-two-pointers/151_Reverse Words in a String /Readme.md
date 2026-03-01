# 151. Reverse Words in a String

**Difficulty:** Medium  
**Topic:** Strings, Two Pointers

## Problem
Given a string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters.  
The result should not contain leading, trailing, or multiple spaces between words.

## Approach:

- Iterate through the string character by character
- Build each word manually
- When a space is encountered:
- Push the word into a list (if not empty)
- After the loop, push the last word (if exists)
- Reverse the list and join with a single space

This avoids using `split()` and manually parses the string.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(n)