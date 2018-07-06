import unittest
import insertionSort
import random

class TestInsertionSort(unittest.TestCase):
	def test_normalEmptyList(self):
		self.assertEqual([],insertionSort.insertionSort([]))

	def test_normalSingletonList(self):
		self.assertEqual([1], insertionSort.insertionSort([1]))

	def test_normalSortedList(self):	
		self.assertEqual([1,2,3], insertionSort.insertionSort([1,2,3]))

	def test_normalUnsortedList(self):	
		self.assertEqual([1,2,3], insertionSort.insertionSort([3,2,1]))

	def test_normalLargerUnsortedList(self):	
		unsortedLst = range(1,101)
		random.shuffle(unsortedLst)
		self.assertEqual(range(1,101), insertionSort.insertionSort(unsortedLst))

