class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        bins,bing = bin(start)[2:],bin(goal)[2:]
        slen = len(bins)
        glen = len(bing)
        bins,bing = ("".join(["0" for i in range(glen-slen)])+bins) , ("".join(["0" for i in range(slen-glen)])+bing)
        # print(bins,bing)
        count = 0
        for i in range(len(bins)):
            if bins[i] != bing[i]:
                count+=1
        
        return count