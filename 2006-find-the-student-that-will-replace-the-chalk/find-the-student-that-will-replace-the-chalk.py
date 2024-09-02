class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        index = 0
        for x in range(len(chalk)):
            if chalk[x]>k:
                return x
            else:
                k -= chalk[x]