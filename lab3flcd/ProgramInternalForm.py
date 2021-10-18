class PIF:
    def __init__(self):
        self.__data = []

    def add(self, token, pos):
        self.__data.append((token, pos))

    def __str__(self):
        resultToStr = ""
        for element in self.__data:
            resultToStr += element[0] + "->" + str(element[1]) + "\n"
        return resultToStr