class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        required = total - sum(rolls)
        if required > 6 * n or required < n:
            return []
        
        ans = [required // n] * n
        remain = required - sum(ans)
        
        for i in range(n):
            if remain > 0:
                add = min(6 - ans[i], remain)
                ans[i] += add
                remain -= add
        
        return ans
