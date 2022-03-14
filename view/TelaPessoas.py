from datetime import datetime
from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPessoas(TelaAbstrata):

    
    def __init__(self):
        self.__window = None
        
    def init_components(self, nome_cpf_participantes, nome_cpf_organizadores):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text("MENU PESSOAS", font=("Helvetica", 20))],
            [sg.Text("__________________________________________")],
            [sg.Text("PARTICIPANTES")],
            [sg.Table(values=nome_cpf_participantes, 
                    headings=["NOME", "CPF", "VACINADO"], 
                    justification="center", 
                    expand_x=True, 
                    expand_y=True,
                    key="participantes",
                    bind_return_key=True)],
            [sg.Button("Adicionar participante", key="bt_adicionar_participante")],
            [sg.Text("__________________________________________")],
            [sg.Text("ORGANIZADORES")],
            [sg.Table(values=nome_cpf_organizadores,
                    headings=["NOME", "CPF"], 
                    justification="center", 
                    expand_x=True, 
                    expand_y=True,
                    key="organizadores",
                    bind_return_key=True)],
            [sg.Button("Adicionar organizador", key="bt_adicionar_organizador")],
            [sg.Text("", size=(1,1))],
            [sg.Submit("Voltar ao menu", key="bt_voltar_menu_principal", size=(45))]
                ]
        
        self.__window = sg.Window("Gerenciador de eventos", element_justification="c").Layout(layout)

    def open(self, participantes, organizadores):
            
        nome_cpf_participantes = []
        nome_cpf_organizadores = []
        
        for participante in participantes:
            if participante.vacina == True:
                nome_cpf_participantes.append([participante.nome, participante.cpf, "SIM"])
            else:
                nome_cpf_participantes.append([participante.nome, participante.cpf, "NÃO"])
            
        for organizador in organizadores:
            nome_cpf_organizadores.append([organizador.nome, organizador.cpf])
        
        self.init_components(nome_cpf_participantes, nome_cpf_organizadores)
        event, values = self.__window.Read()
        return event, values
    
    def close(self):
        self.__window.Close()