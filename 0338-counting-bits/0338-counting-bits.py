class Solution:
    def countBits(self, n: int) -> List[int]:
#         res=[]
#         for i in range(n+1):
#             c=bin(i)
#             d=c[2:]
#             m=0
        
#             for j in d:
#                 if j=='1':
#                     m+=1
#             print(i)
#             res.append(m)
            
#         return res
        res=[0]*(n+1)
        offset=1
        for i in range(1,n+1):
            if i== offset* 2:
                offset=i
                
            res[i] = 1+ res[i-offset]
            
        return res