# 1.2.1 - Definir e descrever os tokens que serão atendidos na Linguagem;

### Palavras Reservadas
| Lexema | Token   | Descrição                          |
| -------- | ------- | ---------------------------------- |
| `if`     | `IF`    | Início de um bloco condicional     |
| `else`   | `ELSE`  | Ramo alternativo do condicional    |
| `for`    | `FOR`   | Estrutura de repetição contada     |
| `while`  | `WHILE` | Estrutura de repetição condicional |
| `do`     | `DO`    | Estrutura de repetição *do-while*  |
| `int`    | `INT`   | Tipo de dado inteiro               |
| `float`  | `FLOAT` | Tipo de dado ponto flutuante       |
| `main`   | `MAIN`  | Ponto de entrada do programa       |

# 1.2.1 - Especificar os tokens da linguagem usando as expressões regulares;

### Literais e Identificadores
| Lexema                 | Token           | Descrição                                                  |
| ------------------------ | --------------- | ---------------------------------------------------------- |
| `[0-9]+`                 | `NUMERO`        | Números inteiros decimais                                  |
| `&[a-zA-Z][a-zA-Z0-9_]*` | `IDENTIFICADOR` | Identificadores que devem começar obrigatoriamente com `&` |

### Operadores Lógicos
| Lexema | Token        | Descrição               |             |                         |
| -------- | ------------ | ----------------------- | ----------- | ----------------------- |
| `&&`     | `&&`   | Operador lógico E (AND) |             |                         |
| `        |              | `                       | `OU_LOGICO` | Operador lógico OU (OR) |
| `!`      | `!` | Negação lógica (NOT)    |             |                         |


### Operadores Relacionais
| Lexema | Token         | Descrição      |
| -------- | ------------- | -------------- |
| `==`     | `==` | Igualdade      |
| `!=`     | `!=`   | Diferença      |
| `<`      | `<`       | Menor que      |
| `<=`     | `<=` | Menor ou igual |
| `>`      | `>`       | Maior que      |
| `>=`     | `>=` | Maior ou igual |

### Operadores Aritméticos e Atribuição
| Lexema | Token           | Descrição     |
| -------- | --------------- | ------------- |
| `=`      | `=`         | Atribuição    |
| `+`      | `+`          | Soma          |
| `-`      | `-`         | Subtração     |
| `*`      | `*` | Multiplicação |
| `/`      | `/`       | Divisão       |

### Delimitadores e Pontuação
| Lexema | Token           | Descrição          |
| -------- | --------------- | ------------------ |
| `(`      | `(` | Parêntese esquerdo |
| `)`      | `)` | Parêntese direito  |
| `{`      | `{`     | Chave esquerda     |
| `}`      | `}`     | Chave direita      |
| `;`      | `;` | Ponto e vírgula    |
| `,`      | `,`       | Vírgula            |


### Tokens Ignorados
| Lexema | Token        | Descrição                                         |
| -------- | ------------ | ------------------------------------------------- |
| `// ...` | `//` | Comentário de linha, ignorado pelo analisador     |
| `\s+`    | `\s`     | Espaços, tabulações e quebras de linha, ignorados |





# 1.2.1 - Apresentar o reconhecimento dos tokens da linguagem por meio de AFD;
* Não foi feita

# 1.2.2 - Apresentar o reconhecimento dos tokens da linguagem por meio de AFD;

![Automato](docs/AFD.jpeg)


------
------

