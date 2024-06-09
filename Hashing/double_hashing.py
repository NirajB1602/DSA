class DoubleHashing:
    def __init__(self, size, double_hash_value):
        self.size = size
        self.hash_table = [None] * self.size
        self.double_hash_value = double_hash_value

    def _hash1(self, key):
        return key % self.size

    def _hash2(self, key):
        return self.double_hash_value - (key % self.double_hash_value)

    def insert(self, key, value):
        index = self._hash1(key)

        if self.hash_table[index] is None:
            self.hash_table[index] = (key, value)
        else:
            # Collision resolution with double hashing
            index2 = self._hash2(key)
            i = 1
            while True:
                new_index = (index + i * index2) % self.size
                if self.hash_table[new_index] is None:
                    self.hash_table[new_index] = (key, value)
                    break
                i += 1

    def search(self, key):
        index = self._hash1(key)
        if self.hash_table[index] is not None and self.hash_table[index][0] == key:
            return self.hash_table[index][1]
        else:
            # Search for the key using double hashing
            index2 = self._hash2(key)
            i = 1
            while self.hash_table[new_index] is not None:
                new_index = (index + i * index2) % self.size
                if self.hash_table[new_index][0] == key:
                    return self.hash_table[new_index][1]
                i += 1
                
            return None


hash_table = DoubleHashing(10, 7)

hash_table.insert(5, "Apple")
hash_table.insert(15, "Banana")
hash_table.insert(25, "Cherry")
print(hash_table.search(5)) 