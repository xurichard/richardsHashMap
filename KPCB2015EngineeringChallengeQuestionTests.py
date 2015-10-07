import unittest
from KPCB2015EngineeringChallengeQuestion import *

class richardsHashMapTests(unittest.TestCase):

	def testConstructor(self):
		# tests the smallest hashmap
		testHashMap = richardsHashMap(1)
		self.failUnless(testHashMap.getSize() == 1)
		self.failUnless(testHashMap.getNumEntries() == 0)

	def testConstructor2(self):
		# tests a larger hashmap
		testHashMap2 = richardsHashMap(300)
		self.failUnless(testHashMap2.getSize() == 300)
		self.failUnless(testHashMap2.getNumEntries() == 0)

	def testSet(self):
		testHashMap = richardsHashMap(8)
		testHashMap.set('key', 'value')
		self.failUnless(testHashMap.getSize() == 8)
		self.failUnless(testHashMap.getNumEntries() == 1)
		self.failUnless(testHashMap.get('key') == 'value')
		self.failUnless(testHashMap.get('anotherKey') == None)

	def testSet2(self):
		# tests set method for replacing an existing key value pair with a new value
		testHashMap2 = richardsHashMap(8)
		testHashMap2.set('key', 'value')
		self.failUnless(testHashMap2.get('key') == 'value')

		# set the same key to a new value
		testHashMap2.set('key', 'newValue')
		self.failIf(testHashMap2.get('key') == 'value')
		self.failUnless(testHashMap2.get('key') == 'newValue')
		self.failUnless(testHashMap2.getSize() == 8)
		self.failUnless(testHashMap2.getNumEntries() == 1)

	def testSet3(self):
		# tests set method for rehashing functionality
		testHashMap3 = richardsHashMap(2)
		testHashMap3.set('k1', 'v1')
		testHashMap3.set('k2', 'v2')
		# should rehash here
		self.failIf(testHashMap3.getSize() == 2)
		self.failUnless(testHashMap3.getSize() == 4)
		self.failUnless(testHashMap3.load() == 0.5)

		# now testHashMap3 has a size of 4, num_entries = 2
		testHashMap3.set('k3', 'v3')

		# should rehash here
		self.failIf(testHashMap3.getSize() == 4)
		self.failUnless(testHashMap3.getSize() == 8)
		self.failUnless(testHashMap3.load() == 0.375)

		# now testHashMap3 has a size of 8, num_entries = 3
		testHashMap3.set('k4', 'v4')
		testHashMap3.set('k5', 'v5')
		testHashMap3.set('k6', 'v6')

		# should rehash here
		self.failIf(testHashMap3.getSize() == 8)
		self.failUnless(testHashMap3.getSize() == 16)
		self.failUnless(testHashMap3.load() == 0.375)
		# now testHashMap3 has a size of 16, num_entries = 6

	def testGet(self):
		# tests get method for some set
		testHashMap = richardsHashMap(16)
		testHashMap.set('k1', 'v1')
		testHashMap.set('k2', 'v2')
		testHashMap.set('k3', 'v3')
		testHashMap.set('k4', 'v4')
		testHashMap.set('k5', 'v5')
		testHashMap.set('k6', 'v6')
		testHashMap.set('k7', 'v7')
		testHashMap.set('k8', 'v8')
		testHashMap.set('k9', 'v9')
		testHashMap.set('k10', 'v10')
		testHashMap.set('k11', 'v11')

		self.failUnless(testHashMap.get('k1') == 'v1')
		self.failUnless(testHashMap.get('k2') == 'v2')
		self.failUnless(testHashMap.get('k3') == 'v3')
		self.failUnless(testHashMap.get('k4') == 'v4')
		self.failUnless(testHashMap.get('k5') == 'v5')
		self.failUnless(testHashMap.get('k6') == 'v6')
		self.failUnless(testHashMap.get('k7') == 'v7')
		self.failUnless(testHashMap.get('k8') == 'v8')
		self.failUnless(testHashMap.get('k9') == 'v9')
		self.failUnless(testHashMap.get('k10') == 'v10')

	def testGet2(self):
		# tests get if the key is set to another value
		testHashMap2 = richardsHashMap(16)
		testHashMap2.set('k1', 'v1')
		self.failUnless(testHashMap2.get('k1') == 'v1')

		# new value is now v2
		testHashMap2.set('k1', 'v2')
		self.failUnless(testHashMap2.get('k1') == 'v2')

		# new value is now v3
		testHashMap2.set('k1', 'v3')
		self.failUnless(testHashMap2.get('k1') == 'v3')

		# new value is now v4
		testHashMap2.set('k1', 'v4')
		self.failUnless(testHashMap2.get('k1') == 'v4')


	def testDelete(self):
		# tests delete method for basic functionality
		testHashMap = richardsHashMap(16)
		testHashMap.set('key', 'value')
		self.failUnless(testHashMap.get('key') == 'value')
		self.failUnless(testHashMap.getNumEntries() == 1)

		delete_value = testHashMap.delete('key')
		self.failIf(testHashMap.get('key') == 'value')
		self.failIf(testHashMap.get('key'))
		self.failUnless(testHashMap.getNumEntries() == 0)
		self.failUnless(delete_value == 'value')

	def testDelete2(self):
		# test delete method in hashmap of multiple entries
		testHashMap2 = richardsHashMap(16)
		testHashMap2.set('k1', 'v1')
		testHashMap2.set('k2', 'v2')
		testHashMap2.set('k3', 'v3')
		testHashMap2.set('k4', 'v4')

		delete_value = testHashMap2.delete('k3')
		self.failIf(testHashMap2.get('k3') == 'v3')
		self.failIf(testHashMap2.get('k3'))
		self.failUnless(testHashMap2.getNumEntries() == 3)
		self.failUnless(delete_value == 'v3')

	def testDelete3(self):
		# test delete method on key that doesn't exist (should return None)
		testHashMap3 = richardsHashMap(16)
		delete_value = testHashMap3.delete('key')
		self.failIf(testHashMap3.get('key'))
		self.failUnless(testHashMap3.getNumEntries() == 0)
		self.failIf(delete_value)

	def testLoad(self):
		# test load method for basic functionality
		testHashMap = richardsHashMap(16)
		testHashMap.set('k1', 'v1')
		self.failUnless(testHashMap.load() == 0.0625)
		testHashMap.set('k2', 'v2')
		self.failUnless(testHashMap.load() == 0.125)
		testHashMap.set('k3', 'v3')
		self.failUnless(testHashMap.load() == 0.1875)
		testHashMap.set('k4', 'v4')
		self.failUnless(testHashMap.load() == 0.25)
		testHashMap.set('k5', 'v5')
		self.failUnless(testHashMap.load() == 0.3125)
		testHashMap.set('k6', 'v6')
		self.failUnless(testHashMap.load() == 0.375)
		testHashMap.set('k7', 'v7')
		self.failUnless(testHashMap.load() == 0.4375)
		testHashMap.set('k8', 'v8')
		self.failUnless(testHashMap.load() == 0.5)
		testHashMap.set('k9', 'v9')
		self.failUnless(testHashMap.load() == 0.5625)

	def testLoad2(self):
		# test load method for replacing value for an existing key-value pair
		testHashMap2 = richardsHashMap(5)
		testHashMap2.set('k1', 'v1')
		self.failUnless(testHashMap2.load() == 0.2)
		testHashMap2.set('k1', 'v2')
		self.failUnless(testHashMap2.load() == 0.2)


	def testLoad3(self):
		# test load method for when rehashing occurs
		# tests set method for rehashing functionality
		testHashMap3 = richardsHashMap(2)
		testHashMap3.set('k1', 'v1')
		self.failUnless(testHashMap3.load() == 0.5)

		testHashMap3.set('k2', 'v2')
		# should rehash here
		self.failUnless(testHashMap3.load() == 0.5)

		# now testHashMap3 has a size of 4, num_entries = 2
		testHashMap3.set('k3', 'v3')

		# should rehash here
		self.failUnless(testHashMap3.load() == 0.375)

		# now testHashMap3 has a size of 8, num_entries = 3
		testHashMap3.set('k4', 'v4')
		self.failUnless(testHashMap3.load() == 0.5)
		testHashMap3.set('k5', 'v5')
		self.failUnless(testHashMap3.load() == 0.625)
		testHashMap3.set('k6', 'v6')
		# should rehash here
		self.failUnless(testHashMap3.load() == 0.375)
		# now testHashMap3 has a size of 16, num_entries = 6


def main():
	unittest.main()

if __name__ == '__main__':
	main()