# Gramática Livre de Contexto - LL(1)
## 1. Definição Formal
$G = (V, T, P, S)$

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
```
----

## Conjuntos FIRST e FOLLOW da Gramática


### FIRST

| Não-terminal | FIRST |
|---|---|
| Programa | { INT } |
| Bloque | { { } |
| Cmds | { INT, FLOAT, IDENTIFICADOR, IF, WHILE, DO, FOR, {, ε } |
| Cmd | { INT, FLOAT, IDENTIFICADOR, IF, WHILE, DO, FOR, { } |
| Declaracao | { INT, FLOAT } |
| Tipo | { INT, FLOAT } |
| ListaIds | { ,, ε } |
| Atribuicao | { IDENTIFICADOR } |
| IfStmt | { IF } |
| ElsePart | { ELSE, ε } |
| WhileStmt | { WHILE } |
| DoWhileStmt | { DO } |
| ForStmt | { FOR } |
| AtribFor | { IDENTIFICADOR } |
| Condicao | { !, IDENTIFICADOR, NUMERO, ( } |
| CondicaoL | { ||, ε } |
| CondTermo | { !, IDENTIFICADOR, NUMERO, ( } |
| CondTermoL | { &&, ε } |
| CondFator | { !, IDENTIFICADOR, NUMERO, ( } |
| OpRel | { ==, !=, <=, >=, <, > } |
| Exp | { IDENTIFICADOR, NUMERO, ( } |
| ExpL | { +, -, ε } |
| Termo | { IDENTIFICADOR, NUMERO, ( } |
| TermoL | { *, /, ε } |
| Fator | { IDENTIFICADOR, NUMERO, ( } |

### FOLLOW

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


---

# Tabela Sintática - Analisador Descendente Preditivo LL(1)

A tabela abaixo define as regras de produção a serem empilhadas com base no **Não-Terminal** (topo da pilha) e no **Token de Entrada**.

**Legenda:**
* **ε (Epsilon):** Produção vazia (deve-se desempilhar o não-terminal sem consumir entrada).
* **Células Vazias:** Representam **Erro Sintático**.

## 1. Estrutura Geral e Blocos

| Não-Terminal (Topo) | Token (Entrada) | Produção a Empilhar |
| :--- | :--- | :--- |
| `<Programa>` | `INT` | `INT MAIN "(" ")" <Bloque>` |
| `<Bloque>` | `{` | `"{" <Cmds> "}"` |
| `<Cmds>` | `INT`, `FLOAT` | `<Cmd> <Cmds>` |
| `<Cmds>` | `IDENTIFICADOR` | `<Cmd> <Cmds>` |
| `<Cmds>` | `IF`, `WHILE`, `DO`, `FOR` | `<Cmd> <Cmds>` |
| `<Cmds>` | `{` | `<Cmd> <Cmds>` |
| `<Cmds>` | `}` | **ε** |

## 2. Comandos e Declarações

| Não-Terminal (Topo) | Token (Entrada) | Produção a Empilhar |
| :--- | :--- | :--- |
| `<Cmd>` | `INT`, `FLOAT` | `<Declaracao>` |
| `<Cmd>` | `IDENTIFICADOR` | `<Atribuicao>` |
| `<Cmd>` | `IF` | `<IfStmt>` |
| `<Cmd>` | `WHILE` | `<WhileStmt>` |
| `<Cmd>` | `DO` | `<DoWhileStmt>` |
| `<Cmd>` | `FOR` | `<ForStmt>` |
| `<Cmd>` | `{` | `<Bloque>` |
| `<Declaracao>`| `INT`, `FLOAT` | `<Tipo> IDENTIFICADOR <ListaIds> ";"` |
| `<Tipo>` | `INT` | `INT` |
| `<Tipo>` | `FLOAT` | `FLOAT` |
| `<ListaIds>` | `,` | `"," IDENTIFICADOR <ListaIds>` |
| `<ListaIds>` | `;` | **ε** |
| `<Atribuicao>`| `IDENTIFICADOR` | `IDENTIFICADOR "=" <Exp> ";"` |

## 3. Estruturas de Controle

| Não-Terminal (Topo) | Token (Entrada) | Produção a Empilhar |
| :--- | :--- | :--- |
| `<IfStmt>` | `IF` | `IF "(" <Condicao> ")" <Cmd> <ElsePart>` |
| `<ElsePart>` | `ELSE` | `ELSE <Cmd>` |
| `<ElsePart>` | `INT`, `FLOAT`, `IDENTIFICADOR`, `IF`, `WHILE`, `DO`, `FOR`, `{`, `}` | **ε** |
| `<WhileStmt>` | `WHILE` | `WHILE "(" <Condicao> ")" <Cmd>` |
| `<DoWhileStmt>`| `DO` | `DO <Bloque> WHILE "(" <Condicao> ")" ";"` |
| `<ForStmt>` | `FOR` | `FOR "(" <AtribFor> ";" <Condicao> ";" <AtribFor> ")" <Cmd>` |
| `<AtribFor>` | `IDENTIFICADOR` | `IDENTIFICADOR "=" <Exp>` |


## 4. Lógica Booleana (Condições)

| Não-Terminal (Topo) | Token (Entrada) | Produção a Empilhar |
| :--- | :--- | :--- |
| `<Condicao>` | `!`, `IDENTIFICADOR`, `NUMERO`, `(` | `<CondTermo> <CondicaoL>` |
| `<CondicaoL>` | `\|\|` | `"||" <CondTermo> <CondicaoL>` |
| `<CondicaoL>` | `)`, `;` | **ε** |
| `<CondTermo>` | `!`, `IDENTIFICADOR`, `NUMERO`, `(` | `<CondFator> <CondTermoL>` |
| `<CondTermoL>`| `&&` | `"&&" <CondFator> <CondTermoL>` |
| `<CondTermoL>`| `\|\|`, `)`, `;` | **ε** |
| `<CondFator>` | `!` | `"!" <CondFator>` |
| `<CondFator>` | `IDENTIFICADOR`, `NUMERO`, `(` | `<Exp> <OpRel> <Exp>` |
| `<OpRel>` | `==`, `!=`, `<=`, `>=`, `<`, `>` | *(Consumir o respectivo operador)* |

## 5. Expressões Aritméticas

| Não-Terminal (Topo) | Token (Entrada) | Produção a Empilhar |
| :--- | :--- | :--- |
| `<Exp>` | `IDENTIFICADOR`, `NUMERO`, `(` | `<Termo> <ExpL>` |
| `<ExpL>` | `+` | `"+" <Termo> <ExpL>` |
| `<ExpL>` | `-` | `"-" <Termo> <ExpL>` |
| `<ExpL>` | `;`, `)`, `OpRel`, `&&`, `\|\|` | **ε** |
| `<Termo>` | `IDENTIFICADOR`, `NUMERO`, `(` | `<Fator> <TermoL>` |
| `<TermoL>` | `*` | `"* " <Fator> <TermoL>` |
| `<TermoL>` | `/` | `"/ " <Fator> <TermoL>` |
| `<TermoL>` | `+`, `-`, `;`, `)`, `OpRel`, `&&`, `\|\|` | **ε** |
| `<Fator>` | `IDENTIFICADOR` | `IDENTIFICADOR` |
| `<Fator>` | `NUMERO` | `NUMERO` |
| `<Fator>` | `(` | `"(" <Exp> ")"` |

