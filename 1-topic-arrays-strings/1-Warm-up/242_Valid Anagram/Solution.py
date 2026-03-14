class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = 26 * [0]

        for i in s:
            list_s[ord(i) - ord('a')] += 1

        for i in t:
            list_s[ord(i) - ord('a')] -= 1

        return all(v == 0 for v in list_s)