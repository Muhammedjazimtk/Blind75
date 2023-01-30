class Solution:
    def hammingWeight(self, n: int) -> int:
        c=bin(n)
        f=0
        d=c[2:]
        for i in d:
            if i=='1':
                f+=1
        return f
        