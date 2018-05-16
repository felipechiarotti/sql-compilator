class Token(object):
    def __init__(self):
        self.value = 0
        self.type = -1

    def get_token(self):
        return self.type, self.value

    def set_type(self,type):
        self.type = type

    def set_value(self,value):
        self.value = value