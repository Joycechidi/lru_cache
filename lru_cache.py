""" This notebook is an implementation of various caching operations"""

class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def remove_chain(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None



class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def update_head(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
                node.remove_chain()
                self.head.prev = node
                node.next = self.head
                self.head = node
    def remove_tail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return 
        self.tail = self.tail.prev
        self.tail.next = None

class LRUCache:

    def __init__(self, max_size): 
        """
        Initialize a cache with a max size

        Arg:
            - max_size: Maximum capacity of the cache storage
        """
        self.max_size = max_size or 1
        self.cache = {}
        self.current_size = 0
        self.most_recent_list = DoublyLinkedList()

    def put_key_value(self, key, value):
        """
        Puts or maps a value to a key in the cache dictionary
        """
        if key not in self.cache:
            if self.current_size == self.max_size:
                self.delete_least_recent()
            else:
                self.current_size += 1
                self.cache[key] = DoublyLinkedListNode(key, value)

        else:
            self.replace_key(key, value)
            self.update_most_recent(self.cache[key])

    def get_value_from_key(self, key):
        """Gets the value of a key"""
        if key not in self.cache:
            return None
        self.update_most_recent(self.cache[key])
        return self.cache[key].value

    def get_most_recent_key(self):
        if self.most_recent_list.head is None:
            return None
        return self.most_recent_list.head.key


    def update_most_recent(self, node):
        """
        The doubly linked list needs to be updated after elements are moved
        
        """
        self.most_recent_list.update_head(node)
        
    def delete_least_recent(self):
        key_to_delete = self.most_recent_list.tail.key
        self.most_recent_list.remove_tail()
        del self.cache[key_to_delete]


    def delete_key(self, key):
        """
        Delete a key (In this case, delete the least recently used)
        """
        key_to_delete = self.most_recent_list.tail.key #tail contains the least recently used
        self.most_recent_list.remove_tail()
        del self.cache[key_to_delete]


    def reset_cache(self):
        """
        Reset a cache to remove all items from the cache
        """
        self.current_size = 0
        self.cache = {}
        self.most_recent_list = DoublyLinkedList()

    def replace_key(self, key, value):
        if key not in self.cache:
            raise Exception("This key is not in cache.")
        self.cache[key].value = value






