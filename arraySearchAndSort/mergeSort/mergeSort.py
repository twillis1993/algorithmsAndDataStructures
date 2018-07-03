def mergeSort(lst):
	"""
	Sorts input list using the merge sort algorithm.

	Parameters
	----------

	lst : list
		List to sort.

	Returns
	-------
	List.
	"""
	if not lst:
		raise ValueError('\'lst\' is empty.')
	elif len(lst) == 1:
		return lst
	else:
		return merge(mergeSort(lst[:len(lst)/2]),mergeSort(lst[(len(lst)/2):]))

def merge(lstA, lstB):
	"""
	Merge sort subroutine which merges two lists and returns the result.

	Parameters
	----------
	
	lstA : list
		First list to merge.

	lstB : list
		Second list to merge

	Returns
	-------
	List.
	"""
	lst = []	

	i, j = (0,0)

	while j < len(lstA) and i < len(lstB):
		if lstB[i] < lstA[j]:
			lst.append(lstB[i])
			i += 1
		else:
			lst.append(lstA[j])
			j += 1

	if j < len(lstA):
		lst += lstA[j:]
	else:
		lst += lstB[i:]
					
	return lst
