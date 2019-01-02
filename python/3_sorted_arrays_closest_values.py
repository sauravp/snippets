# https://www.interviewbit.com/problems/array-3-pointers/

import sys

class Solution:
  # @param A : tuple of integers
  # @param B : tuple of integers
  # @param C : tuple of integers
  # @return an integer
  def minimize(self, A, B, C):
    current_min_gap = sys.maxsize
    for i in range(len(A)):
        other1 = self.binary_search(B, A[i])
        other2 = self.binary_search(C, A[i])
        metric = max(abs(A[i] - other1), abs(A[i] - other2), abs(other1 - other2))
        if metric < current_min_gap:
                  current_min_gap = metric

     for i in range(len(B)):
        other1 = self.binary_search(A, B[i])
        other2 = self.binary_search(C, B[i])
        metric = max(abs(B[i] - other1), abs(B[i] - other2), abs(other1 - other2))
        if metric < current_min_gap:
                current_min_gap = metric

     for i in range(len(C)):
        other1 = self.binary_search(B, C[i])
        other2 = self.binary_search(A, C[i])
        metric = max(abs(C[i] - other1), abs(C[i] - other2), abs(other1 - other2))
        if metric < current_min_gap:
                current_min_gap = metric

     return current_min_gap
        
  # binary search for closest value
  def binary_search(self, arr, elem):
      # edge case - last or above all
      if elem >= arr[len(arr)-1]:
          return arr[len(arr)-1]
      # edge case - first or below all
      if elem <= arr[0]:
          return arr[0]

      start, end = 0, len(arr)-1
      while start <= end :
          mid = (start + end) // 2
          # we found exact value
          if arr[mid] == elem :
              return arr[mid]
          # go on right side
          elif arr[mid] < elem :
              start = mid + 1
          # go on left side
          else :
              end = mid - 1

      # elem not found, return the closest
      if elem < arr[mid]:
          return self.find_closest(arr[mid - 1], arr[mid], elem)
      else:
          return self.find_closest(arr[mid], arr[mid + 1], elem)

  def find_closest(self, val1, val2, target):
      if (abs(target - val1) >= abs(val2 - target)):
          return val2
      else:
          return val1
