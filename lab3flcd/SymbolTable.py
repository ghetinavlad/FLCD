class SymbolTable:
    def __init__(self, size: int) -> None:
        self.__items = [[] for _ in range(size)]
        self.__size = size

    def hashFunction(self, key: str) -> int:
        sum = 0
        for character in key:
            sum += (ord(character) - ord('0'))
        return sum % self.__size

    def find(self, key):
        list_position = self.hashFunction(key)
        list_index = 0
        for item in self.__items[list_position]:
            if item != key:
                list_index += 1
            else:
                break
        return (list_position, list_index)

    def add(self, key: str):
        if self.contains(key):
            return self.find(key)
        self.__items[self.hashFunction(key)].append(key)
        return self.find(key)

    def delete(self, key) -> None:
        position = self.hashFunction(key)
        self.__items[position].remove(key)

    def contains(self, key) -> bool:
        return key in self.__items[self.hashFunction(key)]

    def __str__(self) -> str:
        resultToStr = ""
        for i in range(self.__size):
            resultToStr += str(i) + "->" + str(self.__items[i]) + "\n"
        return resultToStr


