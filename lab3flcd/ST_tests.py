from Scanner import Scanner
from Symbols import Symbols
from SymbolTable import SymbolTable


def test_SymbolTable():
    table = SymbolTable(5)
    table.add("a")
    table.add("b")
    table.add("c")
    table.add("vlad")
    table.add("lk")
    table.add("test")
    assert table.contains("a")
    table.delete("a")
    assert not table.contains("a")
    assert table.contains("vlad")
    assert table.contains("test")

if __name__ == '__main__':
    sc = Symbols()
    print("separators:", sc.separators)
    print("operators:", sc.operators)
    print("reserved words:", sc.reservedWords)