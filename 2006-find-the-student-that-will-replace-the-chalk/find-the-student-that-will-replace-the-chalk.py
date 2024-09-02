class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        k = k % sum(chalk)
        index = 0
        while(k>0):
            k-=chalk[index]
            if(k<0):
                index-=1
            index+=1
            if len(chalk)==index:
                index = 0
        return index