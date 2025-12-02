import re
from src.SymbolTableManager import TabelaSimbolos
from src.ErrorReportManager import RelatorioErros

# Definición de todos los tokens que el analizador puede reconocer.
# La tupla contiene el tipo de token y la expresión regular para identificarlo.
TOKEN_DEFINICOES = [
    # -- Tokens a ignorar --
    ('COMENTARIO', r'//.*'),
    ('ESPACO', r'\s+'),

    # -- Palabras Reservadas (cada una es un token único) --
    ('IF', r'\bif\b'),
    ('ELSE', r'\belse\b'),
    ('FOR', r'\bfor\b'),
    ('WHILE', r'\bwhile\b'),
    ('DO', r'\bdo\b'),
    ('INT', r'\bint\b'),
    ('FLOAT', r'\bfloat\b'),
    ('MAIN', r'\bmain\b'),

    # -- Literais e Identificadores Genéricos --
    ('NUMERO', r'\d+'),
    ('IDENTIFICADOR', r'&[a-zA-Z][a-zA-Z0-9_]*'),  # Debe ir después de las palabras reservadas

    # -- Operadores Lógicos y Relacionales (los de 2 caracteres primero) --
    ('&&', r'&&'),
    ('||', r'\|\|'),
    ('==', r'=='),
    ('!=', r'!='),
    ('<=', r'<='),
    ('>=', r'>='),

    # -- Operadores y Delimitadores de 1 caracter --
    ('=', r'='),
    ('+', r'\+'),
    ('-', r'-'),
    ('*', r'\*'),
    ('/', r'/'),
    ('!', r'!'),
    ('<', r'<'),
    ('>', r'>'),
    ('(', r'\('),
    (')', r'\)'),
    ('{', r'\{'),
    ('}', r'\}'),
    (';', r';'),
    (',', r','),
]

# Compila las expresiones regulares para que la búsqueda sea más eficiente.
TOKEN_REGEX = [(tipo, re.compile(padrao)) for tipo, padrao in TOKEN_DEFINICOES]


# prepara las expresiones regulares que luego se usarán para analizar cadenas de texto,
# identificando distintos tokens según los patrones definidos.

class AnalisadorLexico:
    """
    Esta clase es responsable de tomar un código fuente como texto
    y convertirlo en una secuencia (lista) de tokens.
    """

    def __init__(self, codigo_fonte):
        self.codigo = codigo_fonte
        self.posicao = 0
        self.linha = 1
        self.coluna = 1
        self.tokens = []
        self.tabela_simbolos = TabelaSimbolos()
        self.relatorio_erros = RelatorioErros()
        self.ultimo_tipo_dado = None  # Para rastrear declaraciones de tipo

    def analisar(self):
        """
        Método principal que recorre el código fuente para generar los tokens.
        Ahora continúa el análisis incluso si encuentra errores.
        """
        while self.posicao < len(self.codigo):
            if not self._encontrar_proximo_token():
                # Registrar error pero continuar
                caractere_invalido = self.codigo[self.posicao]
                self.relatorio_erros.adicionar_erro(
                    tipo='LEXICO',
                    mensagem=f"Caractere inesperado '{caractere_invalido}'",
                    linha=self.linha,
                    coluna=self.coluna,
                    lexema=caractere_invalido
                )
                # Avanzar para continuar el análisis
                self._avancar_caractere()

        return self.tokens

    def _avancar_caractere(self):
        """Avanza un carácter y actualiza línea/columna"""
        if self.posicao < len(self.codigo):
            if self.codigo[self.posicao] == '\n':
                self.linha += 1
                self.coluna = 1
            else:
                self.coluna += 1
            self.posicao += 1

    def _encontrar_proximo_token(self):
        """
        Intenta encontrar una coincidencia para los patrones de token en la posición actual.
        """
        for tipo, regex in TOKEN_REGEX:
            match = regex.match(self.codigo, self.posicao)

            if match:
                lexema = match.group(0)
                linha_token = self.linha
                coluna_token = self.coluna

                # Actualizar posición recorriendo cada carácter
                for char in lexema:
                    self._avancar_caractere()

                # Los comentarios y espacios en blanco se ignoran
                if tipo not in ['COMENTARIO', 'ESPACO']:
                    # Agregar token a la lista como tupla (tipo, lexema)
                    self.tokens.append((tipo, lexema))

                    # Rastrear declaraciones de tipo
                    if tipo in ['INT', 'FLOAT']:
                        self.ultimo_tipo_dado = lexema

                    # Agregar identificadores a la tabla de símbolos
                    if tipo == 'IDENTIFICADOR':
                        self.tabela_simbolos.adicionar(
                            nome=lexema,
                            tipo='identificador',
                            linha=linha_token,
                            coluna=coluna_token,
                            tipo_dado=self.ultimo_tipo_dado
                        )
                        # Resetear tipo después de agregar
                        self.ultimo_tipo_dado = None

                    # Rastrear main como símbolo especial
                    elif tipo == 'MAIN':
                        self.tabela_simbolos.adicionar(
                            nome='main',
                            tipo='funcion',
                            linha=linha_token,
                            coluna=coluna_token,
                            tipo_dado='void'
                        )

                return True  # Indica que se procesó un token

        return False  # Indica que no se encontró ningún token válido

    def exibir_tokens(self):
        """
        Muestra la lista de tokens formateada.
        """
        print("\n" + "=" * 80)
        print("LISTA DE TOKENS")
        print("=" * 80)

        if not self.tokens:
            print("⚠️  Nenhum token encontrado")
            print("=" * 80)
            return

        print(f"{'#':<5} {'Tipo':<20} {'Lexema':<20} {'Linha':<8} {'Coluna':<8}")
        print("-" * 80)

        for idx, token in enumerate(self.tokens, 1):
            print(f"{idx:<5} "
                  f"{token[0]:<20} "
                  f"{token[1]:<20} "
                  f"{'N/A':<8} "
                  f"{'N/A':<8}")

        print("=" * 80)
        print(f"Total de tokens: {len(self.tokens)}")