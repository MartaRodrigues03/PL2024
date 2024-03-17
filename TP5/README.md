# TPC5: Máquina de Vending

## Autor

- Marta Raquel da Silva Rodrigues
- A100743

## Resumo
Com recurso à biblioteca **ply**, foram criados vários tokens para cada opção possível de interação com a máquina de vending:

+ `LISTAR` - lista todos os produtos na máquina;
+ `MOEDA` - adicionar saldo, recebendo várias moedas (por exemplo no formato: MOEDA 1e,50c,5c); 
+ `SELECIONAR` - seleciona um produto para comprar (SELECIONAR 1). Caso tenha saldo suficiente, retira o valor da compra do saldo disponível, caso contrário não permite a compra;
+ `ADICIONAR` - adiciona produtos ao stock da máquina, caso o produto já exista adiciona quantidade ao seu stock, caso contrário passa a ser necessário indicar o preço e um novo produto é adicionado;
+ `SAIR` - sai da máquina e devolve o troco;
+ `SALDO` - exibe o saldo atual disponível.

Cada token tem associado uma expressão regular associada permitindo identificar e classificar corretamente as entradas do utilizador.

Os dados dos produtos são carregados a partir de um ficheiro JSON de seguinte estrutura: Código do produto, nome, quantidade e preço. No final da utilização da máquina os dados deste ficheiro JSON são atualizado para o estado atual da máquina.

Os valores monetários são todos expressos com o seguinte formato: 1e 10c etc