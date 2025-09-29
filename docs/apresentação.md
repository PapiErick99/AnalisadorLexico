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
| `&&`     | `E_LOGICO`   | Operador lógico E (AND) |             |                         |
| `        |              | `                       | `OU_LOGICO` | Operador lógico OU (OR) |
| `!`      | `NAO_LOGICO` | Negação lógica (NOT)    |             |                         |


### Operadores Relacionais
| Lexema | Token         | Descrição      |
| -------- | ------------- | -------------- |
| `==`     | `IGUAL_IGUAL` | Igualdade      |
| `!=`     | `DIFERENTE`   | Diferença      |
| `<`      | `MENOR`       | Menor que      |
| `<=`     | `MENOR_IGUAL` | Menor ou igual |
| `>`      | `MAIOR`       | Maior que      |
| `>=`     | `MAIOR_IGUAL` | Maior ou igual |

### Operadores Aritméticos e Atribuição
| Lexema | Token           | Descrição     |
| -------- | --------------- | ------------- |
| `=`      | `IGUAL`         | Atribuição    |
| `+`      | `MAIS`          | Soma          |
| `-`      | `MENOS`         | Subtração     |
| `*`      | `MULTIPLICACAO` | Multiplicação |
| `/`      | `DIVISAO`       | Divisão       |

### Delimitadores e Pontuação
| Lexema | Token           | Descrição          |
| -------- | --------------- | ------------------ |
| `(`      | `PARENTESE_ESQ` | Parêntese esquerdo |
| `)`      | `PARENTESE_DIR` | Parêntese direito  |
| `{`      | `CHAVE_ESQ`     | Chave esquerda     |
| `}`      | `CHAVE_DIR`     | Chave direita      |
| `;`      | `PONTO_VIRGULA` | Ponto e vírgula    |
| `,`      | `VIRGULA`       | Vírgula            |


### Tokens Ignorados
| Lexema | Token        | Descrição                                         |
| -------- | ------------ | ------------------------------------------------- |
| `// ...` | `COMENTARIO` | Comentário de linha, ignorado pelo analisador     |
| `\s+`    | `ESPACO`     | Espaços, tabulações e quebras de linha, ignorados |



# 1.2.1 - Apresentar o reconhecimento dos tokens da linguagem por meio de AFD;


# 1.2.1 - Construir a tabela de transição;












