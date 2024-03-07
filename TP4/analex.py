import ply.lex as lex
import sys

reserved = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE'
}

tokens = [
    'COMANDO', #SELECT
    'OPERADOR_MAT', #> =
    'ATRIBUTO', #id; salario
    'DELIMITADOR', #,
    'NUMERO', #820
    'DELIMITADOR_FINAL' #;
] + list(reserved.values())

t_NUMERO = r'\d+'

t_DELIMITADOR = r','

t_DELIMITADOR_FINAL = r';'

def t_COMANDO(t):
    r'\b[A-Za-z]+\b'
    if(reserved.get(t.value.lower())):
        t.type= "COMANDO"
    else:
        t.type = "ATRIBUTO"
    return t

t_OPERADOR_MAT = r'>=|<=|=|<|>|\+|-|\*'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0]) 
    t.lexer.skip(1)

lexer = lex.lex()

def main():
    for linha in sys.stdin:
        lexer = lex.lex()
        lexer.input(linha)
        for token in lexer:
            print(token)


if __name__ == '__main__':
    main()