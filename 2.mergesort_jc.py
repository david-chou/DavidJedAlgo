_author_ = "jed"

import random

#Below we implement mergesort, a divide-and-conquer method to sort an array
def MergeSort(input_array):
    array_length = len(input_array)
    current_min_index = 0 
    current_max_index = array_length-1
    sorted_array= [0] * array_length

    while 


    return sorted_array

#Maybe instead should do unit testing. 
test_array1 = [1,2,3,4,5]
test_array2 = [5,4,3,2,1]
test_array3 = [2,1,5,3,4]
test_array4 = [1,5,1,2,4]

print test_array1, MergeSort(test_array1)
print test_array2, MergeSort(test_array2)
print test_array3, MergeSort(test_array3)
print test_array4, MergeSort(test_array4)
