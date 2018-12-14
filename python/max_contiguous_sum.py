from sys import maxint 

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        current_max = -maxint - 1
        running_max = 0
       
        for i in range(0, len(A)): 
            running_max = running_max + A[i] 
            if (current_max < running_max): 
                current_max = running_max 
      
            if running_max < 0: 
                running_max = 0   
                
        return current_max 
