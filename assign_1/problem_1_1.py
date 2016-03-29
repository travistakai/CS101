#import packages
import numpy as np

#test array
#arr = np.array([10,21,24,45,2,5,13])

#insertion 
def insertion(A):
   size = A.size
   swap = 0;index = 0
   for i in range(1, size):
      index = i
      while A[index] < A[index-1] and index > 0:
         swap = A[index-1]
         A[index-1] = A[index]
         A[index] = swap
         index-=1


#mergeSort
def mergeSort(A, p, r): 
      if(p < r):
         #recursivley breaks apart the array
         q = int((p+r)/2)
         mergeSort(A, p, q)
         mergeSort(A, q+1, r)
         merge(A, p, q, r)

#merges the array back together
def merge(A, p, q, r):
   n1 = q-p+1
   n2 = r-q
   L = np.zeros(n1)
   R = np.zeros(n2)
   i = 0
   j = 0
   k = 0
   while i < n1:
      L[i] = A[p+i]
      i = i + 1
   while j < n2:
      R[j] = A[q+j+1]
      j = j + 1
   i = 0
   j = 0
   k = p
   while k <= r:
      if( i<n1 and j<n2 ):
         if( L[i]<=R[j] ):
            A[k] = L[i]
            i = i + 1
         else:
            A[k] = R[j]
            j = j + 1
      elif( i<n1 ):
         A[k] = L[i]
         i = i + 1
      else:
         A[k] = R[j]
         j = j + 1
      k = k + 1
