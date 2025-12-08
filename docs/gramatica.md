# Gramática Livre de Contexto - LL(1)
**Disciplina:** Compiladores  
**Status:** Atualizada com todos os tokens definidos (Lógica e Aritmética).

## 1. Definição Formal
$G = (V, T, P, S)$

### Símbolo Inicial (S)
* `Programa`

### Terminais (T) - Baseado em TOKEN_DEFINICOES
* **Ignorados:** `COMENTARIO`, `ESPACO` (Não aparecem na gramática)
* **Palavras Chave:** `IF`, `ELSE`, `FOR`, `WHILE`, `DO`, `INT`, `FLOAT`, `MAIN`
* **Literais/IDs:** `IDENTIFICADOR` (ex: &abc), `NUMERO`
* **Lógicos:** `&&`, `||`, `!`
* **Relacionais:** `==`, `!=`, `<=`, `>=` , `<`, `>`
* **Aritméticos:** `=`, `+`, `-`, `*`, `/`
* **Delimitadores:** `(`, `)`, `{`, `}`, `;`, `,`

### Não-Terminais (V)
`Programa`, `Bloque`, `Cmds`, `Cmd`, `Declaracao`, `Tipo`, `ListaIds`, `Atribuicao`, `IfStmt`, `ElsePart`, `WhileStmt`, `DoWhileStmt`, `ForStmt`, `AtribFor`, `Exp`, `ExpL`, `Termo`, `TermoL`, `Fator`, `Condicao`, `CondicaoL`, `CondTermo`, `CondTermoL`, `CondFator`, `OpRel`.

---

## 2. Regras de Produção (P)

### 2.1 Estrutura Geral
```ebnf
<Programa>      ::= INT MAIN "(" ")" <Bloque>

<Bloque>        ::= "{" <Cmds> "}"

<Cmds>          ::= <Cmd> <Cmds>
                  | ε
                  
<!-- Comandos (Statements) -->

<Cmd>           ::= <Declaracao>
                  | <Atribuicao>
                  | <IfStmt>
                  | <WhileStmt>
                  | <DoWhileStmt>
                  | <ForStmt>
                  | <Bloque>

<Declaracao>    ::= <Tipo> IDENTIFICADOR <ListaIds> ";"

<Tipo>          ::= INT
                  | FLOAT

<ListaIds>      ::= "," IDENTIFICADOR <ListaIds>
                  | ε

<Atribuicao>    ::= IDENTIFICADOR "=" <Exp> ";"

<!-- Estruturas de controle -->

<IfStmt>        ::= IF "(" <Condicao> ")" <Cmd> <ElsePart>

<ElsePart>      ::= ELSE <Cmd>
                  | ε

<WhileStmt>     ::= WHILE "(" <Condicao> ")" <Cmd>

<DoWhileStmt>   ::= DO <Bloque> WHILE "(" <Condicao> ")" ";"

<ForStmt>       ::= FOR "(" <AtribFor> ";" <Condicao> ";" <AtribFor> ")" <Cmd>

<AtribFor>      ::= IDENTIFICADOR "=" <Exp>

<Condicao>      ::= <CondTermo> <CondicaoL>

<!-- Lógica Booleana (Hierarquia LL1) -->

<CondicaoL>     ::= "||" <CondTermo> <CondicaoL>
                  | ε

<CondTermo>     ::= <CondFator> <CondTermoL>

<CondTermoL>    ::= "&&" <CondFator> <CondTermoL>
                  | ε

<CondFator>     ::= "!" <CondFator>
                  | <Exp> <OpRel> <Exp>

<OpRel>         ::= "==" 
                  | "!=" 
                  | "<=" 
                  | ">="
                  | "<" 
                  | ">"

<Exp>           ::= <Termo> <ExpL>

<!-- Expressões Aritméticas -->

<ExpL>          ::= "+" <Termo> <ExpL>
                  | "-" <Termo> <ExpL>
                  | ε

<Termo>         ::= <Fator> <TermoL>

<TermoL>        ::= "*" <Fator> <TermoL>
                  | "/" <Fator> <TermoL>
                  | ε

<Fator>         ::= IDENTIFICADOR
                  | NUMERO
                  | "(" <Exp> ")"


### Verificación de Tokens Utilizados

1.  **Ignorados:** `COMENTARIO`, `ESPACO` (Manejados por el Lexer, no la gramática).
2.  **Palabras Clave:** Todas usadas en `2.1`, `2.2` y `2.3`.
3.  **Identificadores/Números:** Usados en `Declaracao`, `Fator` (Exp) y `Atribuicao`.
4.  **Lógicos (&&, ||, !):**
    * `||` -> Usado en `<CondicaoL>`
    * `&&` -> Usado en `<CondTermoL>`
    * `!` -> Usado en `<CondFator>`
5.  **Relacionales (==, !=, <=, >=, <, >):** Todos agrupados en `<OpRel>`.
6.  **Operadores (+, -, *, /, =):** Usados en `<ExpL>`, `<TermoL>` y `<Atribuicao>`.
7.  **Delimitadores:**
    * `{ }` -> En `<Bloque>`
    * `( )` -> En `<IfStmt>`, `<Fator>`, etc.
    * `;` -> Final de sentencias.
    * `,` -> En `<ListaIds>`.