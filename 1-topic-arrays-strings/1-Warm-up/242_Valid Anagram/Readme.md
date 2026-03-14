# 242. Valid Anagram

**Difficulty:** Easy  
**Topic:** Strings

## Problem

Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`,
and `false` otherwise.

An anagram is a word or phrase formed by rearranging the letters of another word.

## Approach

Two strings are anagrams if they contain the same characters
with the same frequencies.

Since the strings contain only lowercase English letters,
we can use a frequency array of size 26.

We iterate through string `s` and increase the counter
for each character.

Then we iterate through string `t` and decrease the counter
for each character.

If the strings are anagrams, all counters will become zero.

Finally, we check that all values in the array are equal to zero.

## Complexity

**Time complexity:** O(n)  
**Space complexity:** O(1)