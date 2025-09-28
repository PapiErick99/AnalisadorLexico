# -*- coding: utf-8 -*-
import re
import sys

# -----------------------------------------------------------------------------
# Definição dos Tokens com Expressões Regulares
# -----------------------------------------------------------------------------
# A ordem aqui é importante! Palavras reservadas vêm antes de identificadores.
TOKEN_DEFINICOES = [
    # -- Tokens a serem ignorados --
    ('COMENTARIO',  r'//.*'),           # Comentário de linha única
    ('ESPACO',      r'\s+'),             # Espaços em branco, tabs, novas linhas

    # -- Palavras Reservadas --
    ('PALAVRA_RESERVADA', r'\b(if|else|for|while|do|int|float|main)\b'),

    # -- Literais e Identificadores --
    ('NUMERO',      r'\d+'),             # Números inteiros
    ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'), # Identificadores (variáveis, etc)

    # -- Operadores --
    ('OPERADOR_ATRIBUICAO', r'='),
    ('OPERADOR_RELACIONAL', r'==|!=|<=|>=|<|>'),
    ('OPERADOR_ARITMETICO', r'\+|-|\*|/'),
    ('OPERADOR_LOGICO', r'&&|\|\||!'),


    # -- Delimitadores --
    ('DELIMITADOR', r'[\(\)\{\};,]'),
]

# Compila as expressões regulares para melhor desempenho
TOKEN_REGEX = [(tipo, re.compile(padrao)) for tipo, padrao in TOKEN_DEFINICOES]

# -----------------------------------------------------------------------------
# Classe do Analisador Léxico (Lexer)
# -----------------------------------------------------------------------------
class AnalisadorLexico:
    def __init__(self, codigo_fonte):
        self.codigo = codigo_fonte
        self.posicao = 0
        self.tokens = []

    def analisar(self):
        """
        Função principal que percorre o código fonte e gera a lista de tokens.
        """
        while self.posicao < len(self.codigo):
            token_encontrado = self._encontrar_proximo_token()
            if not token_encontrado:
                # Se nenhum token for encontrado, significa um caractere inválido
                caractere_invalido = self.codigo[self.posicao]
                raise ValueError(f"Erro Léxico: Caractere inesperado '{caractere_invalido}' na posição {self.posicao}")

        return self.tokens

    def _encontrar_proximo_token(self):
        """
        Tenta encontrar o próximo token na posição atual do código.
        """
        for tipo, regex in TOKEN_REGEX:
            match = regex.match(self.codigo, self.posicao)
            
            if match:
                lexema = match.group(0)
                
                # Ignora comentários e espaços em branco
                if tipo not in ['COMENTARIO', 'ESPACO']:
                    self.tokens.append((tipo, lexema))
                
                # Avança a posição no código para depois do token encontrado
                self.posicao = match.end(0)
                return True # Retorna True para indicar que um token foi processado
        
        return False # Retorna False se nenhum padrão de token corresponder

# -----------------------------------------------------------------------------
# Função Principal para Execução
# -----------------------------------------------------------------------------
def main():
    # Nome do arquivo de código fonte a ser analisado
    nome_arquivo = 'programa_exemplo.txt'

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            codigo = arquivo.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        sys.exit(1)

    print("--- Iniciando Análise Léxica ---")
    print(f"Arquivo a ser analisado: {nome_arquivo}\n")

    # Cria o analisador e executa a análise
    lexer = AnalisadorLexico(codigo)
    try:
        tokens = lexer.analisar()

        # Imprime os tokens encontrados de forma organizada
        print("--- Tokens Reconhecidos ---")
        for tipo, lexema in tokens:
            print(f"Tipo: {tipo:<20} | Lexema: '{lexema}'")
        print("\n--- Análise Léxica Concluída com Sucesso! ---")

    except ValueError as e:
        print(e)
        sys.exit(1)

# Ponto de entrada do script
if __name__ == '__main__':
    main()