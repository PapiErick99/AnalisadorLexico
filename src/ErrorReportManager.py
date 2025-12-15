class RelatorioErros:
    """
    Clase para almacenar y gestionar todos los errores encontrados
    durante el análisis léxico (y más adelante, sintáctico).
    """
    
    def __init__(self):
        self.erros = []
    
    def adicionar_erro(self, tipo, mensagem, linha, coluna, lexema=''):
        """
        Adiciona un error al reporte.
        
        Args:
            tipo: Tipo de error ('LEXICO', 'SINTATICO', 'SEMANTICO')
            mensagem: Mensaje descriptivo del error
            linha: Línea donde ocurrió el error
            coluna: Columna donde ocurrió el error
            lexema: El lexema que causó el error (opcional)
        """
        self.erros.append({
            'id': len(self.erros) + 1,
            'tipo': tipo,
            'mensagem': mensagem,
            'linha': linha,
            'coluna': coluna,
            'lexema': lexema
        })
    
    def tem_erros(self):
        """
        Verifica si hay errores registrados.
        """
        return len(self.erros) > 0
    
    def total_erros(self):
        """
        Retorna el número total de errores.
        """
        return len(self.erros)
    
    def erros_por_tipo(self, tipo):
        """
        Retorna errores filtrados por tipo.
        """
        return [e for e in self.erros if e['tipo'] == tipo]
    
    def limpar(self):
        """
        Limpia todos los errores.
        """
        self.erros.clear()
    
    def exibir(self):
        """
        Muestra el reporte de errores formateado.
        """
        print("\n" + "="*100)
        print("RELATÓRIO DE ERROS")
        print("="*100)
        
        if not self.tem_erros():
            print("✅ Nenhum erro encontrado! Código analisado com sucesso.")
            print("="*100)
            return
        
        # Encabezado
        print(f"{'ID':<5} {'Tipo':<12} {'Linha':<8} {'Col':<6} "
              f"{'Lexema':<15} {'Mensagem'}")
        print("-"*100)
        
        # Errores
        for erro in self.erros:
            lexema_str = erro['lexema'] if erro['lexema'] else 'N/A'
            print(f"{erro['id']:<5} "
                  f"{erro['tipo']:<12} "
                  f"{erro['linha']:<8} "
                  f"{erro['coluna']:<6} "
                  f"{lexema_str:<15} "
                  f"{erro['mensagem']}")
        
        print("="*100)
        print(f"❌ Total de erros: {self.total_erros()}")
        
        # Estadísticas por tipo
        lexicos = len(self.erros_por_tipo('LEXICO'))
        sintaticos = len(self.erros_por_tipo('SINTATICO'))
        semanticos = len(self.erros_por_tipo('SEMANTICO'))
        
        if lexicos > 0:
            print(f"   - Erros Léxicos: {lexicos}")
        if sintaticos > 0:
            print(f"   - Erros Sintáticos: {sintaticos}")
        if semanticos > 0:
            print(f"   - Erros Semânticos: {semanticos}")