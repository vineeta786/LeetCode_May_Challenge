class Solution:
    def findComplement(self, num: int) -> int:
        binary=[]
        while(num>0):
            binary.append(num%2)
            num = num//2
        n=len(binary)
        for i in range(n):
            if(binary[i]==0):
                binary[i] = 1 
            elif(binary[i]==1):
                binary[i] = 0

        #binary.reverse()
        final_number = 0
        
        for v in range(n):
            final_number = final_number + binary[v]*(math.pow(2,v))

        return int(final_number)   
        