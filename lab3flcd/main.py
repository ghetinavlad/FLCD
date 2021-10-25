from ProgramInternalForm import ProgramInternalForm
from Scanner import Scanner
from SymbolTable import SymbolTable
from re import *

class ScannerResult:

    def __init__(self):
        self.ST = SymbolTable(7)
        self.PIF = ProgramInternalForm()
        self.scanner = Scanner()
        self.cases = ["=+", "<+", ">+", "<=+", ">=+", "==+", "!=+", "=-", "<-", ">-", "<=-", ">=-", "==-", "!=-"]

    def compute_results(self, file_name: str):
        exceptionMessage = ""
        reserved_words = self.scanner.getReservedWords()
        separators = self.scanner.getSeparators()
        operators = self.scanner.getOperators()

        with open(file_name, 'r') as file:
            line_counter = 0
            for line in file:
                line_counter += 1
                tokens = self.scanner.tokenize(line.strip())
                extra = ''
                for i in range(len(tokens)):
                    if tokens[i] in reserved_words + separators + operators:
                        if tokens[i] == ' ':
                            continue
                        self.PIF.add(tokens[i], 0)
                    elif tokens[i] in self.cases and i < len(tokens) - 1:
                        if match("[1-9]", tokens[i + 1]):
                            self.PIF.add(tokens[i][:-1], 0)
                            extra = tokens[i][-1]
                            continue
                        else:
                            exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                                line_counter) + "\n"
                    elif self.scanner.isIdentifier(tokens[i]):
                        id = self.ST.add(tokens[i])
                        print("id", id)
                        self.PIF.add("id", id)
                    elif self.scanner.isConstant(tokens[i]):
                        const = self.ST.add(extra + tokens[i])
                        extra = ''
                        print("const", const)
                        self.PIF.add("const", const)
                    else:
                        exceptionMessage += 'Lexical error at token ' + tokens[i] + ', at line ' + str(
                            line_counter) + "\n"

        with open('st.out', 'w') as writer:
            writer.write(str(self.ST))
        with open('pif.out', 'w') as writer:
            writer.write(str(self.PIF))
        if exceptionMessage == '':
            print("Lexically correct")
        else:
            print(exceptionMessage)

if __name__ == '__main__':
    scanner_result = ScannerResult()
    scanner_result.compute_results("p1err.txt")

    # scanner = Scanner()
    # line = "println('is prime');"
    # print(line)
    # tokens = scanner.get_tokens(line)
    # print(tokens)