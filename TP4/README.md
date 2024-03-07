# TPC4: Analisador Léxico

## Autor

- Marta Raquel da Silva Rodrigues
- A100743

## Resumo
Com recurso à biblioteca **ply**, foi desenvolvido um analisador léxico de uma expressão (recebida no *stdin*), capaz de identificar os seguintes tokens:

- Comandos SQL: `SELECT`, `FROM` e `WHERE`;
- Nomes de objetos/atributos das tables;
- Números;
- Delimitadores: `,` e `;`
- Operadores matemáticos: `>=`,`<=`,`=`,`<`,`>`,`+`,`-`,`*`;