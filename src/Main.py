# -*- coding: utf-8 -*-
import sys

from LexicalAnalizer import AnalisadorLexico
from SintacticAnalizer import AnalisadorSintatico


def main():
    """
    Función principal que orquesta la ejecución del analizador léxico y sintáctico.
    """
    nome_arquivo = 'data/programa_exemplo.txt'

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            codigo = arquivo.read()
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
        sys.exit(1)

    print("--- Iniciando Análise Léxica ---")
    print(f"Arquivo a ser analisado: {nome_arquivo}\n")

    # ==========================
    # Análise Léxica
    # ==========================
    lexer = AnalisadorLexico(codigo)
    tokens = lexer.analisar()

    print("--- Tokens Reconhecidos ---")
    # for tipo, lexema in tokens:
    lexer.exibir_tokens()
    #    print(f"Token: {tipo:<20} | Lexema: '{lexema}'")

    print("\n--- Análise Léxica Concluída com Sucesso! ---\n")
    # ==========================
    # Análise Sintática
    # ==========================
    print("--- Iniciando Análise Sintática ---")
    try:
        parser = AnalisadorSintatico(tokens)
        parser.programa()
        print("--- Análise Sintática Concluída com Sucesso! ---")
    except SyntaxError as e:
        print(e)
        sys.exit(1)


if __name__ == '__main__':
    main()
