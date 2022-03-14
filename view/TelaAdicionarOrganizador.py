from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaAdicionarOrganizador(TelaAbstrata):

    def __init__(self):
        self.__window = None
        
    def init_components(self):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text("DADOS DO ORGANIZADOR", font=("Helvetica", 20), justification="center")],
            [self.cria_input_de_string("Nome:", "it_nome", None)],
            [self.cria_input_de_string("CPF:", "it_cpf", None)],
            [sg.Submit("Confirmar", key="bt_confirmar"), sg.Submit("Cancelar", key="bt_cancelar")]
                ]
        
        self.__window = sg.Window("Gerenciador de eventos", element_justification="c").Layout(layout)
        
    def open(self):
        self.init_components()
        while True:
            event, values = self.__window.Read()
            print (event, values)
            if event is None or event == "bt_confirmar" or event == "bt_cancelar":
                break
            elif len(values["it_nome"]) > 30 or (values["it_nome"] and (not values["it_nome"][-1].isalpha())):
                self.__window.Element("it_nome").Update(values['it_nome'][:-1])
            elif len(values["it_cpf"]) > 11 or (values["it_cpf"] and values["it_cpf"][-1] not in ("0123456789")):
                self.__window.Element("it_cpf").Update(values['it_cpf'][:-1])
        return event, values
            
    def close(self):
        self.__window.Close()