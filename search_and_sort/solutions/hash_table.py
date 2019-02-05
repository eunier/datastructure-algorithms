"""
# Implementation of a Hash Table

In this lecture we will be implementing our own Hash Table to complete our understanding of Hash Tables and Hash
Functions! Make sure to review the video lecture before this to fully understand this implementation!

Keep in mind that Python already has a built-in dictionary object that serves as a Hash Table, you would never actually
need to implement your own hash table in Python.

___
## Map
The idea of a dictionary used as a hash table to get and retrieve items using **keys** is often referred to as a
mapping. In our implementation we will have the following methods:


* **HashTable()** Create a new, empty map. It returns an empty map collection.
* **put(key,val)** Add a new key-value pair to the map. If the key is already in the map then replace the old value
with the new value.
* **get(key)** Given a key, return the value stored in the map or None otherwise.
* **del** Delete the key-value pair from the map using a statement of the form del map[key].
* **len()** Return the number of key-value pairs stored
* **in** the map in Return True for a statement of the form **key in map**, if the given key is in the map, False
otherwise.
"""


class HashTable(object):
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size     # example: [None] * 2 = [None, None]
        self.val = [None] * self.size

    def put(self, key, val):
        # get the hash value suing the key and the length of slots
        hash_val = self.hash_func(key, len(self.slots))

        if self.slots[hash_val] is None:
            self.slots[hash_val] = key
            self.slots[hash_val] = val
        else:
            if self.slots[hash_val] == key:
                self.val[hash_val] = val
            else:
                next_slot = self.rehash(hash_val, len(self.slots))

                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.val[next_slot] = val
                else:
                    self.val[next_slot] = val

    @staticmethod
    def hash_func(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_func(key, len(self.slots))
        val = None
        stop = False
        found = False
        position = start_slot
        slot_position = self.slots[position]

        while slot_position is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                val = self.val[position]
            else:
                position = self.rehash(position, len(self.slots))

                if position == start_slot:
                    stop = True

        return val

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, val):
        self.put(key, val)


h = HashTable(5)
print(h)
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'
print(h[2])

