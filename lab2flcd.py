from collections import deque

class HashTable:

    def __init__(self, size):
        self.__keys = [deque() for _ in range(size)]
        self.__size = size

    def add(self, key):
        if self.contains(key):
            return self.find(key)
        else:
            self.__keys[self.hashFunction(key)].append(key)
            return self.find(key)

    def contains(self, key):
        return key in self.__keys[self.hashFunction(key)]

    def delete(self, key):
        self.__keys[self.hashFunction(key)].remove(key)

    def find(self, key):
        positionInList = 0
        positionInHashTable= self.hashFunction(key)
        for item in self.__keys[positionInHashTable]:
            if item != key:
                positionInList += 1
            else:
                break
        return (positionInHashTable, positionInList)

    def hashFunction(self, key):
        total = 0
        for character in key:
            total += (ord(character) - ord('0'))
        return total % self.__size

    def __str__(self) -> str:
        toStr = ""
        for idx in range(self.__size):
            toStr = toStr + str(idx) + "->" + str(self.__keys[idx]) + "\n"
        return toStr

class SymbolTable:

    def __init__(self, size):
        self.__hashTable = HashTable(size)

    def __str__(self) -> str:
        return str(self.__hashTable)

    def add(self, key):
        return self.__hashTable.add(key)

    def contains(self, key):
        return self.__hashTable.contains(key)

    def remove(self, key):
        self.__hashTable.delete(key)

    def find(self, key):
        return self.__hashTable.find(key)