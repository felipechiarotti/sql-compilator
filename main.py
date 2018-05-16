from lexer.lexer import Lexer
from util.manage_file import ManageFile
import sys

file = ManageFile(sys.argv[1])
lexer = Lexer()
run(lexer)

def run(lexer)
    token = lexer.next_token()
    token_list = []
    while(token != Grammar.ERR):
        token_list.append(token)
        token = lexer.next_token()