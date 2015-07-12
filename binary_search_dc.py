class Search_Functions:
	def binary_search_while(self, array, key):
		minimum = 0
		maximum = len(array) - 1
		middle = (minimum + maximum) / 2

		while minimum < maximum:
			if array[middle] == key:
				return middle

			elif array[middle] < key:
				lower = middle+1

			elif array[middle] > key:
				upper = middle-1

			middle = (minimum + maximum) / 2

		return None

searcher = Search_Functions()
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 1)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 3)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 5)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 6)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 7)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 8)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 9)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 10)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 11)
print searcher.binary_search_while([1,3,5,6,7,8,9,10], 0)
