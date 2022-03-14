from view.TelaPessoas import TelaPessoas
from model.participante import Participante
from model.organizador import Organizador
from model.pessoa import Pessoa

class ControladorPessoas:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoas()
        self.__participantes = []
        self.__organizadores = []

    @property
    def organizadores(self):
        return self.__organizadores

    @property
    def participantes(self):
        return self.__participantes

    def incluir_organizador(self):
        self.__tela_pessoas.limpa_tela()
        nome, cpf = self.__tela_pessoas.pega_dados_organizador()
        for organizador in self.__organizadores:
            if organizador.cpf == cpf:
                self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ESSE ORGANIZADOR JÁ EXISTE")

        novo_organizador = Organizador(nome, cpf)
        self.__organizadores.append(novo_organizador)
        self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ORGANIZADOR CADASTRADO")
        
    def excluir_organizador(self):
        self.__tela_pessoas.limpa_tela()
        cpf = self.__tela_pessoas.seleciona_organizador_pelo_cpf()
        organizador = self.pega_organizador_pelo_cpf(cpf)
            
        if organizador is not None:
            self.__organizadores.remove(organizador)
            self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ORGANIZADOR EXCLÚIDO")
        else:
            self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ESSE ORGANIZADOR NÃO EXISTE")
            
    def editar_organizador(self):
        self.__tela_pessoas.limpa_tela()
        cpf = self.__tela_pessoas.seleciona_organizador_pelo_cpf()
        organizador = self.pega_organizador_pelo_cpf(cpf)
        
        if organizador is not None:
            nome, cpf = self.__tela_pessoas.pega_dados_organizador()
            organizador.nome = nome
            organizador.cpf = cpf
            self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ORGANIZADOR ALTERADO")
        else:
            self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ESSE ORGANIZADOR NÃO EXISTE")
        
    def incluir_participante(self):
        self.__tela_pessoas.limpa_tela()
        nome, cpf, nascimento, endereco, vacina, exame = self.__tela_pessoas.pega_dados_participante()
        for participante in self.__participantes:
            if participante.cpf == cpf:
                self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ESSE PARTICIPANTE JÁ EXISTE")
        
        participante = Participante(nome,cpf,endereco,nascimento,vacina,exame)
        self.__participantes.append(participante)
        self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "PARTICIPANTE CADASTRADO")

    def excluir_participante(self):
        self.__tela_pessoas.limpa_tela()
        cpf = self.__tela_pessoas.seleciona_participante_pelo_cpf()
        participante = self.pega_participante_pelo_cpf(cpf)

        if participante is not None:
            self.__participantes.remove(participante)
            self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "PARTICIPANTE EXCLUÍDO")
        else:
            self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ESSE PARTICIPANTE NÃO EXISTE")

    def editar_participante(self):
        self.__tela_pessoas.limpa_tela()
        cpf = self.__tela_pessoas.seleciona_participante_pelo_cpf()
        participante = self.pega_participante_pelo_cpf(cpf)

        if participante is not None:
            nome, cpf, nascimento, endereco, vacina, exame = self.__tela_pessoas.pega_dados_participante()
            participante.nome = nome
            participante.cpf = cpf
            participante.nascimento = nascimento
            participante.endereco = endereco
            participante.vacina = vacina
            participante.exame = exame
            self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "PARTICIPANTE ALTERADO")
        else:
            self.mostra_tela_menu_pessoas(self.__participantes, self.__organizadores, "ESSE PARTICIPANTE NÃO EXISTE")
            
    def voltar_menu_principal(self):
        self.__tela_pessoas.close()
        self.__controlador_sistema.menu_principal()
            
    def pega_participante_pelo_cpf(self, cpf):
        for participante in self.__participantes:
            if participante.cpf == cpf:
                return participante
            return None
        
    def pega_organizador_pelo_cpf(self, cpf):
        for organizador in self.__organizadores:
            if organizador.cpf == cpf:
                return organizador
            return None
        
    def lista_pessoas(self, participantes, organizadores, mensagem):
        
        if organizadores or participantes:
            self.__tela_pessoas.lista_pessoas(participantes, organizadores, mensagem)
        else:
            self.__tela_pessoas.lista_pessoas(None, None, "NÃO EXISTEM PESSOAS CADASTRADAS")
            
    def menu_pessoas(self):
        lista_opcoes = {"bt_adicionar_participante":self.incluir_participante, "bt_excluir_participante":self.excluir_participante, "bt_editar_participante":self.editar_participante, "bt_adicionar_organizador":self.incluir_organizador, "bt_excluir_organizador":self.excluir_organizador, "bt_editar_organizador":self.editar_organizador, "bt_voltar_menu_principal":self.voltar_menu_principal}

        opcao_escolhida = self.__tela_pessoas.open()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()

