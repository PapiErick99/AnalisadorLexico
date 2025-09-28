import re

# Definición de todos los tokens que el analizador puede reconocer.
# La tupla contiene el tipo de token y la expresión regular para identificarlo.
TOKEN_DEFINICOES = [
    # -- Tokens a ignorar --
    ('COMENTARIO',      r'//.*'),
    ('ESPACO',          r'\s+'),

    # -- Palabras Reservadas (cada una es un token único) --
    ('IF',              r'\bif\b'),
    ('ELSE',            r'\belse\b'),
    ('FOR',             r'\bfor\b'),
    ('WHILE',           r'\bwhile\b'),
    ('DO',              r'\bdo\b'),
    ('INT',             r'\bint\b'),
    ('FLOAT',           r'\bfloat\b'),
    ('MAIN',            r'\bmain\b'),

    # -- Literais e Identificadores Genéricos --
    ('NUMERO',          r'\d+'),
    ('IDENTIFICADOR',   r'&[a-zA-Z][a-zA-Z0-9_]*'), # Debe ir después de las palabras reservadas

    # -- Operadores Lógicos y Relacionales (los de 2 caracteres primero) --
    ('E_LOGICO',        r'&&'),
    ('OU_LOGICO',       r'\|\|'),
    ('IGUAL_IGUAL',     r'=='),
    ('DIFERENTE',       r'!='),
    ('MENOR_IGUAL',     r'<='),
    ('MAIOR_IGUAL',     r'>='),

    # -- Operadores y Delimitadores de 1 caracter --
    ('IGUAL',           r'='),
    ('MAIS',            r'\+'),
    ('MENOS',           r'-'),
    ('MULTIPLICACAO',   r'\*'),
    ('DIVISAO',         r'/'),
    ('NAO_LOGICO',      r'!'),
    ('MENOR',           r'<'),
    ('MAIOR',           r'>'),
    ('PARENTESE_ESQ',   r'\('),
    ('PARENTESE_DIR',   r'\)'),
    ('CHAVE_ESQ',       r'\{'),
    ('CHAVE_DIR',       r'\}'),
    ('PONTO_VIRGULA',   r';'),
    ('VIRGULA',         r','),
]

# Compila las expresiones regulares para que la búsqueda sea más eficiente.
TOKEN_REGEX = [(tipo, re.compile(padrao)) for tipo, padrao in TOKEN_DEFINICOES]

class AnalisadorLexico:
    """
    Esta clase es responsable de tomar un código fuente como texto
    y convertirlo en una secuencia (lista) de tokens.
    """
    def __init__(self, codigo_fonte):
        self.codigo = codigo_fonte
        self.posicao = 0
        self.tokens = []

    def analisar(self):
        """
        Método principal que recorre el código fuente para generar los tokens.
        Devuelve una lista de tuplas, donde cada tupla es un token (tipo, lexema).
        """
        while self.posicao < len(self.codigo):
            if not self._encontrar_proximo_token():
                # Si no se encuentra ningún token, se lanza un error léxico.
                caractere_invalido = self.codigo[self.posicao]
                raise ValueError(f"Erro Léxico: Caractere inesperado '{caractere_invalido}' na posição {self.posicao}")
        return self.tokens

    def _encontrar_proximo_token(self):
        """
        Intenta encontrar una coincidencia para los patrones de token en la posición actual.
        """
        for tipo, regex in TOKEN_REGEX:
            match = regex.match(self.codigo, self.posicao)
            
            if match:
                lexema = match.group(0)
                # Se avanza la posición en el código al final del lexema encontrado.
                self.posicao = match.end(0)
                
                # Los comentarios y espacios en blanco se ignoran y no se añaden a la lista.
                if tipo not in ['COMENTARIO', 'ESPACO']:
                    self.tokens.append((tipo, lexema))
                
                return True # Indica que se procesó un token.
        
        return False # Indica que no se encontró ningún token válido.