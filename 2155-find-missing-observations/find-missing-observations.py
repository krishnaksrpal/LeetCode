class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = mean * (m + n)
        required = total - sum(rolls)
        if required > 6 * n or required < n:
            return []
        
        quotient = required // n
        remainder = required % n
        return [quotient + (1 if i < remainder else 0) for i in range(n)]
        
