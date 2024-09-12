class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        set_allowed = set(allowed)
        ans = 0
        for word in words:
            word_allowed = True
            for letter in word:
                if letter not in set_allowed:
                    word_allowed = False
            if word_allowed:
                ans+=1
        return ans