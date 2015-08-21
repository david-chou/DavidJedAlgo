#takes array of integers and sorts in increasing order

def insertionsort(input_array):
    n = len(input_array)
    #sorts the array in place
    for i in range(1,n):
        key = input_array[i]
        j = i -1
        #compare current key to the sorted subarray to the left of key
        while (j >= 0 and input_array[j] > key):
            input_array[j+1] = input_array[j]
            j -= 1
        input_array[j+1] = key
    return input_array

print insertionsort([1,3,4,5,2,6,7,8,1,2,13])
print insertionsort([1,2,3,4,5])
print insertionsort([5,4,3,2,1])
