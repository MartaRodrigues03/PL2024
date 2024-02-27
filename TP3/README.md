# TPC3: Somador on/off

## Autor

- Marta Raquel da Silva Rodrigues
- A100743

## Resumo

- O ficheiro texto é lido linha a linha através da função *sys.stdin*, e, com recurso à libraria **re**, através de uma expressão regular é feita a captura das ocorrências de "on", "off", "=" e de sequências de digitos presentes em cada linha;
- Visto que deve ser possível detetar "on" e "off" em qualquer combinação de maiusculas e minusculas, na captura é utilizada a flag *re.IGNORECASE*. Esta permite identificar as ocorrências dessas mesmas com qualquer combinação possivel de maiusculas e minusculas;
- É instanciada uma flag auxiliar (on), que se ativa quando se encontra uma ocorrência de "on" e desativa assim que encontrar "off", ligando e desligando a soma;
- Se a flag estiver ativada, adiciona-se a sequência de digitos à soma total até ao momento;
- Quando ocorre "=" o resultado atual da soma é imprimido na saída.