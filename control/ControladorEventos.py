import datetime
from view.TelaAdicionarEvento import TelaAdicionarEventos
from view.TelaEditarEvento import TelaEditarEventos
from view.TelaEventos import TelaEventos
from model.evento import Evento
from daos.DAOEvento import DAOEvento

class ControladorEventos():

    def __init__(self, controlador_sistema):
        #self.__eventos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_eventos = TelaEventos()
        self.__tela_adicionar_evento = TelaAdicionarEventos()
        self.__tela_editar_evento = TelaEditarEventos()
        self.__dao = DAOEvento()

    def organiza_eventos_por_tempo(self):

            hoje = datetime.datetime.now()
            eventos_a_ocorrer = []
            eventos_ocorridos = []
            for evento in self.__dao.get_all():
                if evento.data > hoje:
                    eventos_a_ocorrer.append(evento)
                else:
                    eventos_ocorridos.append(evento)
            return eventos_a_ocorrer, eventos_ocorridos

    def menu_eventos(self):
        lista_opcoes = {"bt_adicionar_evento":self.menu_adicionar_evento, "bt_voltar_menu_principal":self.voltar_menu_principal}

        eventos_a_ocorrer, eventos_ocorridos = self.organiza_eventos_por_tempo()

        opcao_escolhida, valores = self.__tela_eventos.open(eventos_a_ocorrer, eventos_ocorridos)
        
        print(valores)
        self.__tela_eventos.close()
        if opcao_escolhida != "bt_adicionar_evento" and opcao_escolhida != "bt_voltar_menu_principal":
            if opcao_escolhida == "a_ocorrer":
                linha = valores["a_ocorrer"][0]
                evento_para_editar = eventos_a_ocorrer[linha]
            else:
                linha = valores["ocorridos"][0]
                evento_para_editar = eventos_ocorridos[linha]  
            self.menu_editar_evento(evento_para_editar)
        else:
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
        
    def menu_editar_evento(self, evento_para_editar):
        
        dados_evento = {"titulo":evento_para_editar.titulo, "data1":evento_para_editar.data.day, "data2":evento_para_editar.data.month, "data3":evento_para_editar.data.year, "horario1":evento_para_editar.data.hour, "horario2":evento_para_editar.data.minute, "capacidade":evento_para_editar.capacidade_maxima, "local":evento_para_editar.local}
        opcao_escolhida, dados_novos = self.__tela_editar_evento.open(dados_evento)
        if opcao_escolhida == "bt_alterar":
            self.__tela_editar_evento.close()
            self.editar_evento(dados_novos, evento_para_editar)
        elif opcao_escolhida == "bt_cancelar":
            self.__tela_editar_evento.close()
            self.menu_eventos()
        elif opcao_escolhida == "bt_excluir":
            self.__tela_editar_evento.close()
            self.excluir_evento(evento_para_editar)
            self.menu_eventos()
            
    def editar_evento(self, dados, evento):
        if dados["it_titulo"] == "" or dados["it_data1"] == "" or dados["it_data2"]=="" or dados["it_data3"]=="" or dados["it_horario1"]=="" or dados["it_horario2"]=="" or dados["it_capacidade"]=="" or dados["it_local"]=="":
            self.__tela_editar_evento.mostra_mensagem("Preencha corretamente os campos")
            self.menu_editar_evento(evento)
            return None
        
        if  int(dados["it_data1"]) == 0 or int(dados["it_data1"]) > 30 or len(dados["it_data1"]) != 2 or int(dados["it_data2"]) > 12 or int(dados["it_data2"]) == 0 or len(dados["it_data2"]) != 2 or len(dados["it_data3"]) != 4 or len(dados["it_horario1"]) != 2 or int(dados["it_horario1"]) > 23 or len(dados["it_horario2"]) != 2 or int(dados["it_horario2"]) > 59:
            self.__tela_editar_evento.mostra_mensagem("Preencha corretamente os campos")
            self.menu_editar_evento(evento)
            return None
        
        evento.titulo = dados["it_titulo"]
        data = datetime.datetime(int(dados["it_data3"]), int(dados["it_data2"]), int(dados["it_data1"]), int(dados["it_horario1"]), int(dados["it_horario2"]))
        evento.data = data
        evento.capacidade_maxima = dados["it_capacidade"]
        evento.local = dados["it_local"]
        self.__tela_editar_evento.mostra_mensagem("Evento editado com sucesso")
        
        self.menu_eventos()
        
    def menu_adicionar_evento(self):
        
        opcao_escolhida, dados = self.__tela_adicionar_evento.open()
        print(opcao_escolhida, dados)
        self.__tela_adicionar_evento.close()
        if opcao_escolhida == "bt_confirmar":
            self.adicionar_evento(dados)
        else:
            self.menu_eventos()
            
    def adicionar_evento(self, dados):
        
        if not dados["it_titulo"] or not dados["it_data1"] or not dados["it_data2"] or not dados["it_data3"] or not dados["it_horario1"] or not dados["it_horario2"] or not dados["it_capacidade"] or not dados["it_local"]:
            self.__tela_adicionar_evento.mostra_mensagem("Preencha corretamente os campos")
            self.menu_adicionar_evento()
            return None

        if  int(dados["it_data1"]) == 0 or int(dados["it_data1"]) > 30 or len(dados["it_data1"]) != 2 or int(dados["it_data2"]) > 12 or int(dados["it_data2"]) == 0 or len(dados["it_data2"]) != 2 or len(dados["it_data3"]) != 4 or len(dados["it_horario1"]) != 2 or int(dados["it_horario1"]) > 23 or len(dados["it_horario2"]) != 2 or int(dados["it_horario2"]) > 59:
            self.__tela_adicionar_evento.mostra_mensagem("Preencha corretamente os campos")
            self.menu_adicionar_evento()
            return None
        
        for evento in self.__dao.get_all():
            if evento.titulo == dados["it_titulo"]:
                self.__tela_adicionar_evento.mostra_mensagem("Esse evento já existe")
                self.menu_adicionar_evento()
                return None
            
        data = datetime.datetime(int(dados["it_data3"]), int(dados["it_data2"]), int(dados["it_data1"]), int(dados["it_horario1"]), int(dados["it_horario2"]))
        novo_evento = Evento(dados["it_titulo"], data, dados["it_local"], dados["it_capacidade"])
        self.__dao.add(novo_evento)
        self.__tela_adicionar_evento.mostra_mensagem("Evento cadastrado com sucesso")
        
        self.menu_eventos()

    def excluir_evento(self, evento):

        self.__dao.remove(evento)
        self.__tela_editar_evento.mostra_mensagem("EVENTO EXCLUÍDO")
        
    def voltar_menu_principal(self):
        self.__controlador_sistema.menu_principal()