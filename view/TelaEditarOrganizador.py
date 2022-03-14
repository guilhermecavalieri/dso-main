from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaEditarOrganizador(TelaAbstrata):

    def __init__(self):
        self.__window = None
        
    def init_components(self, dados):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text("Incluir participante no evento:"), sg.InputText(key="it_eventoincluido")],
            [sg.Text("Excluir participante no evento:"), sg.InputText(key="it_eventoexcluido")],
            [sg.Text("EDITAR ORGANIZADOR", font=("Helvetica", 20), justification="center")],
            [self.cria_input_de_string("Nome:", "it_nome", dados["nome"])],
            [self.cria_input_de_string("CPF:", "it_cpf", dados["cpf"])],
            [sg.Submit("Alterar", key="bt_alterar"), sg.Submit("Cancelar", key="bt_cancelar"), sg.Submit("Excluir", key="bt_excluir")]
                ]
        
        self.__window = sg.Window("Gerenciador de eventos", element_justification="c").Layout(layout)
        
    def open(self, dados):
        self.init_components(dados)
        while True:
            event, values = self.__window.Read()
            print (event, values)
            if event is None or event == "bt_alterar" or event == "bt_cancelar" or event == "bt_excluir":
                break
            elif len(values["it_nome"]) > 30 or (values["it_nome"] and (not values["it_nome"][-1].isalpha())):
                self.__window.Element("it_nome").Update(values['it_nome'][:-1])
            elif len(values["it_cpf"]) > 11 or (values["it_cpf"] and values["it_cpf"][-1] not in ("0123456789")):
                self.__window.Element("it_cpf").Update(values['it_cpf'][:-1])
        return event, values
            
    def close(self):
        self.__window.Close()