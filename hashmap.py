# Author:        Bryan Yang
# Student ID:    #001303738
# Major:         B.S. Computer Science. Started 10/1/22
# Email:         byang10@wgu.edu
# Date:          12/3/22


class HashMap:

    # Big-O Notation: O(n)
    def __init__(self, capacity=100):
        # Initialize hash table with empty entries
        self.capacity = capacity
        self.hashMap = []
        for i in range(capacity):
            self.hashMap.append([])

    # Compute Index using Key.
    # 'get_hash' result in Index.
    # Big-O Notation: O(1)
    def get_hash(self, key):
        return key % self.capacity

    # Insert packages into the hash table
    # Big-O Notation: O(1)
    def insert(self, package):
        key = package.pk_id
        hash_key = self.get_hash(key)
        self.hashMap[hash_key].append(package)

    # Delete packages from the hash table
    # Big-O Notation: O(1)
    def delete(self, package):
        key = package.pk_id
        hash_key = self.get_hash(key)
        self.hashMap[hash_key].remove(package)

    # Get hash_key if key is in hash map.
    # Big-O Notation: O(n)
    def get(self, key):
        hash_key = self.get_hash(key)
        if self.hashMap[hash_key] is not None:
            for i, item in self.hashMap[hash_key]:
                # Big-O: O(n)
                if i == key:
                    return item
        else:
            return None
