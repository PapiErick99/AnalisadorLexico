class TabelaSimbolos:
    """
    Tabla de Símbolos para almacenar identificadores, variables y otros símbolos
    encontrados durante el análisis léxico.
    
    En tu lenguaje, los identificadores empiezan con '&' (ej: &variable, &count)
    """
    
    def __init__(self):
        self.simbolos = {}  # Diccionario: {nombre: información}
        self.contador = 0   # Contador de símbolos
    
    def adicionar(self, nome, tipo, linha, coluna, escopo='global', tipo_dado=None):
        """
        Adiciona un símbolo a la tabla.
        
        Args:
            nome: Nombre del identificador (ej: &variable)
            tipo: Tipo de símbolo ('identificador', 'variable', 'funcion', etc.)
            linha: Línea donde aparece
            coluna: Columna donde aparece
            escopo: Ámbito del símbolo (global, local, etc.)
            tipo_dado: Tipo de dato (int, float, etc.) si aplica
        
        Returns:
            El símbolo agregado o el existente
        """
        if nome not in self.simbolos:
            self.contador += 1
            self.simbolos[nome] = {
                'id': self.contador,
                'nome': nome,
                'tipo': tipo,
                'linha': linha,
                'coluna': coluna,
                'escopo': escopo,
                'tipo_dado': tipo_dado if tipo_dado else 'indefinido',
                'primeira_ocorrencia': linha
            }
        else:
            # Si ya existe, solo actualizamos información si es necesaria
            # (por ejemplo, si ahora conocemos el tipo de dato)
            if tipo_dado and self.simbolos[nome]['tipo_dado'] == 'indefinido':
                self.simbolos[nome]['tipo_dado'] = tipo_dado
        
        return self.simbolos[nome]
    
    def buscar(self, nome):
        """
        Busca un símbolo en la tabla.
        
        Args:
            nome: Nombre del símbolo a buscar
            
        Returns:
            Información del símbolo o None si no existe
        """
        return self.simbolos.get(nome)
    
    def existe(self, nome):
        """
        Verifica si un símbolo existe en la tabla.
        """
        return nome in self.simbolos
    
    def listar(self):
        """
        Retorna todos los símbolos como lista ordenada por ID.
        """
        return sorted(self.simbolos.values(), key=lambda x: x['id'])
    
    def listar_por_tipo(self, tipo):
        """
        Retorna símbolos filtrados por tipo.
        """
        return [s for s in self.simbolos.values() if s['tipo'] == tipo]
    
    def total_simbolos(self):
        """
        Retorna el número total de símbolos.
        """
        return len(self.simbolos)
    
    def limpar(self):
        """
        Limpia la tabla de símbolos.
        """
        self.simbolos.clear()
        self.contador = 0
    
    def exibir(self):
        """
        Muestra la tabla de símbolos formateada en consola.
        """
        print("\n" + "="*90)
        print("TABELA DE SÍMBOLOS")
        print("="*90)
        
        if not self.simbolos:
            print("⚠️  Nenhum símbolo encontrado")
            print("="*90)
            return
        
        # Encabezado
        print(f"{'ID':<5} {'Nome':<20} {'Tipo':<15} {'Tipo Dado':<12} "
              f"{'Linha':<8} {'Col':<6} {'Escopo':<10}")
        print("-"*90)
        
        # Símbolos ordenados por ID
        for simbolo in self.listar():
            print(f"{simbolo['id']:<5} "
                  f"{simbolo['nome']:<20} "
                  f"{simbolo['tipo']:<15} "
                  f"{simbolo['tipo_dado']:<12} "
                  f"{simbolo['linha']:<8} "
                  f"{simbolo['coluna']:<6} "
                  f"{simbolo['escopo']:<10}")
        
        print("="*90)
        print(f"Total de símbolos: {self.total_simbolos()}")
