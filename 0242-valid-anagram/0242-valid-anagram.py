class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss=list(s)
        ts=list(t)
        ss.sort()
        ts.sort()
        if ss==ts:
            return True
        else:
            return False
        