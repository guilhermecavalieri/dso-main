from view.TelaAdicionarOrganizador import TelaAdicionarOrganizador
from view.TelaAdicionarParticipante import TelaAdicionarParticipante
from view.TelaEditarOrganizador import TelaEditarOrganizador
from view.TelaEditarParticipante import TelaEditarParticipante
from view.TelaPessoas import TelaPessoas
from model.participante import Participante
from model.organizador import Organizador
import datetime

class ControladorPessoas:

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoas = TelaPessoas()
        self.__tela_adicionar_participantes = TelaAdicionarParticipante()
        self.__tela_adicionar_organizadores = TelaAdicionarOrganizador()
        self.__tela_editar_organizador = TelaEditarOrganizador()
        self.__tela_editar_participante = TelaEditarParticipante()
        self.__participantes = []
        self.__organizadores = []

    @property
    def organizadores(self):
        return self.__organizadores

    @property
    def participantes(self):
        return self.__participantes
        
    def excluir_organizador(self, organizador):
        self.__organizadores.remove(organizador)
        self.__tela_editar_organizador.mostra_mensagem("Organizador excluído com sucesso")
            
    def editar_organizador(self, dados, organizador):
        if dados["it_nome"] == "" or dados["it_cpf"] == "":
            self.__tela_adicionar_participantes.mostra_mensagem("Preencha corretamente os campos")
            self.menu_editar_organizador(organizador)
            return None
        if len(dados["it_cpf"]) != 11:
            self.__tela_editar_organizador.mostra_mensagem("Preencha corretamente os dados")
            self.menu_editar_organizador(organizador)
            return None
        for organizador in self.__organizadores:
            if organizador.cpf == dados["it_cpf"]:
                self.__tela_editar_organizador.mostra_mensagem("Esse organizador já existe")
                self.menu_editar_organizador(organizador)
                return None
        organizador.nome = dados["it_nome"]
        organizador.cpf = dados["it_cpf"]
        self.__tela_editar_organizador.mostra_mensagem("Organizador alterado com sucesso")
        self.menu_pessoas()
        
    def adicionar_participante(self, dados):
        if not dados["it_nome"] or not dados["it_data1"] or not dados["it_data2"] or not dados["it_data3"] or not dados["it_cpf"] or not dados["it_endereco"]:
            self.__tela_adicionar_participantes.mostra_mensagem("Preencha corretamente os campos")
            self.menu_adicionar_participante()
            return None
        if int(dados["it_data1"]) == 0 or int(dados["it_data1"]) > 30 or len(dados["it_data1"]) != 2 or int(dados["it_data2"]) > 12 or int(dados["it_data2"]) == 0 or len(dados["it_data2"]) != 2 or len(dados["it_data3"]) != 4 or len(dados["it_cpf"]) != 11:
            self.__tela_adicionar_participantes.mostra_mensagem("Preencha corretamente os campos")
            self.menu_adicionar_participante()
            return None
        for participante in self.__participantes:
            if participante.cpf == dados["it_cpf"]:
                self.__tela_adicionar_participantes.mostra_mensagem("Esse participante já existe")
                self.menu_adicionar_participante()
                return None
        data = datetime.datetime(int(dados["it_data3"]), int(dados["it_data2"]), int(dados["it_data1"]))
        novo_participante = Participante(dados["it_nome"], dados["it_cpf"], dados["it_endereco"], data, dados["com_vacina"])
        self.__participantes.append(novo_participante)
        self.__tela_adicionar_participantes.mostra_mensagem("Participante cadastrado com sucesso")
        self.menu_pessoas()

    def excluir_participante(self, participante):
        self.__participantes.remove(participante)
        self.__tela_editar_participante.mostra_mensagem("Participante excluído com sucesso")

    def menu_editar_participante(self, participante_para_editar):
        dados_participante = {"nome":participante_para_editar.nome, "cpf":participante_para_editar.cpf, "endereco":participante_para_editar.endereco, "data1":participante_para_editar.nascimento.day, "data2":participante_para_editar.nascimento.month, "data3":participante_para_editar.nascimento.year, "vacina":participante_para_editar.vacina}
        opcao_escolhida, dados_novos = self.__tela_editar_participante.open(dados_participante)
        if opcao_escolhida == "bt_alterar":
            self.__tela_editar_participante.close()
            self.editar_participante(dados_novos, participante_para_editar)
        elif opcao_escolhida == "bt_cancelar":
            self.__tela_editar_participante.close()
            self.menu_pessoas()
        else:
            self.__tela_editar_participante.close()
            self.excluir_participante(participante_para_editar)
            self.menu_pessoas()

    def editar_participante(self, dados, participante):
        if dados["it_nome"] == "" or dados["it_cpf"] == "" or dados["it_data1"] == "" or dados["it_data2"] == "" or dados["it_data3"] == "" or dados["it_endereco"] == "" or dados["com_vacina"] == "":
            self.__tela_editar_participante.mostra_mensagem("Preencha corretamente os campos")
            self.menu_editar_participante(participante)
            return None
        if len(dados["it_cpf"]) != 11:
            self.__tela_editar_participante.mostra_mensagem("Preencha corretamente os campos")
            self.menu_editar_participante(participante)
            return None
        for participante in self.__participantes:
            if participante.cpf == dados["it_cpf"]:
                self.__tela_editar_participante.mostra_mensagem("Esse participante já existe")
                self.menu_editar_participante(participante)
                return None
        participante.nome = dados["it_nome"]
        data = datetime.datetime(int(dados["it_data3"]), int(dados["it_data2"]), int(dados["it_data1"]))
        participante.nascimento = data
        participante.cpf = dados["it_cpf"]
        participante.endereco = dados["it_endereco"]
        participante.vacina = dados["com_vacina"]
        self.__tela_editar_participante.mostra_mensagem("Participante alterado com sucesso")
        self.menu_pessoas()
            
    def menu_pessoas(self):
        lista_opcoes = {"bt_adicionar_participante":self.menu_adicionar_participante, "bt_adicionar_organizador":self.menu_adicionar_organizador, "bt_voltar_menu_principal":self.voltar_menu_principal}
        opcao_escolhida, valores= self.__tela_pessoas.open(self.__participantes, self.__organizadores)
        print(valores)
        self.__tela_pessoas.close()
        if opcao_escolhida != "bt_adicionar_participante" and opcao_escolhida != "bt_adicionar_organizador" and opcao_escolhida != "bt_voltar_menu_principal":
            if opcao_escolhida == "participantes":
                linha = valores["participantes"][0]
                participante_para_editar = self.__participantes[linha]
                self.menu_editar_participante(participante_para_editar)
            else:
                linha = valores["organizadores"][0]
                organizador_para_editar = self.__organizadores[linha]
                self.menu_editar_organizador(organizador_para_editar)
        else:
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
        
    def voltar_menu_principal(self):
        self.__controlador_sistema.menu_principal()

    def menu_adicionar_participante(self):
        opcao_escolhida, dados = self.__tela_adicionar_participantes.open()
        print(opcao_escolhida, dados)
        self.__tela_adicionar_participantes.close()
        if opcao_escolhida == "bt_confirmar":
            self.adicionar_participante(dados)
        else:
            self.menu_pessoas()
            
    def menu_adicionar_organizador(self):
        opcao_escolhida, dados = self.__tela_adicionar_organizadores.open()
        print(opcao_escolhida, dados)
        self.__tela_adicionar_organizadores.close()
        if opcao_escolhida == "bt_confirmar":
            self.adicionar_organizador(dados)
        else:
            self.menu_pessoas()
            
    def adicionar_organizador(self, dados):
        if not dados["it_nome"] or not dados["it_cpf"]:
            self.__tela_adicionar_organizadores.mostra_mensagem("Preencha corretamente os dados")
            self.menu_adicionar_organizador()
            return None
        if len(dados["it_cpf"]) != 11:
            self.__tela_adicionar_organizadores.mostra_mensagem("Preencha corretamente os dados")
            self.menu_adicionar_organizador()
            return None
        for organizador in self.__organizadores:
            if organizador.cpf == dados["it_cpf"]:
                self.__tela_adicionar_organizadores.mostra_mensagem("Esse organizador já existe")
                self.menu_adicionar_organizador()
                return None
        novo_organizador = Organizador(dados["it_nome"], dados["it_cpf"])
        self.__organizadores.append(novo_organizador)
        self.__tela_adicionar_organizadores.mostra_mensagem("Organizador cadastrado com sucesso")
        self.menu_pessoas()
        
    def menu_editar_organizador(self, organizador_para_editar):
        dados_organizador = {"nome":organizador_para_editar.nome, "cpf":organizador_para_editar.cpf}
        opcao_escolhida, dados_novos = self.__tela_editar_organizador.open(dados_organizador)
        if opcao_escolhida == "bt_alterar":
            self.__tela_editar_organizador.close()
            self.editar_organizador(dados_novos, organizador_para_editar)
        elif opcao_escolhida == "bt_cancelar":
            self.__tela_editar_organizador.close()
            self.menu_pessoas()
        else:
            self.__tela_editar_organizador.close()
            self.excluir_organizador(organizador_para_editar)
            self.menu_pessoas()