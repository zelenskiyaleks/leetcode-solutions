class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        i, j = 0, len(s) - 1
        vowels = "AaEeIiOoUu"

        while i < j:
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            elif s[i] in vowels and s[j] not in vowels:
                while i <= j and s[j] not in vowels:
                    j -= 1
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            elif s[j] in vowels and s[i] not in vowels:
                while i <= j and s[i] not in vowels:
                    i += 1
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

            else:
                i += 1
                j -= 1

        return "".join(s)