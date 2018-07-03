def binarySearch(inputList, value):
	"""
	Executes a binary search on the inputList.

	Parameters
	----------
	
	inputList : list
		List of ints to search

	value : int
		Value to find.
		
	Returns
	-------
	Bool.
	"""
	if not inputList:
		return False
	elif inputList[len(inputList)/2] == value:
		return True
	else:	
		if inputList[len(inputList)/2] > value:
			return binarySearch(inputList[:len(inputList)/2],value)
		else:
			return binarySearch(inputList[(len(inputList)/2)+1:],value)

def binarySearchWithIndex(inputList, value, index=0):
	"""
	Executes a binary search on the inputList.

	Returns index if value present and -1 if not.

	Parameters
	----------
	
	inputList : list
		List of ints to search

	value : int
		Value to find.

	index : int
		Index of first element of list in terms of original input list.
	
	Returns
	-------
	Int.
	"""
	if not inputList:
		return -1
	elif inputList[len(inputList)/2] == value:
		return index+(len(inputList)/2)
	else:	
		if inputList[len(inputList)/2] > value:
			return binarySearchWithIndex(inputList[:len(inputList)/2],value,index)
		else:
			return binarySearchWithIndex(inputList[(len(inputList)/2)+1:],value,index+(len(inputList)/2)+1)

