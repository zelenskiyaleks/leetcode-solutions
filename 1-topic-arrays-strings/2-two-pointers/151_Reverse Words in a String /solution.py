class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        current = ""

        for ch in s:
            if ch != " ":
                current += ch
            else:
                if current != "":
                    words.append(current)
                    current = ""

        if current != "":
            words.append(current)

        return " ".join(words[::-1])