# TPC2: Conversor de MD para HTML

## Autor

- Marta Raquel da Silva Rodrigues
- A100743

## Explicação

Este trabalho foi realizado com recurso a libraria *re* com o objetivo de implementar um conversor de markdown para html, assim capaz de converter os seguintes elementos:
- Cabeçalhos
- Bold
- Itálico
- Listas Numeradas
- Links
- Imagens

Foram utilizados os métodos "sub" e "match" da libraria *re*, para detetar e posteriormente substituir as instâncias encontradas para as expressões regulares fornecidas.

Adicionalmente, para se poder saber quando iniciar e terminar uma Lista Numerada, foi instanciada uma *flag* para permitir, assim, a escrita de \<ol> e \</ol>

Este programa recebe um ficheiro .md e cria um ficheiro .html