class AnalisadorSintatico:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    # =========================
    # Utilidades
    # =========================

    def lookahead(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos][0]
        return 'EOF'

    def consumir(self, esperado):
        atual = self.lookahead()
        if atual == esperado:
            self.pos += 1
        else:
            self.erro_sintatico(
                f"Esperado '{esperado}', encontrado '{atual}'"
            )

    # =========================
    # Gramática
    # =========================

    def programa(self):
        self.consumir('INT')
        self.consumir('MAIN')
        self.consumir('(')
        self.consumir(')')
        self.bloque()
        print("✔ Programa sintaticamente correto")

    def bloque(self):
        self.consumir('{')
        self.cmds()
        self.consumir('}')

    def cmds(self):
        if self.lookahead() in [
            'INT', 'FLOAT', 'IDENTIFICADOR',
            'IF', 'WHILE', 'DO', 'FOR', '{'
        ]:
            self.cmd()
            self.cmds()
        # ε

    def cmd(self):
        la = self.lookahead()

        if la in ['INT', 'FLOAT']:
            self.declaracao()
        elif la == 'IDENTIFICADOR':
            self.atribuicao()
        elif la == 'IF':
            self.if_stmt()
        elif la == 'WHILE':
            self.while_stmt()
        elif la == 'DO':
            self.do_while_stmt()
        elif la == 'FOR':
            self.for_stmt()
        elif la == '{':
            self.bloque()
        else:
            self.erro_sintatico(f"Comando inválido: {la}")

    # =========================
    # Declarações
    # =========================

    def declaracao(self):
        self.tipo()
        self.consumir('IDENTIFICADOR')
        self.lista_ids()
        self.consumir(';')

    def tipo(self):
        if self.lookahead() in ['INT', 'FLOAT']:
            self.pos += 1
        else:
            self.erro_sintatico("Tipo esperado")

    def lista_ids(self):
        if self.lookahead() == ',':
            self.consumir(',')
            self.consumir('IDENTIFICADOR')
            self.lista_ids()
        # ε

    def atribuicao(self):
        self.consumir('IDENTIFICADOR')
        self.consumir('=')
        self.exp()
        self.consumir(';')

    # =========================
    # Estruturas de Controle
    # =========================

    def if_stmt(self):
        self.consumir('IF')
        self.consumir('(')
        self.condicao()
        self.consumir(')')
        self.cmd()
        self.else_part()

    def else_part(self):
        if self.lookahead() == 'ELSE':
            self.consumir('ELSE')
            self.cmd()
        # ε

    def while_stmt(self):
        self.consumir('WHILE')
        self.consumir('(')
        self.condicao()
        self.consumir(')')
        self.cmd()

    def do_while_stmt(self):
        self.consumir('DO')
        self.bloque()
        self.consumir('WHILE')
        self.consumir('(')
        self.condicao()
        self.consumir(')')
        self.consumir(';')

    def for_stmt(self):
        self.consumir('FOR')
        self.consumir('(')
        self.atrib_for()
        self.consumir(';')
        self.condicao()
        self.consumir(';')
        self.atrib_for()
        self.consumir(')')
        self.cmd()

    def atrib_for(self):
        self.consumir('IDENTIFICADOR')
        self.consumir('=')
        self.exp()

    # =========================
    # Condições Lógicas
    # =========================

    def condicao(self):
        self.cond_termo()
        self.condicao_l()

    def condicao_l(self):
        if self.lookahead() == '||':
            self.consumir('||')
            self.cond_termo()
            self.condicao_l()
        # ε

    def cond_termo(self):
        self.cond_fator()
        self.cond_termo_l()

    def cond_termo_l(self):
        if self.lookahead() == '&&':
            self.consumir('&&')
            self.cond_fator()
            self.cond_termo_l()
        # ε

    def cond_fator(self):
        if self.lookahead() == '!':
            self.consumir('!')
            self.cond_fator()
        else:
            self.exp()
            self.op_rel()
            self.exp()

    def op_rel(self):
        if self.lookahead() in ['==', '!=', '<=', '>=', '<', '>']:
            self.pos += 1
        else:
            self.erro_sintatico("Operador relacional esperado")

    # =========================
    # Expressões Aritméticas
    # =========================

    def exp(self):
        self.termo()
        self.exp_l()

    def exp_l(self):
        if self.lookahead() in ['+', '-']:
            self.pos += 1
            self.termo()
            self.exp_l()
        # ε

    def termo(self):
        self.fator()
        self.termo_l()

    def termo_l(self):
        if self.lookahead() in ['*', '/']:
            self.pos += 1
            self.fator()
            self.termo_l()
        # ε

    def fator(self):
        la = self.lookahead()

        if la in ['IDENTIFICADOR', 'NUMERO']:
            self.pos += 1
        elif la == '(':
            self.consumir('(')
            self.exp()
            self.consumir(')')
        else:
            self.erro_sintatico(f"Fator inválido: {la}")

    def erro_sintatico(self, msg):
        print(f"[ERRO SINTÁTICO] {msg}")
        self.modo_panico()

    def modo_panico(self):
        sincronizacao = [';', '}', ')', 'EOF']

        while self.pos < len(self.tokens) and self.lookahead() not in sincronizacao:
            self.pos += 1

        if self.lookahead() != 'EOF':
            self.pos += 1

