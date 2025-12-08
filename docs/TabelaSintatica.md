# Tabla de Análisis Sintáctico

> **Notación:** En cada celda `M[A, a]` se muestra la producción usada `A → ...`  
> Las celdas vacías indican que no hay producción definida para esa combinación.

## Símbolos Terminales

| Símbolo | Descripción |
|---------|-------------|
| `INT`, `FLOAT` | Tipos de datos |
| `ID` | Identificador |
| `IF`, `WHILE`, `DO`, `FOR` | Palabras reservadas |
| `NUM` | Número |
| `{`, `}`, `(`, `)` | Delimitadores |
| `==`, `!=`, `<=`, `>=`, `<`, `>` | Operadores relacionales |
| `+`, `-`, `*`, `/` | Operadores aritméticos |
| `||`, `&&`, `!` | Operadores lógicos |
| `,`, `;` | Separadores |
| `$` | Fin de archivo |

---

## Tabla de Análisis LL(1)

| No-terminal | `INT` | `FLOAT` | `ID` | `IF` | `WHILE` | `DO` | `FOR` | `{` | `}` | `(` | `)` | `NUM` | `,` | `;` | `==` | `!=` | `<=` | `>=` | `<` | `>` | `+` | `-` | `*` | `/` | `\|\|` | `&&` | `!` | `$` |
|-------------|-------|---------|------|------|---------|------|-------|-----|-----|-----|-----|-------|-----|-----|------|------|------|------|-----|-----|-----|-----|-----|-----|--------|------|-----|-----|
| **`<Programa>`** | `→ INT MAIN ( ) <Bloque>` | | | | | | | | | | | | | | | | | | | | | | | | | | | `$` |
| **`<Bloque>`** | | | | | | | | `→ { <Cmds> }` | | | | | | | | | | | | | | | | | | | | |
| **`<Cmds>`** | `→ <Cmd> <Cmds>` | `→ <Cmd> <Cmds>` | `→ <Cmd> <Cmds>` | `→ <Cmd> <Cmds>` | `→ <Cmd> <Cmds>` | `→ <Cmd> <Cmds>` | `→ <Cmd> <Cmds>` | `→ <Cmd> <Cmds>` | `→ ε` | | | | | | | | | | | | | | | | | | | |
| **`<Cmd>`** | `→ <Declaracao>` | `→ <Declaracao>` | `→ <Atribuicao>` | `→ <IfStmt>` | `→ <WhileStmt>` | `→ <DoWhileStmt>` | `→ <ForStmt>` | `→ <Bloque>` | | | | | | | | | | | | | | | | | | | | |
| **`<Declaracao>`** | `→ <Tipo> ID <ListaIds> ;` | `→ <Tipo> ID <ListaIds> ;` | | | | | | | | | | | | | | | | | | | | | | | | | | |
| **`<Tipo>`** | `→ INT` | `→ FLOAT` | | | | | | | | | | | | | | | | | | | | | | | | | | |
| **`<ListaIds>`** | | | | | | | | | | | | | `→ , ID <ListaIds>` | `→ ε` | | | | | | | | | | | | | | |
| **`<Atribuicao>`** | | | `→ ID = <Exp> ;` | | | | | | | | | | | | | | | | | | | | | | | | | |
| **`<IfStmt>`** | | | | `→ IF ( <Condicao> ) <Cmd> <ElsePart>` | | | | | | | | | | | | | | | | | | | | | | | | |
| **`<ElsePart>`** | `→ ε` | `→ ε` | `→ ε` | `→ ε` | `→ ε` | `→ ε` | `→ ε` | `→ ε` | `→ ε` | | | | | | | | | | | | | | | | | | | |
| **`<WhileStmt>`** | | | | | `→ WHILE ( <Condicao> ) <Cmd>` | | | | | | | | | | | | | | | | | | | | | | | |
| **`<DoWhileStmt>`** | | | | | | `→ DO <Bloque> WHILE ( <Condicao> ) ;` | | | | | | | | | | | | | | | | | | | | | | |
| **`<ForStmt>`** | | | | | | | `→ FOR ( <AtribFor> ; <Condicao> ; <AtribFor> ) <Cmd>` | | | | | | | | | | | | | | | | | | | | | |
| **`<AtribFor>`** | | | `→ ID = <Exp>` | | | | | | | | | | | | | | | | | | | | | | | | | |
| **`<Condicao>`** | | | `→ <CondTermo> <CondicaoL>` | | | | | | | `→ <CondTermo> <CondicaoL>` | | `→ <CondTermo> <CondicaoL>` | | | | | | | | | | | | | | | `→ <CondTermo> <CondicaoL>` | |
| **`<CondicaoL>`** | | | | | | | | | `→ ε` | | `→ ε` | | | `→ ε` | | | | | | | | | | | `→ \|\| <CondTermo> <CondicaoL>` | `→ ε` | | |
| **`<CondTermo>`** | | | `→ <CondFator> <CondTermoL>` | | | | | | | `→ <CondFator> <CondTermoL>` | | `→ <CondFator> <CondTermoL>` | | | | | | | | | | | | | | | `→ <CondFator> <CondTermoL>` | |
| **`<CondTermoL>`** | | | | | | | | | `→ ε` | | `→ ε` | | | `→ ε` | | | | | | | | | | | `→ ε` | `→ && <CondFator> <CondTermoL>` | | |
| **`<CondFator>`** | | | `→ <Exp> <OpRel> <Exp>` | | | | | | | `→ <Exp> <OpRel> <Exp>` | | `→ <Exp> <OpRel> <Exp>` | | | | | | | | | | | | | | | `→ ! <CondFator>` | |
| **`<OpRel>`** | | | | | | | | | | | | | | | `→ ==` | `→ !=` | `→ <=` | `→ >=` | `→ <` | `→ >` | | | | | | | | |
| **`<Exp>`** | | | `→ <Termo> <ExpL>` | | | | | | | `→ <Termo> <ExpL>` | | `→ <Termo> <ExpL>` | | | | | | | | | | | | | | | | |
| **`<ExpL>`** | | | | | | | | | `→ ε` | | `→ ε` | | | `→ ε` | | | | | | | `→ + <Termo> <ExpL>` | `→ - <Termo> <ExpL>` | | | | | | |
| **`<Termo>`** | | | `→ <Fator> <TermoL>` | | | | | | | `→ <Fator> <TermoL>` | | `→ <Fator> <TermoL>` | | | | | | | | | | | | | | | | |
| **`<TermoL>`** | | | | | | | | | `→ ε` | | `→ ε` | | | `→ ε` | | | | | | | `→ ε` | `→ ε` | `→ * <Fator> <TermoL>` | `→ / <Fator> <TermoL>` | | | | |
| **`<Fator>`** | | | `→ ID` | | | | | | | `→ ( <Exp> )` | | `→ NUM` | | | | | | | | | | | | | | | | |

---

## Leyenda

- **ε** : Producción vacía (epsilon)
- **→** : Símbolo de producción
- Las celdas vacías indican **error sintáctico**
- **Negrita** en no-terminales para mejor legibilidad

## Características de la Gramática

- ✅ Gramática LL(1)
- ✅ Sin ambigüedades
- ✅ Factorización por izquierda aplicada
- ✅ Recursión por derecha en producciones opcionales