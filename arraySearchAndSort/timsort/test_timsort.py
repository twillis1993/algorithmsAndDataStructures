import unittest
import timsort

class TestTimsort(unittest.TestCase):
	def test_normalGetRunStackEmptyList(self):
		self.assertEqual([], timsort.getRunStack([]))	
	
	def test_normalGetRunStackSingletonList(self):
		self.assertEqual([], timsort.getRunStack([1]))

	def test_normalGetRunStackAscendingList(self):
		self.assertEqual([], timsort.getRunStack([1,2,3,4,5]))

	def test_normalGetRunStackDescendingList(self):
		self.assertEqual([(0,4)], timsort.getRunStack([5,4,3,2,1]))

	def test_normalGetRunStackListWithDescendingRun(self):
		self.assertEqual([(2,6)], timsort.getRunStack([1,2,5,4,3,2,1]))

	def test_normalGetRunStackDescendingListWithRepeats(self):
		self.assertEqual([(0,1),(2,3)], timsort.getRunStack([5,4,4,3,3]))

	def test_normalGetRunStackListWithDistinctDescendingRuns(self):
		self.assertEqual([(2,3),(4,5),(6,8)], timsort.getRunStack([1,2,5,4,6,1,3,2,1]))
	
	def test_normalReverseSubsequenceSingleton(self):
		self.assertEqual([1], timsort.reverseSubsequence([1],0,0))

	def test_normalReverseSubsequenceCouplet(self):
		self.assertEqual([2,1], timsort.reverseSubsequence([1,2],0,1))

	def test_normalReverseSubsequenceTriplet(self):
		self.assertEqual([3,2,1], timsort.reverseSubsequence([1,2,3],0,2))

	def test_normalReverseSubsequenceLengthTenList(self):
		self.assertEqual(range(10, 0, -1), timsort.reverseSubsequence(range(1,11), 0,9))

	def test_normalReverseDescendingRunsEmptyList(self):
		self.assertEqual([], timsort.reverseDescendingRuns([]))	
	
	def test_normalReverseDescendingRunsSingletonList(self):
		self.assertEqual([1], timsort.reverseDescendingRuns([1]))

	def test_normalReverseDescendingRunsAscendingList(self):
		self.assertEqual([1,2,3,4,5], timsort.reverseDescendingRuns([1,2,3,4,5]))

	def test_normalReverseDescendingRunsDescendingList(self):
		self.assertEqual([1,2,3,4,5], timsort.reverseDescendingRuns([5,4,3,2,1]))

	def test_normalReverseDescendingRunsListWithDescendingRun(self):
		self.assertEqual([1,2,1,2,3,4,5], timsort.reverseDescendingRuns([1,2,5,4,3,2,1]))

	def test_normalReverseDescendingRunsDescendingListWithRepeats(self):
		self.assertEqual([4,5,3,4,3], timsort.reverseDescendingRuns([5,4,4,3,3]))

	def test_normalReverseDescendingRunsListWithDistinctDescendingRuns(self):
		self.assertEqual([1,2,4,5,1,6,1,2,3], timsort.reverseDescendingRuns([1,2,5,4,6,1,3,2,1]))

