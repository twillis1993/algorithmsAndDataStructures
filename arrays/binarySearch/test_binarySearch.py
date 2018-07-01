import unittest
import binarySearch

class BinarySearchTest(unittest.TestCase):
	
	def test_errorFloatValue(self):
		with self.assertRaises(TypeError) as e:
			binarySearch.binarySearch([],1.0)

		self.assertEqual('Parameter \'value\' must be an int.', str(e.exception))

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
