import json
import sys
import ply.lex as lex
from datetime import date
import math


tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'ADICIONAR',
    'SAIR',
    'SALDO'
]

t_LISTAR = r'LISTAR'

def t_MOEDA(t):
    r'MOEDA[ ]([2e|1e|50c|20c|10c|5c],?)+'
    return t

def t_SELECIONAR(t):
    r'SELECIONAR[ ]\d+'
    return t

def t_ADICIONAR(t):
    r'ADICIONAR[ ][\w-]+[ ]\d([ ]\d+(\.\d+)?)?'
    return t

t_SALDO = r'SALDO'

t_SAIR = r'SAIR'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'

def t_error(t):
    print("Caracter Ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

def calculaTroco(saldo):
    troco = {}
    valores = [2,1,0.5,0.2,0.1,0.05]
    for valor in valores:
        troco[valor] = int(saldo // valor)
        saldo = round(saldo%valor,2)
    return troco

def float_moedas(valor):
    res = ""
    decimal,inteiro = math.modf(valor)
    if inteiro > 0:
        res += f"{int(inteiro)}e"
    if decimal > 0:
        res += f"{int(round(decimal*100,0))}c"
    if not res:
        res = "0e"
    return res



def main():
    with open("stock.json",'r') as ficheiro:
        dados = json.load(ficheiro)
    produtos = dados["stock"]

    items = {} #passa os dados para local para ser mais facil a procuro
    for produto in produtos:
        items[produto['cod']] = produto


    lexer = lex.lex()

    saldo = 0
    data_atual = date.today()

    print(f"maq: {data_atual}, Stock carregado.")
    print("maq: Olá! Estou disponível para atender o seu pedido.")
    for line in sys.stdin:
        lexer.input(line)
        for token in lexer:
            if not token:
                print("maq: Comando inválido.")
            

            if token.type == "LISTAR":
                print("maq:")
                print("""     Número     |            Nome                             |      Quantidade      |   Preço
---------------------------------------------------------------------------------------------------""")
                
                for cod,produto in items.items():
                    print(f"       {cod}        |        {produto['nome']: <30}       |       {produto['quant']}              |    {produto['preco']}")
            

            elif token.type =="MOEDA":
                moedas = token.value.split(" ")[1].split(",")
                for moeda in moedas:
                    if moeda[-1] == "e":
                        saldo += float(moeda[:-1])
                    else:
                        saldo += round(float(moeda[:-1]) /100,2)
                print(f"maq: Saldo = {float_moedas(saldo)}")


            elif token.type == "SALDO":
                print(f"maq: Saldo Disponível = {float_moedas(saldo)}")


            elif token.type == "SELECIONAR":
                id = int(token.value.split(" ")[1])
                if id in items:
                    if(items[id]["quant"]>0):
                        produto = items[id]
                        if saldo >= produto["preco"]:
                            saldo -= produto["preco"]
                            items[id]["quant"] -= 1
                            print(f"maq: Pode retirar o produto dispensado -> {produto['nome']}")
                            print(f"maq: Saldo Disponível = {float_moedas(saldo)}")
                        else:
                            print("maq: Saldo insuficiente para satisfazer o seu pedido")
                            print(f"maq: Saldo = {float_moedas(saldo)}; Pedido = {float_moedas(produto['preco'])}")

                    else:
                        print(f"maq: Produto {id} está fora de stock.")
                else: 
                    print(f"maq: Produto{id} não existe.")


            elif token.type == "SAIR":
                print(f"maq: Troco = {float_moedas(saldo)}")
                troco = calculaTroco(saldo)
                moedas_troco = "maq: Pode retirar o troco:"
                for valor,numero in troco.items():
                    if numero > 0:
                        moedas_troco += f"{numero}x {float_moedas(valor)};"
                print(moedas_troco)
                print("maq: Até à próxima!")
                bd = {}
                bd['stock'] = produtos
                with open("stock.json", 'w') as ficheiro:
                    json.dump(bd, ficheiro, indent=2)
                return


            elif token.type == "ADICIONAR":
                nome = token.value.split(" ")[1]
                quantidade = int(token.value.split(" ")[2])
                adicionado = False
                #adicionar quantidade
                for produto in produtos:
                    if produto["nome"] == nome:
                        produto["quant"] += quantidade
                        adicionado = True
                #novo produto
                if(adicionado == False):
                    if len(token.value.split(" ")) == 4:
                        preco = float(token.value.split(" ")[3])
                        produtos.append({"cod": len(produtos)+1, "nome": nome, "quant": quantidade,"preco": preco})
                    else:
                        print(f"maq: O preço do produto está em falta")

                
                print(f"maq: Adicionado {quantidade} itens ao produto {nome}")



if __name__ == "__main__":
    main()