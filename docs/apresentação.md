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

![Automato](docs/AFD.jpeg)











