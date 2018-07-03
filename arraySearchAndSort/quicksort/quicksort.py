def quicksort(inputList):
	"""
	Executes quicksort on inputList.

	Parameters
	----------
	
	inputList : list
		List to sort.

	Returns
	-------
	List.
	"""
	if not inputList:
		return []	
	else:
		return quicksort(filter(lambda x: x < inputList[len(inputList)/2], inputList))+[inputList[len(inputList)/2]]+quicksort(filter(lambda x: x > inputList[len(inputList)/2], inputList))	
