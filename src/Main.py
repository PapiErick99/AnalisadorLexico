# -*- coding: utf-8 -*-
import sys
# Importamos la clase AnalisadorLexico desde nuestro otro archivo.
from LexicalAnalizer import AnalisadorLexico

def main():
    """
    Función principal que orquesta la ejecución del analizador léxico.
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

    # 1. Se crea una instancia del analizador con el código fuente.
    lexer = AnalisadorLexico(codigo)
    
    try:
        # 2. Se llama al método para que procese el código y devuelva los tokens.
        tokens = lexer.analisar()

        # 3. Se imprimen los resultados de forma clara.
        print("--- Tokens Reconhecidos ---")
        for tipo, lexema in tokens:
            print(f"Token: {tipo:<20} | Lexema: '{lexema}'")
        print("\n--- Análise Léxica Concluída com Sucesso! ---")

    except ValueError as e:
        # Si ocurre un error léxico durante el análisis, se captura y muestra.
        print(e)
        sys.exit(1)

if __name__ == '__main__':
    main()