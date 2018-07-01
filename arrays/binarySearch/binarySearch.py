import sys
import argparse

# TODO: unsorted input list?
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
	if type(value) != int:
		raise TypeError('Parameter \'value\' must be an int.')

	if not inputList:
		return False
	elif inputList[len(inputList)/2] == value:
		return True
	else:	
		if inputList[len(inputList)/2] > value:
			return binarySearch(inputList[:len(inputList)/2],value)
		else:
			return binarySearch(inputList[(len(inputList)/2)+1:],value)
