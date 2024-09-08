class Solution:
    def convertDateToBinary(self, date: str) -> str:
        words = date.split('-')
        ans = []
        for word in words:
            inti = int(word)
            ans.append(bin(inti)[2:])
        print(ans)
        return "-".join(ans)