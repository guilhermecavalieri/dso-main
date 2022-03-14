from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaEventos(TelaAbstrata):

    def __init__(self):
        self.__window = None
        
    def init_components(self, a_ocorrer, ocorridos):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text("EVENTOS", font=("Helvetica", 20))],
            [sg.Text("__________________________________________")],
            [sg.Text("EVENTOS A OCORRER")],
            [sg.Table(values=a_ocorrer, 
                    headings=["NOME", "LOCAL", "DATA", "CAPACIDADE MÁXIMA", "PARTICIPANTES"], 
                    justification="center", 
                    expand_x=True, 
                    expand_y=True,
                    bind_return_key=True,
                    key="a_ocorrer")],
            [sg.Text("__________________________________________")],
            [sg.Text("EVENTOS OCORRIDOS")],
            [sg.Table(values=ocorridos, 
                    headings=["NOME", "LOCAL", "DATA", "CAPACIDADE MÁXIMA", "PARTICIPANTES"], 
                    justification="center", 
                    expand_x=True, 
                    expand_y=True,
                    bind_return_key=True,
                    key="ocorridos")],
            [sg.Text("__________________________________________")],
            [sg.Button("Adicionar evento", key="bt_adicionar_evento")],
            [sg.Text("", size=(1,1))],
            [sg.Submit("Voltar ao menu", key="bt_voltar_menu_principal", size=(45))]
                ]
        
        self.__window = sg.Window("Gerenciador de eventos", element_justification="c").Layout(layout)
        
    def open(self, eventos_a_ocorrer, eventos_ocorridos):
        
        a_ocorrer = []
        ocorridos = []
        
        for evento in eventos_a_ocorrer:
            a_ocorrer.append([evento.titulo, evento.local, evento.data, evento.capacidade_maxima, evento.num_participantes])
            
        for evento in eventos_ocorridos:
            ocorridos.append([evento.titulo, evento.local, evento.data, evento.capacidade_maxima, evento.num_participantes])
        
        self.init_components(a_ocorrer, ocorridos)
        event, values = self.__window.Read()
        return event, values
    
    def close(self):
        self.__window.Close()