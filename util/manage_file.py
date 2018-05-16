class ManageFile:
    def __init__(self,filename):
        self.analise_file = filename
        self.line_number = 1 #Linha do Arquivo
        self.char_pos = 0 #Posição do Caractere na linha atual

    @staticmethod
    #Pega o proximo caractere do arquivo
    def get_next_file_char(self):
        return self.analise_file.read()

    #Retorna a posição do caractere na linha
    def get_char_pos(self):
        return char_pos

    #Retorna o numero da linha
    def get_line_number(self):
        return line_number
    
    @staticmethod
    def update_data_file(self, char):
        if(char == '\n'):
            self.line_number = self.line_number + 1
            self.char_pos = 0
        else:
            self.char_pos = self.char_pos + 1