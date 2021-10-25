class ProgramInternalForm:

    def __init__(self):
        self._items = []

    def add(self, token, position):
        self._items.append((token, position))

    def __str__(self):
        resultToStr = ""
        for tuple in self._items:
            resultToStr += tuple[0] + "->" + str(tuple[1]) + "\n"
        return resultToStr