class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        flag=0
        if(ransomNote in magazine):
            return True
            #print(True)
            flag = 0

        else:
            s = [0 for v in range(123)]
            ma = [0 for v in range(123)]

            for l in ransomNote :
                if(s[ord(l)]==0):
                    s[ord(l)] = ransomNote.count(l)
                   # print(l+" "+str(s[ord(l)]))
            #print(s[97:123])        


            for lj in magazine :
                if(ma[ord(lj)]==0):
                    ma[ord(lj)] = magazine.count(lj) 
                    #print(lj+" "+str(ma[ord(lj)]))
            #print(ma[97:123])        


            for v in range(97,123):
                if(s[v]!=0):
                    if(ma[v]>=s[v]):
                        flag=0
                    elif(ma[v]!=s[v]):
                        #return False
                        flag=1
                        break


            if(flag==1):
                return False
                #print(False)
            else:
                return True
                #print(True)

