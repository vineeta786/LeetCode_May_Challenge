class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        jc = list(J)
        sc = list(S)
        
        cj=0
        
        for jw in jc:
            cj=cj+sc.count(jw)
        return cj    
            
        