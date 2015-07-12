

class Searcher:

    def binary_search_while(self, array, to_find):
        lower = 0
        upper = len(array) - 1 if len(array) % 2 == 1 else len(array)
        mid = (lower+upper) / 2

        while lower < upper:

            if array[mid] == to_find:
                return mid

            # The middle value is greater than value to compare
            # Search the right half of the array
            elif array[mid] > to_find:
                upper = mid

            # The middle value is less than the value being compared
            # Search the left half of the array
            elif array[mid] < to_find:
                lower = mid

            # Set mid to value at midpoint of lower and upper
            mid = (lower+upper) / 2

        return None

# Test cases
search_class = Searcher()

print search_class.binary_search_while( [1,3,5], 3)
print search_class.binary_search_while( [1,2,3,4,5,6,7,8], 8)
print search_class.binary_search_while( [1,3,6,7,8,10,15,23,25], 1)
print search_class.binary_search_while( [1,3,6,7,8,10,15,23,25,29], 1)
print search_class.binary_search_while( [1,3,5,6,7,8,10,13,15], 8)