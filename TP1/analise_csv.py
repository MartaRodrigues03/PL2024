import sys

#Ler o dataset, processá-lo e criar os seguintes resultados:
    #Lista ordenada alfabeticamente das modalidades desportivas;
    #Percentagens de atletas aptos e inaptos para a prática desportiva;
    #Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...



def ler_ficheiro(nome_ficheiro):
    modalidades = set()
    aptos = 0
    inaptos = 0
    n_atletas = 0
    distribuicoes = {}

    with open(nome_ficheiro,'r') as ficheiro:
        next(ficheiro) #ignora a primeira linha

        for linha in ficheiro:
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
    



def main(args):
    modalidades,aptos,inaptos,distribuicao = ler_ficheiro(args[1])

    print("Modalidades Desportivas Ordenadas: \n", modalidades)

    print("\nPercentagem de atletas aptos: ", aptos)
    print("Percentagem de atletas inaptos: ", inaptos)

    print("\nDistribuição de atletas por escalão: ")
    for i in range(0,100,5):
        if i in distribuicao:
            print(f"[{i}-{i+4}]:", distribuicao[i], "\n")



if __name__ == "__main__": 
    main(sys.argv)