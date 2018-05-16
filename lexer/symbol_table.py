class SymbolTable(object):
    def __init__(self):
        self.symbols = []

    def add_symbol(self,symbol):
        for key, symb in enumerate(self.symbols):
            if symb.lexem == symbol.lexem:
                return key
        self.symbols.append(symbol)
        return len(self.symbols)-1