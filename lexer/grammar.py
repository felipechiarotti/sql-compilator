from enum import Enum

class Grammar(Enum):
    ERR    = -2, #Erro

    #PALAVRAS CHAVE
    INSERT = 300 #Palavra Chave INSERT em caixa alta ou baixa
    UPDATE = 301 #Palavra Chave UPDATE em caixa alta ou baixa
    DELETE = 302 #Palavra Chave DELETE em caixa alta ou baixa
    INTO   = 303 #Palavra Chave INTO em caixa alta ou baixa
    SET    = 304 #Palavra Chave SET em caixa alta ou baixa
    WHERE  = 305 #Palavra Chave WHERE em caixa alta ou baixa
    FROM   = 306 #Palavra Chave FROM em caixa alta ou baixa
    VALUES = 307 #Palavra Chave VALUES em caixa alta ou baixa

    #OUTROS
    EOL    = 500 #Fim de Linha
    OPEN   = 501 #Parenteses Aberto
    CLOSE  = 502 #Parenteses Fechado
    COMMA  = 503 #Virgula
    EQUALS = 504 #Sinal de Igualdade

    #TIPOS
    ID     = 600 #Tipo ID
    STRING = 601 #Tipo String
    NUMBER = 602 #Tipo Number