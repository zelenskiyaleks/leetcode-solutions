# 345. Reverse Vowels of a String

**Difficulty:** Easy  
**Topic:** Two Pointers, String

## Problem

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a', 'e', 'i', 'o', 'u'` (both lower and upper cases).

## Approach

- Use two pointers (`i`, `j`)
- Move from both ends toward the center
- Swap characters only if both are vowels
- Skip non-vowel characters
- Convert string to list (since strings are immutable in Python)

Time complexity: **O(n)**  
Space complexity: **O(n)** (due to list conversion)