from HashTable import HashTable


class ChainingHashTableItem:
    def __init__(self, itemKey, itemValue):
        self.key = itemKey
        self.value = itemValue
        self.next = None


class ChainingHashTable(HashTable):
    def __init__(self, initialCapacity=11):
        self.table = [None] * initialCapacity

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def insert(self, key, value):
        # Hash the key to get the bucket index
        bucket_index = self.hashKey(key) % len(self.table)

        # Traverse the linked list, searching for the key. If the key exists in
        # an item, the value is replaced. Otherwise a new item is appended.

        # add your code here
        item = self.table[bucket_index]
        previous = None
        while item != None:
            if key == item.key:
                item.value = value
                return True
            previous = item
            item = item.next
                
                

        # Append to the linked list
        if self.table[bucket_index] == None:
            self.table[bucket_index] = ChainingHashTableItem(key, value)
        else:
            previous.next = ChainingHashTableItem(key, value)
        return True

    # Searches for the specified key. If found, the key/value pair is removed
    # from the hash table and True is returned. If not found, False is returned.
    def remove(self, key):
        # Hash the key to get the bucket index
        bucket_index = self.hashKey(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        previous = None
        while item != None:
            if key == item.key:
                if previous == None:
                    # Remove linked list's first item
                    self.table[bucket_index] = item.next
                else:
                    previous.next = item.next
                return True
            previous = item
            item = item.next
        return False  # key not found

    # Searches for the key, returning the corresponding value if found, None if
    # not found.
    def search(self, key):
        # Hash the key to get the bucket index
        bucket_index = self.hashKey(key) % len(self.table)

        # Search the bucket's linked list for the key
        item = self.table[bucket_index]
        previous = None
        while item != None:
            if key == item.key:
                return item.value
            item = item.next
            
            
        return None
        # add your code here

    def __str__(self):
        result = ""
        for i in range(len(self.table)):
            result += "%d: " % i
            if self.table[i] == None:
                result += "(empty)\n"
            else:
                item = self.table[i]
                while item != None:
                    result += "%s, %s --> " % (str(item.key), str(item.value))
                    item = item.next
                result += "\n"
        return result