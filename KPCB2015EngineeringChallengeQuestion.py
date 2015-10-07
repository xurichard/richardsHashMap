# Richard Xu KPBC Fellows Challenge Question
# Problem
# Using only primitive types, implement a fixed-size hash map that associates string keys with arbitrary data object references (you don't need to copy the object). Your data structure should be optimized for algorithmic runtime and memory usage. You should not import any external libraries, and may not use primitive hash map or dictionary types in languages like Python or Ruby.

# The solution should be delivered in one class (or your language's equivalent) that provides the following functions:

# 	constructor(size): return an instance of the class with pre-allocated space for the given number of objects.
# 	boolean set(key, value): stores the given key/value pair in the hash map. Returns a boolean value indicating success / failure of the operation.
# 	get(key): return the value associated with the given key, or null if no value is set.
# 	delete(key): delete the value associated with the given key, returning the value on success or null if the key has no value.
# 	float load(): return a float value representing the load factor (`(items in hash map)/(size of hash map)`) of the data structure. Since the size of the dat structure is fixed, this should never be greater than 1.

# If your language provides a built-in hashing function for strings (ex. `hashCode` in Java or `__hash__` in Python) you are welcome to use that. If not, you are welcome to do something naive, or use something you find online with proper attribution.

# Instructions
# Please provide the source, tests, runnable command-line function and all the resources required to compile (if necessary) and run the following program. You are free to use any coding language that compiles/runs on *nix operating systems and requires no licensed software.

# Upload your answer as a compressed file (.zip or .tar)

class richardsHashMap(object):

	class richardsEntry:
		def __init__(self, key, value):
			self.key = key
			self.value = value
			self.next = None

		def getKey(self):
			return self.key

		def getValue(self):
			return self.value

		def setValue(self, value):
			self.value = value
			return self.value

		def getNext(self):
			return self.next

		def setNext(self, entry):
			self.next = entry
			return self.next

	def __init__(self, size):
		self.size = size
		self.load_factor = 0.75
		self.num_entries = 0
		self.entries = [None]*self.size

	# I'm not actually sure when a set would fail
	def set(self, key, value):
		hash_value = key.__hash__()%self.size
		entry = self.entries[hash_value]
		if entry:
			# if there are entries, then we must traverse all entries in the bucket
			while entry.getNext():
				if entry.getKey() == key:
					entry.setValue(value)
					return True # replacing an existing key, value pair
				entry = entry.getNext()
			# one more check for the last element in the bucket
			if entry.getKey() == key:
				entry.setValue(value)
				return True # replacing an existing key, value pair
			entry.next = self.richardsEntry(key, value) # appending to the end of entries
		else: # else entry doesn't exist
			self.entries[hash_value] = self.richardsEntry(key, value) # placing the first entry into a previously empty bucket

		self.num_entries += 1
		if self.load() >= self.load_factor:
			self.rehash()
		return True

	def get(self, key):
		hash_value = key.__hash__()%self.size
		entry = self.entries[hash_value]
		while entry:
			if entry.getKey() == key:
				return entry.getValue()
		return None

	def delete(self, key):
		delete_value = None
		previous_entry = None
		entry = self.entries[key.__hash__()%self.size]
		while entry:
			if entry.getKey() == key: # we have to remove this entry
				delete_value = entry.getValue()
				if previous_entry: # we have more than one entry in the bucket
					previous_entry.setNext(entry.getNext())
				else: # we only have one entry in the bucket, so remove it
					self.entries[key.__hash__()%self.size] = entry.getNext()
			entry = entry.getNext()
		return delete_value


	def load(self):
		return float(self.num_entries)/self.size


	def rehash(self):
		self.size *= 2
		old_entries = self.entries
		self.entries = [None]*self.size
		self.num_entries = 0

		for entry in old_entries: # go through each bucket and rehash all entries in the bucket
			while entry:
				self.set(entry.getKey(), entry.getValue())
				entry = entry.getNext()


	def getSize(self):
		return self.size

	def getNumEntries(self):
		return self.num_entries




