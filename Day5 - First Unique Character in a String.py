class Solution:
    def firstUniqChar(self, s: str) -> int:
        #li=list(str)
        c=0
        for v in s:
            
            if(s.count(v)==1):
                return c
            c+=1
            
        return -1    
        