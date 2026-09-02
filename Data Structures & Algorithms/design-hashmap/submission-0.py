class MyHashMap:

    def __init__(self):
        self.size = 10**4
        self.bucket = [[] for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        for pair in self.bucket[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.bucket[index].append([key,value])

    def get(self, key: int) -> int:
        index = key % self.size

        for pair in self.bucket[index]:
            if pair[0]==key:
                return pair[1]
        return -1
    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.bucket[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)