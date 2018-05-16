from lexer.symbol_table import SymbolTable
from lexer.token import Token
from lexer.grammar import Grammar
from lexer.symbol import Symbol
from lexer.buffer import Buffer
import threading
class Lexer:
    def __init__(self):
        self.char_peek = ' '
        self.symbol_table = SymbolTable()
        self.buffer = [Buffer(), Buffer()]
        self.active_buffer = 0
        for buffer in self.buffer:
            thread = threading.Thread(target=buffer.verify_buffer)
            thread.start()
    
    #Alterna entre os buffers
    def next_buffer():
        if(len(self.buffer)-1 == self.active_buffer):
            self.active_buffer = 0
        else
            self.active_buffer = self.active_buffer + 1
    
    #Retorna um Token 
    def next_token(self):
         token = Token()
         peek = self.buffer[self.active_buffer].next_buffer_char()
         while(peek == ' ' or peek == '\n'):
            peek = self.buffer[self.active_buffer].next_buffer_char()

        if(peek == '+' or peek == '-' or peek.isdigit()):
            result = peek
            decimal = 0
            peek = self.buffer[self.active_buffer].next_buffer_char()
            if(result == '+' or result == '-'):
                if(peek.isdigit()):
                    result = result + str(peek)
                    peek = self.buffer[self.active_buffer].next_buffer_char()
                    while(peek.isdigit() or (peek == '.' and decimal = 0)):
                        if(peek == '.'):
                            decimal = 1
                            result = result + peek
                        else:
                            result = result + str(peek)
                        peek = self.buffer[self.active_buffer].next_buffer_char()
            self.buffer[self.active_buffer].rollback()

            symbol = Symbol(Grammar.NUMBER, result)
            token.set_type(Grammar.NUMBER)
            token.value = self.symbol_table.add_symbol(symbol)
        elif (peek == "'"):
            string = peek
            peek = self.buffer[self.active_buffer].next_buffer_char()
            while(peek != "'"):
                string = string + str(peek)
                peek = self.buffer[self.active_buffer].next_buffer_char()
            self.buffer[self.active_buffer].rollback()
            symbol = Symbol(Grammar.STRING, string)
            token.set_type(Grammar.STRING)
            token.set_value = self.symbol_table.add_symbol(symbol)
        elif (peek == ';'):
            token.set_type(Grammar.EOL)
            token.set_value = 0
        elif (peek == ','):
            token.set_type(Grammar.COMMA)
            token.set_value = 0
        elif (peek == '='):
            token.set_type(Grammar.EQUALS)
            token.set_value = 0         
        elif (peek == '('):
            token.set_type(Grammar.OPEN)
            token.set_value = 0     
        elif (peek == ')'):
            token.set_type(Grammar.CLOSE)
            token.set_value = 0         
        elif (peek.isalpha()):
            string = peek
            peek = self.buffer[self.active_buffer].next_buffer_char()
            if(lower(peek) == 'i'):
                string = string + peek
                peek = self.buffer[self.active_buffer].next_buffer_char()
                if(lower(peek) == 'n'):
                    string = string + peek
                    peek = self.buffer[self.active_buffer].next_buffer_char()
                    if(lower(peek) == 's'):
                        string = string + peek
                        peek = self.buffer[self.active_buffer].next_buffer_char()
                        if(lower(peek) == 'e'):
                            string = string + peek
                            peek = self.buffer[self.active_buffer].next_buffer_char()
                            if(lower(peek) == 'r'):
                                string = string + peek
                                peek = self.buffer[self.active_buffer].next_buffer_char()
                                if(lower(peek) == 't'):
                                    string = string + peek
                                    peek = self.buffer[self.active_buffer].next_buffer_char()
                                    if(peek != ' '):
                                        string = string + peek
                                        peek = self.buffer[self.active_buffer].next_buffer_char()     
                                        while(peek != ' '):
                                            string = string + peek
                                            peek = self.buffer[self.active_buffer].next_buffer_char()   
                                        symbol = Symbol(Grammar.ID, string)
                                        token.set_type(Grammar.ID)
                                        token.value = self.symbol_table.add_symbol(symbol)                                         
                                    else:
                                        token.set_type(Grammar.INSERT)
                                        token.value = 0
                    elif(lower(peek) == 't'):
                        string = string + peek
                        peek = self.buffer[self.active_buffer].next_buffer_char()
                        if(lower(peek) == 'o'):
                            string = string + peek
                            peek = self.buffer[self.active_buffer].next_buffer_char()
                                if(peek != ' '):
                                    string = string + peek
                                    peek = self.buffer[self.active_buffer].next_buffer_char()     
                                    while(peek != ' '):
                                        string = string + peek
                                        peek = self.buffer[self.active_buffer].next_buffer_char()   
                                        symbol = Symbol(Grammar.ID, string)
                                        token.set_type(Grammar.ID)
                                        token.value = self.symbol_table.add_symbol(symbol)                                         
                                    else:
                                        token.set_type(Grammar.INTO)
                                        token.value = 0
            elif(lower(peek) == 'u'):        
                string = string + peek
                peek = self.buffer[self.active_buffer].next_buffer_char()
                if(lower(peek) == 'p'):
                    string = string + peek
                    peek = self.buffer[self.active_buffer].next_buffer_char()
                    if(lower(peek) == 'd'):
                        string = string + peek
                        peek = self.buffer[self.active_buffer].next_buffer_char()
                        if(lower(peek) == 'a'):
                            string = string + peek
                            peek = self.buffer[self.active_buffer].next_buffer_char()
                            if(lower(peek) == 't'):
                                string = string + peek
                                peek = self.buffer[self.active_buffer].next_buffer_char()
                                if(lower(peek) == 'e'):
                                    string = string + peek
                                    peek = self.buffer[self.active_buffer].next_buffer_char()
        # if(len(self.line_data) > 0):
        #     peek = self.next_char()
        #     while (peek == ' ' and len(self.line_data) > 0):
        #         peek = self.next_char()
        #     while(peek == '\n' and len(self.line_data) > 0):
        #         peek = self.next_char()
        #     if str(peek).isdigit():
        #         sum = peek
        #         peek = self.next_char()
        #         while peek.isdigit():
        #             sum = (int(sum) * 10) + int(peek)
        #             peek = self.next_char()
        #         self.char_pos = self.char_pos - 1
        #         token.set_type(Grammar.NUM.value)
        #         token.set_value(sum)
        #     elif peek == '$':
        #         peek = self.next_char()
        #         aux_string = ''
        #         while peek.isalpha():
        #             aux_string = aux_string + peek
        #             peek = self.next_char()
        #         self.char_pos = self.char_pos - 1
        #         token.set_type(Grammar.VAR.value)
        #         token.set_value(self.symbol_table.add_symbol( Symbol(Grammar.VAR.value,0,aux_string,False) ))
        #     elif str(peek).isalpha():
        #         reserved_keyword = ''
        #         while str(peek).isalpha():
        #             reserved_keyword = reserved_keyword + str(peek)
        #             peek = self.next_char()
        #         self.char_pos = self.char_pos - 1
        #         if(reserved_keyword == "print"):
        #             s_type = Grammar.PRINT.value
        #             token.set_type(Grammar.PRINT.value)
        #         else:
        #             return token

        #         symbol = Symbol(s_type,0,reserved_keyword,True)
        #         token.value = self.symbol_table.add_symbol(symbol)
        #     elif peek == '+':
        #         token.type = Grammar.PLUS.value
        #         token.value = 0
        #     elif peek == '=':
        #         token.type = Grammar.EQUALS.value
        #         token.value = 0
        #     elif peek == ';':
        #         token.type = Grammar.EOL.value
        #         token.value = 0
        # return token

