import datetime
from msilib.schema import Error
from multiprocessing.sharedctypes import Value
from view.TelaAdicionarEvento import TelaAdicionarEventos
from view.TelaEventos import TelaEventos
from model.evento import Evento

class ControladorEventos():

    def __init__(self, controlador_sistema):
        self.__eventos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_eventos = TelaEventos()
        self.__tela_adicionar_evento = TelaAdicionarEventos()

    def pega_evento_por_titulo(self, titulo):
        for evento in self.__eventos:
            if evento.titulo == titulo:
                return evento
        return None

    def organiza_eventos_por_tempo(self):

            hoje = datetime.datetime.now()
            eventos_a_ocorrer = []
            eventos_ocorridos = []
            for evento in self.__eventos:
                if evento.data > hoje:
                    eventos_a_ocorrer.append(evento)
                else:
                    eventos_ocorridos.append(evento)
            return eventos_a_ocorrer, eventos_ocorridos

    def lista_eventos(self):
        
        eventos_a_ocorrer, eventos_ocorridos = self.organiza_eventos_por_tempo()
        tres_maiores_eventos = self.pega_tres_maiores_eventos()

        if self.__eventos:
            self.__tela_eventos.lista_eventos(eventos_a_ocorrer, eventos_ocorridos, tres_maiores_eventos, None)
        else:
            self.__tela_eventos.lista_eventos(None, None, None, "NÃO EXISTEM EVENTOS")

    def menu_eventos(self):
        lista_opcoes = {"bt_adicionar_evento":self.menu_adicionar_evento, "bt_voltar_menu_principal":self.voltar_menu_principal}

        eventos_a_ocorrer, eventos_ocorridos = self.organiza_eventos_por_tempo()

        opcao_escolhida = self.__tela_eventos.open(eventos_a_ocorrer, eventos_ocorridos)
        self.__tela_eventos.close()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        funcao_escolhida()
        
    def voltar_menu_principal(self):
        self.__controlador_sistema.menu_principal()
        
    def menu_adicionar_evento(self):
        lista_opcoes = {"bt_cancelar":self.menu_eventos, "bt_confirmar":self.adicionar_evento}
        
        opcao_escolhida, dados = self.__tela_adicionar_evento.open()
        print(opcao_escolhida, dados)
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        self.__tela_adicionar_evento.close()
        if opcao_escolhida == "bt_confirmar":
            funcao_escolhida(dados)
        else:
            funcao_escolhida()
    def adicionar_evento(self, dados):
        
        if not dados["it_titulo"] or not dados["it_data1"] or not dados["it_data2"] or not dados["it_data3"] or not dados["it_horario1"] or not dados["it_horario2"] or not dados["it_capacidade"] or not dados["it_local"]:
            self.__tela_adicionar_evento.mostra_mensagem("Preencha corretamente os campos")
            self.menu_adicionar_evento()
            return None

        if  int(dados["it_data1"]) == 0 or int(dados["it_data1"]) > 30 or len(dados["it_data1"]) != 2 or int(dados["it_data2"]) > 12 or int(dados["it_data2"]) == 0 or len(dados["it_data2"]) != 2 or len(dados["it_data3"]) != 4 or len(dados["it_horario1"]) != 2 or int(dados["it_horario1"]) > 23 or len(dados["it_horario2"]) != 2 or int(dados["it_horario2"]) > 59:
            self.__tela_adicionar_evento.mostra_mensagem("Preencha corretamente os campos")
            self.menu_adicionar_evento()
            return None
        
        for evento in self.__eventos:
            if evento.titulo == dados["it_titulo"]:
                self.__tela_adicionar_evento.mostra_mensagem("Preencha corretamente os campos")
                self.menu_adicionar_evento()
                return None
            
        data = datetime.datetime(int(dados["it_data3"]), int(dados["it_data2"]), int(dados["it_data1"]), int(dados["it_horario1"]), int(dados["it_horario2"]))
        novo_evento = Evento(dados["it_titulo"], data, dados["it_local"], dados["it_capacidade"])
        self.__eventos.append(novo_evento)
        self.__tela_adicionar_evento.mostra_mensagem("Evento cadastrado com sucesso")
        
        self.menu_eventos()

    def exclui_evento(self):
        self.__tela_eventos.limpa_tela()
        titulo = self.__tela_eventos.seleciona_evento_por_titulo()
        evento = self.pega_evento_por_titulo(titulo)

        if evento is not None:
            self.__eventos.remove(evento)
        else:
            self.mostra_tela_menu_eventos("ESSE EVENTO NÃO EXISTE")

        self.mostra_tela_menu_eventos("EVENTO EXCLUÍDO")

    def lista_dados_do_evento(self):
        self.__tela_eventos.limpa_tela()
        titulo = self.__tela_eventos.seleciona_evento_por_titulo()
        evento = self.pega_evento_por_titulo(titulo)

        if evento is not None:
            self.mostra_tela_edicao_eventos(evento, None)
        else:
            self.mostra_tela_menu_eventos("ESSE EVENTO NÃO EXISTE")



    #edição de evento
    def mostra_tela_edicao_eventos(self, evento, mensagem):
        self.__tela_eventos.limpa_tela()
        self.__tela_eventos.mostra_dados_do_evento(evento, mensagem)
        self.pega_opcao_de_edicao(evento)

    def pega_opcao_de_edicao(self, evento):
        #lista_opcoes = {1:self.editar_dados_do_evento(evento), 2:self.adiciona_pessoa(evento, "organizador"), 3:self.exclui_pessoa(evento, "organizador"), 4:self.adiciona_pessoa(evento, "participante"), 5:self.exclui_pessoa(evento,"participante"), 6:self.voltar_menu_eventos}
        lista_opcoes = {1:self.editar_dados_do_evento, 6:self.voltar_menu_eventos}
        
        opcao_escolhida = self.__tela_eventos.lista_opcoes_de_edicao()
        funcao_escolhida = lista_opcoes[opcao_escolhida]
        if opcao_escolhida != 6:
            funcao_escolhida(evento)
        else:
            funcao_escolhida()

    #def voltar_menu_eventos(self):
        #self.mostra_tela_menu_eventos(None)
        
    def editar_dados_do_evento(self, evento):
        self.__tela_eventos.limpa_tela()
        titulo, dia, mes, ano, hora, minuto, capacidade_maxima, local = self.__tela_eventos.pega_dados_de_evento()
        data = datetime.datetime(ano, mes, dia, hora, minuto)

        evento.titulo = titulo
        evento.data = data
        evento.capacidade_maxima = capacidade_maxima
        evento.local = local

        self.mostra_tela_edicao_eventos(evento, "EVENTO ALTERADO")

    #def adiciona_pessoa(self, evento, cargo):
     #   self.__tela_eventos.limpa_tela()
     #   cpf = self.__tela_eventos.seleciona_pessoa_por_cpf()
        
      #  if cargo == "participante":
      #      for pessoa in evento.participantes:
      #          if pessoa.cpf == cpf:
      #              self.mostra_tela_edicao_eventos(evento, "ESSA PESSOA JÁ ESTÁ NO EVENTO")
      #              return None
       #     nova_pessoa = self.pega_pessoa_por_cpf(cpf, cargo)
      #      evento.participantes.append(nova_pessoa)
      #  else:
       #     for pessoa in evento.organizadores:
       #         if pessoa.cpf == cpf:
          #          self.mostra_tela_edicao_eventos(evento, "ESSA PESSOA JÁ ESTÁ NO EVENTO")
        #    nova_pessoa = self.pega_pessoa_por_cpf(cpf, cargo)
          #  evento.organizadores.append(nova_pessoa)
    
    #def exclui_pessoa(self, evento, cargo):
     #   self.__tela_eventos.limpa_tela()
      #  cpf = self.__tela_eventos.le_cpf()
       # pessoa = self.pega_pessoa_por_cpf(cpf)

     #   if pessoa is not None:
      #      if cargo == "participante":
      #          evento.participantes.remove(pessoa)
      #      else:
      #          evento.organizadores.remove(pessoa)
      #  else:
      #      self.mostra_tela_edicao_eventos(evento, "ESSE CPF NÃO EXISTE")
            
     #   self.mostra_tela_edicao_eventos(evento, "PESSOA EXCLUÍDA")
    
    #def pega_pessoa_por_cpf(self, cpf, cargo):
     #   if cargo == "participante":
     #       pessoas = self.__controlador_sistema.retorna_participantes()
     #   else:
      #      pessoas = self.__controlador_sistema.retorna_organizadores()
      #  for pessoa in pessoas:
      #      if cpf == pessoa.cpf:
       #         return pessoa
        #    return None 