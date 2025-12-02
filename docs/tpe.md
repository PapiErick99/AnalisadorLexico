# 📜 Relatório Completo - Analisador Sintático Preditivo LL(1) 💡

---

### **Sumário Executivo**

Este relatório detalha o design completo de um **analisador sintático preditivo não recursivo (LL(1))** para a linguagem **CompCCUno**. O projeto aborda a construção da gramática, seu ajuste para ser LL(1), o cálculo dos conjuntos FIRST e FOLLOW, a geração da tabela sintática, a implementação da recuperação de erros (*panic-mode*), e o pseudocódigo do analisador.

---

### **1. 🎯 Objetivo Geral**

O propósito principal deste trabalho é projetar completamente um analisador sintático preditivo não recursivo (LL(1)) para a linguagem CompCCUno.

O desenvolvimento inclui os seguintes passos chave:
* Construção da gramática GLC.
* Ajustes para torná-la LL(1).
* Cálculo completo dos conjuntos $\text{FIRST}$ e $\text{FOLLOW}$.
* Construção da tabela sintática $\text{LL(1)}$.
* Implementação do modo de recuperação de erros (*panic-mode*).
* Geração do pseudocódigo do analisador.
Exemplos completos de *parsing*.

---

### **2. 💻 Definição da Linguagem CompCCUno**

#### **2.1. Tokens Completos (Excerto)**

A linguagem define vários *tokens*, incluindo identificadores que começam com '&', palavras-chave, operadores e símbolos.

| Categoria | Nome do Token | Exemplo de Lexema |
| :--- | :--- | :--- |
| **Comentário** | COMENTARIO | `//.*` |
| **Palavra-Chave** | IF, ELSE, INT, MAIN | `if`, `else`, `int`, `main` |
| **Identificador** | IDENTIFICADOR | `&[a-zA-Z][a-zA-Z0-9_]*` |
| **Literal** | NUMERO | `\d+` |
| **Operador Relacional** | $==, !=, <=, >=, <, >$ | `==`, `!=`, `<`, `>` |
| **Operador Lógico** | `&&`, `||` | `&&`, `||` |
| **Outros** | (, ), {, }, ;, = | `(`, `)`, `{`, `}`, `;` |

#### **2.2. Sintaxe e Componentes**

A sintaxe de CompCCUno inclui:
* Função principal: `main()`.
* Blocos de código entre chaves.
* Declarações de variáveis (`int`, `float`).
* Comandos de atribuição.
* Condicionais `if/else`.
* Estruturas de repetição: `while`, `do-while`, `for`.
* Expressões aritméticas, relacionais e lógicas.
* Identificadores começando com `&`.

#### **2.3. Gramática GLC Original (Excerto)**

A gramática GLC é definida como:
* `Program → MAIN '(' ')' Block`
* `Block → '{' Declarations Statements '}'`
* `Statements → Statement Statements | ε`
* `IfStmt → IF '(' Expression ')' Statement ElsePart`
* `ElsePart → ELSE Statement | ε`

---

### **3. 🧮 Cálculos de Conjuntos**

Os conjuntos $\text{FIRST}$ e $\text{FOLLOW}$ foram construídos com base na gramática transformada.

#### **3.1. Conjuntos FIRST (Excertos)**

| Não Terminal | Conjunto FIRST |
| :--- | :--- |
| **Program** | $\{$MAIN$\}$ |
| **Block** | $\{$'{'$\}$ |
| **Declarations** | $\{$INT, FLOAT, $\epsilon$$\}$ |
| **Expression** | $\{$IDENTIFICADOR, NUMERO, '(', '!', '-'$\}$ |

#### **3.2. Conjuntos FOLLOW (Excertos)**

| Não Terminal | Conjunto FOLLOW |
| :--- | :--- |
| **Program** | $\{$ $\$$ $\}$ |
| **Block** | $\{$ ELSE, WHILE, DO, FOR, IDENTIFICADOR, ';', '}', $\$$ $\}$ |
| **Statements** | $\{$'}'$\}$ |
| **Declarations** | $=$ FOLLOW(Block) |

---

### **5. 🛠️ Recuperação de Erros (Panic Mode)**

O método de recuperação de erros implementado é o *panic-mode*.

| Situação | Método de Recuperação |
| :--- | :--- |
| $\text{token} \in \text{FOLLOW(A)}$ | O não terminal $A$ é descartado da pilha (*pop*). |
| **Sincronização** | Os *tokens* de entrada são descartados até que um *token* de sincronização seja encontrado. |

**Conjuntos Sincronizantes (Exemplos)**:
* `sync(Statement)` = `{ ';', '}', ELSE }`
* `sync(Block)` = `{'}' , $ }`

---

### **6. 📝 Pseudocódigo do Analisador Preditivo**

```pseudocode
Procedure PredictiveParser (input):
    stack = [$, Program]
    token = nextToken()
    
    while stack not empty:
        top = stack.top()
        
        if top is terminal:
            if top == token:
                pop(top)
                token = nextToken()
            else:
                erro("terminal inesperado")
                token = nextToken()
        
        else: // top é um Não Terminal
            prod = M[top, token]
            
            if prod existe:
                pop(top)
                push(prod.RHS invertida)
            
            elif token  FOLLOW(top):
                pop(top) // Caso 1: Descartar Não Terminal
            
            else:
                token = nextToken() // Caso 2: Descartar token de entrada
                
    if token == $:
        aceitar()