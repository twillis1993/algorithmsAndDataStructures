import unittest
import binarySearch
import random

class BinarySearchTest(unittest.TestCase):	
	def test_normalEmptyInputList(self):
		self.assertEqual(False,binarySearch.binarySearch([],1))

	def test_normalSingletonInputListAbsent(self):
		self.assertEqual(False,binarySearch.binarySearch([0],1))

	def test_normalSingletonInputListPresent(self):
		self.assertEqual(True,binarySearch.binarySearch([1],1))

	def test_normalEvenInputListAbsent(self):
		self.assertEqual(False,binarySearch.binarySearch([0,1,2,3],4))
			
	def test_normalEvenInputListPresent(self):
		self.assertEqual(True,binarySearch.binarySearch([0,1,2,3],0))

	def test_normalOddInputListAbsent(self):
		self.assertEqual(False,binarySearch.binarySearch([0,1,2,3,4],5))

	def test_normalOddInputListPresent(self):
		self.assertEqual(True,binarySearch.binarySearch([0,1,2,3,4],0))

	def test_normalRandomEvenInputListPresent(self):	
		for i in range(10):
			self.assertEqual(True,binarySearch.binarySearch(list(range(1,101)),random.randint(1,100)))

	def test_normalWithIndexEmptyList(self):
		self.assertEqual(-1,binarySearch.binarySearchWithIndex([],1))

	def test_normalWithIndexSingletonListValueAbsent(self):
		self.assertEqual(-1,binarySearch.binarySearchWithIndex([0],1))

	def test_normalWithIndexSingletonListValuePresent(self):
		self.assertEqual(0,binarySearch.binarySearchWithIndex([1],1))

	def test_normalEvenInputListAbsent(self):
		self.assertEqual(-1,binarySearch.binarySearchWithIndex([0,1,2,3],4))
			
	def test_normalEvenInputListPresent(self):
		self.assertEqual(0,binarySearch.binarySearchWithIndex([0,1,2,3],0))

	def test_normalOddInputListAbsent(self):
		self.assertEqual(-1,binarySearch.binarySearchWithIndex([0,1,2,3,4],5))

	def test_normalOddInputListPresent(self):
		self.assertEqual(0,binarySearch.binarySearchWithIndex([0,1,2,3,4],0))

	def test_normalRandomEvenInputListPresent(self):	
		for i in range(10):	
			randValue = random.randint(1,100)
			inputList = list(range(1,101))
			self.assertEqual(inputList.index(randValue),
			binarySearch.binarySearchWithIndex(inputList,randValue))
