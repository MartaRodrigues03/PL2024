import sys

def ler_ficheiro():
    modalidades = set()
    aptos = 0
    inaptos = 0
    n_atletas = 0
    distribuicoes = {}

    next(sys.stdin) #ignora a primeira linha

    for linha in sys.stdin:
        n_atletas += 1
        parametros = linha.strip().split(',')
        #Coloca todas as modalidades numa lista
        modalidades.add(parametros[8])
        #Apto ou não apto
        if(parametros[12] == "true"):
            aptos +=1
        else: inaptos += 1
        #Fazer Distribuição -> resultado é o número de atletas e o nomes de todos
        escalao = int(parametros[5]) // 5 * 5
        nome = parametros[3] + ' ' + parametros[4]
        if escalao not in distribuicoes.keys():
            #distribuicoes[escalao] = 1
            distribuicoes[escalao] = (1, [nome])
        else:
            #total = distribuicoes[escalao]
            #distribuicoes[escalao] = total + 1
            total,nomes = distribuicoes[escalao]
            distribuicoes[escalao] = (total + 1, nomes + [nome])

    #Ordena a lista das modalidades por ordem alfabética
    modalidadessorted = sorted(modalidades)

    #Calcula as percentagens de atletas aptos e inaptos
    percAptos = aptos / n_atletas * 100
    percInaptos = inaptos / n_atletas * 100

    return modalidadessorted, percAptos, percInaptos, distribuicoes


def main():
    modalidades,aptos,inaptos,distribuicao = ler_ficheiro()

    print("Modalidades Desportivas Ordenadas: \n", modalidades)

    print("\nPercentagem de Atletas Aptos: \n", aptos)
    print("Percentagem de Atletas Inaptos: \n", inaptos)

    print("\nDistribuição de Atletas por Escalão: ")
    for i in range(0,100,5):
        if i in distribuicao:
            print(f"[{i}-{i+4}]:", distribuicao[i], "\n")



if __name__ == "__main__": 
    main()