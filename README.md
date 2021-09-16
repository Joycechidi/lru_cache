# Least Recently Used (LRU) Cache Implementation in Python
This program contains pythoon code for various classes, functions and methods that implement various operations in the Least Recently Used Caching strategy. 

Two types of data structure were used to provide local data stroage for the cached items. A hash map in the form of python dictionary was combined with a Doubly Linked List(DLL) to implement the LRU cache. The dictionary is used to map every item in the cache to a specific location in the doubly linked list. The head of the DLL points to the most recently used entry, the tail points to the least recently used entry.

**Why a Dictionary and a Doubly Linked List?**

These two data structures were chosen for the following reasons.
Hash map or a dictionary will allow for inserting, retrieving, and deleting items. We need to keep track of the order of items and dictionaries don’t keep track of orders. 
Constant time is needed to make the newly accessed key-value pair the most recent once the key-value pair is retrieved. 

**Storing the keys** 

Map them to nodes in a doubly linked list containing the keys’ corresponding values
With these 2 data structures, any key-value pair can be accessed easily from the hash table and easily move nodes in the linkedlist in order to keep track of the most recent and least recent key-value pairs
Linkedlist will keep track of the order of the pairs which helps with updating the least recent key-value pairs after deletion.

#How to use this repository


