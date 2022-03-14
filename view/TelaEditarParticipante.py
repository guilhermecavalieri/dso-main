from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaEditarParticipante(TelaAbstrata):

    def __init__(self):
        self.__window = None
        
    def init_components(self, dados):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text("Incluir participante no evento:"), sg.InputText(key="it_eventoincluido")],
            [sg.Text("Excluir participante no evento:"), sg.InputText(key="it_eventoexcluido")],
            [sg.Text("EDITAR PARTICIPANTE", font=("Helvetica", 20), justification="center")],
            [self.cria_input_de_string("Nome:", "it_nome", dados["nome"])],
            [self.cria_input_de_data("Nascimento:", "it_data1", "it_data2", "it_data3", dados["data1"], dados["data2"], dados["data3"])],
            [self.cria_input_de_string("CPF:", "it_cpf", dados["cpf"])],
            [self.cria_input_de_string("Endereço:", "it_endereco", dados["endereco"])],
            [sg.Text("Possui vacina?", size=(18)), sg.Radio("Não", "vacina", default=True, key="sem_vacina"), sg.Radio("Sim", "vacina", key="com_vacina")],
            [sg.Submit("Alterar", key="bt_alterar"), sg.Submit("Cancelar", key="bt_cancelar"), sg.Submit("Excluir", key="bt_excluir")]
                ]
        
        self.__window = sg.Window("Gerenciador de eventos", element_justification="c").Layout(layout)
        
    def open(self, dados):
        self.init_components(dados)
        while True:
            event, values = self.__window.Read()
            print (event, values)
            if event is None or event == "bt_alterar" or event == "bt_cancelar" or event =="bt_excluir":
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