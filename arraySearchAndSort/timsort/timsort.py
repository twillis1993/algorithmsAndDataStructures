import pythonCode.algorithmsAndDataStructures.arraySearchAndSort.insertionSort as insertionSort

def timsort():
	pass

def reverseDescendingRuns(lst):
	"""
	Reverses order of descending runs in list.

	Modifies list in place.

	Parameters
	---------

	lst : list
		List to sort.

	Returns 
	-------
	List.
	"""
	runStack = getRunStack(lst)
	
	while runStack:
		start, stop = runStack.pop()

		lst = reverseSubsequence(lst, start, stop)
	
	return lst

def reverseSubsequence(lst, start, stop):
	"""
	"""
	if start >= stop:
		return lst
	else:
		lst[start], lst[stop] = lst[stop], lst[start]
		return reverseSubsequence(lst, start+1,stop-1)

def getRunStack(lst):
	"""
	Identifies all runs of descending elements.

	Parameters
	----------
	lst : list
		List to sort.

	Returns
	-------
	List.
	"""
	runStack = []
	
	i = 0

	while i < len(lst)-1:
		# Descending
		if lst[i] > lst[i+1]:	
			j = i+1
			while j < len(lst)-1 and lst[j] > lst[j+1]:
				j += 1

			runStack.append((i,j))

			i = j+1
		else:
			i += 1

	return runStack	
