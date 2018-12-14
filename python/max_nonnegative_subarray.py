from sys import maxint

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        current_max = -maxint - 1
        running_sum = 0
        running_start = 0
        running_length = 0
        max_start = 0
        max_length = 0
       
        for i in range(0, len(A)): 
            if A[i] < 0:
                running_sum = 0
                running_start += 1
                running_length = 0
            else:
                if running_length == 0:
                    running_start = i
                running_length += 1
                running_sum = running_sum + A[i] 
                
            if current_max < running_sum: 
                current_max = running_sum 
                max_start = running_start
                max_length = running_length
            elif current_max == running_sum:
                if running_length > max_length:
                    max_start = running_start
                    max_length = running_length
      
            if running_sum < 0: 
                running_sum = 0   
                
        return A[max_start:max_start+max_length] 
