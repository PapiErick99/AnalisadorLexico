# Conjuntos FIRST e FOLLOW da Gramática

## FIRST

| Não-terminal | FIRST                                                   |
|---|---------------------------------------------------------|
| Programa | { INT }                                                 |
| Bloque | { { } }                                                  |
| Cmds | { INT, FLOAT, IDENTIFICADOR, IF, WHILE, DO, FOR, {, ε } |
| Cmd | { INT, FLOAT, IDENTIFICADOR, IF, WHILE, DO, FOR, { }    |
| Declaracao | { INT, FLOAT }                                          |
| Tipo | { INT, FLOAT }                                          |
| ListaIds | { ,, ε }                                                |
| Atribuicao | { IDENTIFICADOR }                                       |
| IfStmt | { IF }                                                  |
| ElsePart | { ELSE, ε }                                             |
| WhileStmt | { WHILE }                                               |
| DoWhileStmt | { DO }                                                  |
| ForStmt | { FOR }                                                 |
| AtribFor | { IDENTIFICADOR }                                       |
| Condicao | { !, IDENTIFICADOR, NUMERO, ( }                         |
| CondicaoL | {                                                       ||, ε } |
| CondTermo | { !, IDENTIFICADOR, NUMERO, ( }                         |
| CondTermoL | { &&, ε }                                               |
| CondFator | { !, IDENTIFICADOR, NUMERO, ( }                         |
| OpRel | { ==, !=, <=, >=, <, > }                                |
| Exp | { IDENTIFICADOR, NUMERO, ( }                            |
| ExpL | { +, -, ε }                                             |
| Termo | { IDENTIFICADOR, NUMERO, ( }                            |
| TermoL | { *, /, ε }                                             |
| Fator | { IDENTIFICADOR, NUMERO, ( }                            |

## FOLLOW

| Não-terminal | FOLLOW |
|---|---|
| Programa | { $ } |
| Bloque | { $, INT, FLOAT, IDENTIFICADOR, IF, WHILE, DO, FOR, {, } } |
| Cmds | { } } |
| Cmd | { INT, FLOAT, IDENTIFICADOR, IF, WHILE, DO, FOR, {, }, ELSE } |
| Declaracao | igual a FOLLOW(Cmd) |
| Tipo | { IDENTIFICADOR } |
| ListaIds | { ; } |
| Atribuicao | igual a FOLLOW(Cmd) |
| IfStmt | igual a FOLLOW(Cmd) |
| ElsePart | igual a FOLLOW(IfStmt) |
| WhileStmt | igual a FOLLOW(Cmd) |
| DoWhileStmt | igual a FOLLOW(Cmd) |
| ForStmt | igual a FOLLOW(Cmd) |
| AtribFor | { ;, ) } |
| Condicao | { ), ; } |
| CondicaoL | { ), ; } |
| CondTermo | { ||, ), ; } |
| CondTermoL | { ||, ), ; } |
| CondFator | { &&, ||, ), ; } |
| OpRel | { IDENTIFICADOR, NUMERO, ( } |
| Exp | { ;, ), ==, !=, <=, >=, <, >, &&, || } |
| ExpL | igual a FOLLOW(Exp) |
| Termo | { +, -, ;, ), ==, !=, <=, >=, <, > } |
| TermoL | igual a FOLLOW(Termo) |
| Fator | { *, /, +, -, ;, ), ==, !=, <=, >=, <, > } |
