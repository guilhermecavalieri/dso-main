from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg
class TelaAdicionarParticipante(TelaAbstrata):

    def __init__(self):
        self.__window = None
        
    def init_components(self):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text("DADOS DO PARTICIPANTE", font=("Helvetica", 20), justification="center")],
            [self.cria_input_de_string("Nome:", "it_nome", None)],
            [self.cria_input_de_data("Nascimento:", "it_data1", "it_data2", "it_data3", None, None, None)],
            [self.cria_input_de_string("CPF:", "it_cpf", None)],
            [self.cria_input_de_string("Endereço:", "it_endereco", None)],
            [sg.Text("Possui vacina?", size=(18)), sg.Radio("Não", "vacina", default=True, key="sem_vacina"), sg.Radio("Sim", "vacina", key="com_vacina")],
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
            elif len(values["it_data1"]) > 2 or (values["it_data1"] and values["it_data1"][-1] not in ("0123456789")):
                self.__window.Element("it_data1").Update(values['it_data1'][:-1])
            elif len(values["it_data2"]) > 2 or (values["it_data2"] and values["it_data2"][-1] not in ("0123456789")):
                self.__window.Element("it_data2").Update(values['it_data2'][:-1])
            elif len(values["it_data3"]) > 4 or (values["it_data3"] and values["it_data3"][-1] not in ("0123456789")):
                self.__window.Element("it_data3").Update(values['it_data3'][:-1])
            elif len(values["it_cpf"]) > 11 or (values["it_cpf"] and values["it_cpf"][-1] not in ("0123456789")):
                self.__window.Element("it_cpf").Update(values['it_cpf'][:-1])
            elif len(values["it_endereco"]) > 40:
                self.__window.Element("it_endereco").Update(values['it_endereco'][:-1])
        return event, values
            
    def close(self):
        self.__window.Close()