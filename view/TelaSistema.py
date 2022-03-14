from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaSistema(TelaAbstrata):
    
    def __init__(self):
        self.__window = None
    
    def init_components(self):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text('MENU PRINCIPAL', font=("Helvetica", 20))],
            [sg.Submit("EVENTOS", size=(45), key="bt_eventos")],
            [sg.Submit("PARTICIPANTES E ORGANIZADORES", size=(45), key="bt_participantes")],
            [sg.Button("SAIR", size=(45), key="bt_sair")]
                ]
        
        self.__window = sg.Window("Gerenciador de eventos", element_justification="c").Layout(layout)
        
    def open(self):
        self.init_components()
        event, values = self.__window.Read()
        return event
    
    def close(self):
        self.__window.Close() 