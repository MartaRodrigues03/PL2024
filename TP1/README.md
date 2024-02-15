# TPC1: Análise de um dataset

## Autor

- Marta Raquel da Silva Rodrigues
- A100743

## Explicação

- A leitura do ficheiro csv, sem usar o módulo CSV, é feita apartir do uso da libraria *sys*, utilizando assim sys.stdin para ler linha a linha do ficheiro fornecido no comando "cat emd.csv | python3 analise_csv.py";
- Para cada linha, é feito o parsing dos diferentes parametros de cada atleta;
- **Lista ordenadada alfabeticamente das modalidades desportivas:** Ao percorrer as linhas, as modalidades identificadas são colocadas num *set*, para evitar armazenar modalidades repetidas. No final, ordena-se esta lista por ordem alfabética;
- **Percentagem de atletas aptos e inaptos para a prática desportiva:** são criadas duas variáveis auxiliares *apto* e *inapto*, e consoante o último parametro de um atleta, essas variaveis são incrementadas. Por último, são calculadas as percentagens pretendidas tendo em conta o número total de atletas no csv e as variáveis criadas previamente;
- **Distribuição de atletas por escalão etário:** Inicialmente, é criado um dicionário *distribuicoes* cuja chave é calculada através da função "idade // 5 * 5", permitindo dividir os escalões em intervalos de 5 anos e agrupar os atletas pelas suas idades. Para cada distribuição, é armazenado um tuplo com o número de atletas em cada escalão e uma lista com nomes dos que pertencem a esse escalão. O resultado devolve, assim, o número de atletas numa certa faixa etária, a percentagem de atletas em cada uma dessas mesmas faixas e por último a lista de nomes desses mesmos atletas.