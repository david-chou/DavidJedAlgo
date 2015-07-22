
def merge(A,B): #function to merge two sorted arrays
  i = 0
  j = 0
  C=[0]*(len(l_array)+len(r_array))
  for x in range(0,len(A)+len(B)):
    if A[i] <= B[j]:
      C[x] = A[i]
      i++
    else:
      C[x] = B[j]
      j++

def divide(self,input_array,min_index,max_index):
  if len(input_array) == 1:
    return input_array
  else:
    m=len(input_array)/2
    l_array=[
    
