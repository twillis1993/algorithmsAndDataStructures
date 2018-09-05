import unittest

from node import TreeNode

class TestTreeNode(unittest.TestCase):
	def test_normalInit(self):
		self.assertEqual(TreeNode(2).value,2)

	def test_normalSetItem(self):
		pass
	
	def test_errorSetItem_DifferentValueTypes(self):
		with self.assertRaises(Exception) as cm:
			treeNode = TreeNode(1)
			treeNode['child0'] = TreeNode(2.0)

		self.assertEqual('Parent and child nodes\' values must share the same type', str(cm.exception))

	# TODO	
	def test_normalStr(self):
		pass
				
	def test_normalRamify_noKeys(self):
		treeNode = TreeNode(1)
		treeNode.ramify(range(3))
		self.assertEqual(range(3), [x.value for x in treeNode.children.values()])

	def test_normalRamify_WithKeys(self):
		treeNode = TreeNode(1)
		treeNode.ramify(range(3),['kid'+str(x) for x in range(3)])

		self.assertEqual(treeNode.children, {'kid'+str(x):x for x in range(3)})
	
	def test_errorRamify_childrenPresent(self):
		with self.assertRaises(Exception) as cm:
			treeNode = TreeNode(1)
			treeNode['child0'] = TreeNode(2)
			treeNode.ramify([1,1])

		self.assertEqual('Node already has 1 children',str(cm.exception))

	

