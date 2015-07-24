_author_ = "jed"

class MergeSort:
    #merge two sorted arrays
    def merge(self,input_array,min_index,mid_index,max_index):
        array_len = max_index - min_index + 1
        aux = [0]*(array_len)
        #copy input array to auxiliary array 
        for i in range(0, array_len):
            aux[i] = input_array[min_index+i]
            i = 0
            j = mid_index - min_index
            #merge the two sorted arrays
            for x in range(min_index,max_index+1):
                if aux[i] <= aux[j]:
                    input_array[x] = aux[i]
                    i+=1
                else:
                    input_array[x] = aux[j]
                    j+=1
        return input_array
    #sort input_array[min_index..max_index]
    def sort(self,input_array,min_index,max_index):
        if (max_index <= min_index):
            return
        mid_index = min_index + (max_index - min_index)/2
        self.sort(input_array,min_index,mid_index)
        self.sort(input_array,mid_index+1,max_index)
        self.merge(input_array,min_index,mid_index,max_index)

#tests (maybe instead should do unit testing). 
sorting_hat = MergeSort()
test_array1 = [1,2,3,4,5]
test_array2 = [5,4,3,2,1]
test_array3 = [2,1,5,3,4]
test_array4 = [1,5,1,2,4]

print test_array1, sorting_hat.sort(test_array1,0,4)
print test_array2, sorting_hat.sort(test_array2,0,4)
print test_array3, sorting_hat.sort(test_array3,0,4)
print test_array4, sortint_hat.sort(test_array4,0,4)

