import unittest
import mergeSort
import random

class TestMergeSort(unittest.TestCase):	

	def test_normalMergeEmptyLists(self):
		self.assertEqual([], mergeSort.merge([],[]))

	def test_normalMergeEmptyAndSingletonLists(self):
		self.assertEqual([1], mergeSort.merge([],[1]))

	def test_normalMergeEmptyAndSingletonLists(self):
		self.assertEqual([1], mergeSort.merge([],[1]))

	def test_normalMergeIdenticalSingletonLists(self):
		self.assertEqual([1,1], mergeSort.merge([1],[1]))

	def test_normalMergeSingletonLists(self):
		self.assertEqual([1,2], mergeSort.merge([2],[1]))

	def test_normalMergeLists(self):	
		self.assertEqual([1,2,3], mergeSort.merge([2,3],[1]))

	def test_normalMergeSortIdenticalList(self):
		self.assertEqual([1,1],mergeSort.mergeSort([1, 1]))
	
	def test_normalMergeSortList(self):
		self.assertEqual([1, 2, 3, 4],mergeSort.mergeSort([4, 1, 2, 3]))

	def test_normalMergeSortLargeList(self):	
		lst = range(1,101)
		random.shuffle(lst)		
		self.assertEqual(range(1,101),mergeSort.mergeSort(lst))

	
