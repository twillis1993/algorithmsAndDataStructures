from abc import ABCMeta

class Node:
	"""				
	Abstract node base class for data structures.
	"""	
	__metaclass__ = ABCMeta

	def __init__(self, value):
		"""
		value : ?
			Value to store in this Node.
		"""
		self.value = value	

class TreeNode(Node):
	"""
	Models nodes comprising tree data structures.
	"""

	def __init__(self, value):
		"""
		value : ?
			Value to store in this Node.
		"""
		super(TreeNode,self).__init__(value)
		self.children = {}

	def __getitem__(self,key):
		return self.children[key]

	def __setitem__(self, key, treeNode):
		if type(self.value) != type(treeNode.value):
			raise TypeError('Parent and child nodes\' values must share the same type')
		else:
			self.children[key] = treeNode
	
	# TODO
	def __str__(self):
		pass

	def ramify(self, values, keys=None):
		"""
		Creates children for this TreeNode.

		values : list
			Values with which to instantiate the children.

		keys : list
			Keys for children.		
		"""
		if self.children:
			raise Exception('Node already has %d children' % len(self.children))

		# Use for loops rather than list comprehension so we can outsource the value type-checking to __setitem__
		elif keys:	
			for key, value in zip(keys,values):
				self[key] = TreeNode(value)
		else:	
			for key, value in zip(['child'+str(i) for i in range(len(values))],values):
				self[key] = TreeNode(value)

	def ramifyRandomly(self,degree=2):
		"""
		Creates children for this TreeNode with random values of the same type as this TreeNode's value.
		"""
		pass		
