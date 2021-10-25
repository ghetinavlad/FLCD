from re import *

from Symbols import Symbols


class Scanner:

    def __init__(self):
        self.symbols = Symbols()

    def isIdentifier(self, token) -> bool:
        return match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def isConstant(self, token) -> bool:
        return match(r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None

    def getStringToken(self, line, index):
        token = ''
        quotes = 0
        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1
        return token, index

    def isPartOfOperator(self, char) -> bool:
        for op in self.symbols.operators:
            if char in op:
                return True
        return False

    def getOperatorToken(self, line, index):
        token = ''
        while index < len(line) and self.isPartOfOperator(line[index]):
            token += line[index]
            index += 1
        return token, index

    def getReservedWords(self):
        return self.symbols.reservedWords

    def getOperators(self):
        return self.symbols.separators

    def getSeparators(self):
        return self.symbols.operators

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.isPartOfOperator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.getOperatorToken(line, index)
                tokens.append(token)
                token = ''

            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                print(token)
                tokens.append(token)
                token = ''

            elif line[index] in self.symbols.separators:
                if token:
                    tokens.append(token)
                token = line[index]
                index += 1

                tokens.append(token)
                token = ''

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens
