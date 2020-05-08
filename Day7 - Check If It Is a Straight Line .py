class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)==2:
            return True
        else:
            x1=(coordinates[1][1]-coordinates[0][1])
            y1=(coordinates[1][0]-coordinates[0][0])
            if(y1==0):
                m = 0
            else:    
                m = x1/y1
            y=coordinates[1][1]
            x=coordinates[1][0]
            c=y-(m*x)
            flag = 0
            n = len(coordinates)
            for v in range(n):
                    x = coordinates[v][0]
                    y = coordinates[v][1]       
                    if (y!= (m*x)+c):
                        flag = 1
                        break
                    
            if(flag==0):
                return True
            else:
                return False
                
                       
                    
                          
                        
                           
                           
                           
                           
            
        