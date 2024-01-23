# Base class for a hash table that supports the insert, remove, and search
# operations.
class HashTable:
    # Returns a non-negative hash code for the specified key.
    def hashKey(self, key):
        return abs(hash(key))

    # Inserts the specified key/value pair. If the key already exists, the
    # corresponding value is updated. If inserted or updated, True is returned.
    # If not inserted, then False is returned.
    def insert(self, key, value):
        pass

    # Searches for the specified key. If found, the key/value pair is removed
    # from the hash table and True is returned. If not found, False is returned.
    def remove(self, key):
        pass

    # Searches for the key, returning the corresponding value if found, None if
    # not found.
    def search(self, key):
        pass