class myHash:
    def __init__(self, bucket):
        self.bucket = bucket
        self.table = [[] for i in range(self.bucket)]

    def insert(self, var):
        if self.search(var):
            return "The element is already present in the hashmap."
        
        hash_key = var % self.bucket
        self.table[hash_key].append(var)
        return self.table
        
    def search(self, var):
        hash_key = var % self.bucket
        return var in self.table[hash_key]

    def delete(self, var):
        hash_key = var % self.bucket
        if self.search(var):
            self.table[hash_key].remove(var)
            return self.table

        return "The element does not exist."
    
p = myHash(7)
print(p.insert(10))
print(p.insert(19))
print(p.insert(5))
print(p.insert(22))
print(p.search(19))
print(p.search(20))
print(p.delete(19))
print(p.delete(19))
print(p.delete(20))
