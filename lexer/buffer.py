class Buffer:
    def __init__(self):
        self.buffer_size = 256 #Tamanho do Buffer
        self.buffer = [] # Buffer
        self.buffer_control = 0 #Quantidade de caracteres no buffer
        self.read_buffer_pos = 0 #Quantidade de caracteres lidos no buffer

    #Esvazia o Buffer
    def empty_buffer(self):
        self.buffer = []
        self.buffer_control = 0
        self.read_buffer_pos = 0
    
    #Preenche o Buffer
    def fill_buffer(self):
        next_char = ManageFile.get_next_file_char()
        while buffer_control < buffer_size:
            if(not next_char):
                return Grammar.ERR
            buffer.append(next_char)
            next_char = ManageFile.get_next_file_char()

    #Retorna o proximo char do buffer
    def next_buffer_char(self):
        if(self.read_buffer_pos < self.buffer_size):
            read_char = self.buffer[self.read_buffer_pos]
            ManageFile.update_data_file(read_char)
            return read_char
        else:
            return '\\'
    #Volta a fita do buffer
    def rollback(self):
        if(self.read_buffer_pos > 0):
            self.read_buffer_pos = self.read_buffer_pos - 1

    #Verifica se o buffer foi inteiro lido e reenche o mesmo
    def verify_buffer(self):
        while(True):
            if(self.read_buffer_pos == self.buffer_size):
                self.empty_buffer()
                if(self.fill_buffer() == Grammar.ERR):
                    break

