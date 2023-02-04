class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        for i in range(n+1):
            c=bin(i)
            d=c[2:]
            m=0
        
            for j in d:
                if j=='1':
                    m+=1
            print(i)
            res.append(m)
            
        return res
        