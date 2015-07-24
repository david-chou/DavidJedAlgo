__author__ = 'davidchou'

class Search_Functions:
    def binary_search_while(self, array, key):
        minimum = 0
        maximum = len(array) - 1
        middle = (minimum + maximum) / 2

        while minimum <= maximum:
            if array[middle] == key:
                return middle

            elif array[middle] < key:
                minimum = middle + 1

            elif array[middle] > key:
                maximum = middle - 1

            middle = (minimum + maximum) / 2

        return None

    def binary_search_recurse_utility(self, the_array, key, imin, imax):
        if (imax < imin):
            return None
        else:
            imid = imin + ((imax - imin) / 2)
            if the_array[imid] > key:
                return self.binary_search_recurse_utility(the_array, key, imin, imid-1)
            elif the_array[imid] < key:
                return self.binary_search_recurse_utility(the_array, key, imid+1, imax)
            else:
                return imid

    def binary_search_recurse(self, array, key):
        return self.binary_search_recurse_utility(array, key, 0, len(array)-1)

searcher = Search_Functions()
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 1)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 3)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 5)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 6)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 7)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 8)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 9)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 10)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 11)
#print searcher.binary_search_while([1,3,5,6,7,8,9,10], 0)
#print ''
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 1)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 3)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 5)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 6)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 7)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 8)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 9)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 10)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 11)
print searcher.binary_search_recurse([1,3,5,6,7,8,9,10], 0)
print searcher.binary_search_recurse([1,30,56,62,53],30)
