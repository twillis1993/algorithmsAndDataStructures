import unittest
import quicksort
import random

class TestQuicksort(unittest.TestCase):
	def test_normalEmptyInputList(self):
		self.assertEqual([], quicksort.quicksort([]))
	
	def test_normalSingletonList(self):
		self.assertEqual([0], quicksort.quicksort([0]))

	def test_normalOddSortedList(self):
		self.assertEqual([0,1,2,3,4], quicksort.quicksort([0,1,2,3,4]))

	def test_normalEvenSortedList(self):
		self.assertEqual([0,1,2,3], quicksort.quicksort([0,1,2,3]))

	def test_normalOddUnsortedList(self):	
		self.assertEqual([0,1,2,3,4], quicksort.quicksort([0,2,4,1,3]))

	def test_normalOddUnsortedList(self):	
		lst = range(101)
		random.shuffle(lst)	
		self.assertEqual(range(101), quicksort.quicksort(lst))	

	def test_normalEvenUnsortedList(self):	
		lst = range(100)
		random.shuffle(lst)	
		self.assertEqual(range(100), quicksort.quicksort(lst))	
