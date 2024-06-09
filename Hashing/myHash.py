class myHash:
    def __init__(self, bucket):
        self.bucket = bucket
        self.table = [-1] * self.bucket

    def insert(self, var):
        if self.search(var):
            return "The element is already present in the hashmap."
        
        hash_key = var % self.bucket
        temp = hash_key

        while self.table[temp] != -1:
            if self.isFull():
                break

            temp = (temp + 1) % self.bucket

            if temp == hash_key:
                break
        
        if self.table[temp] == -1:
            self.table[temp] = var

        return self.table
        
    def search(self, var):
        hash_key = var % self.bucket

        if self.table[hash_key] == var:
            return True
        
        temp = (hash_key + 1) % self.bucket
        while temp != hash_key and self.table[temp] != -1:
            if self.table[temp] == var:
                return True
            
            temp = (temp + 1) % self.bucket

        return False

    def delete(self, var):
        hash_key = var % self.bucket
        if self.search(var):
            if self.table[hash_key] == var:
                self.table[hash_key] = "Deleted"

            else:
                temp = (hash_key + 1) % self.bucket
                while self.table[temp] != -1 and temp != hash_key:
                    if self.table[temp] == var:
                        self.table[temp] = "Deleted"
                        break

                    temp = (temp + 1) % self.bucket

            return self.table

        return "The element does not exist."
    
    def isFull(self):
        return False if -1 in self.table else True
    
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