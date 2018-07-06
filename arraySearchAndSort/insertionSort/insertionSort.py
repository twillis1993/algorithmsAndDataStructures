def insertionSort(lst):
	"""
	Executes insertion sort on input.

	Parameters
	----------

	lst : list
		List to sort.

	Returns
	-------
	List.	
	"""
	if not lst:
		return lst

	sortedLst = lst[:]
	
	i = 1	
		
	while i < len(sortedLst):
		j = i - 1	
		while j >= 0 and sortedLst[j] > sortedLst[j+1]:
			temp = sortedLst[j]	
			sortedLst[j] = sortedLst[j+1]
			sortedLst[j+1] = temp	
			j -= 1
		i +=1

	return sortedLst		
