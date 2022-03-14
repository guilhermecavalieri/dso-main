from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaEditarEventos(TelaAbstrata):

    def __init__(self):
        self.__window = None
        
    def init_components(self, dados):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [
            [sg.Text("EDITAR EVENTO", font=("Helvetica", 20), justification="center")],
            [self.cria_input_de_string("Título do evento:", "it_titulo", dados["titulo"])],
            [self.cria_input_de_data("Data:", "it_data1", "it_data2", "it_data3", dados["data1"], dados["data2"], dados["data3"])],
            [self.cria_input_de_horario("Horário:", "it_horario1", "it_horario2", dados["horario1"], dados["horario2"])],
            [self.cria_input_de_string("Capacidade máxima:", "it_capacidade", dados["capacidade"])],
            [self.cria_input_de_string("Local:", "it_local", dados["local"])],
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
            elif len(values["it_titulo"]) > 30:
                self.__window.Element("it_titulo").Update(values['it_titulo'][:-1])
            elif len(values["it_data1"]) > 2 or (values["it_data1"] and values["it_data1"][-1] not in ("0123456789")):
                self.__window.Element("it_data1").Update(values['it_data1'][:-1])
            elif len(values["it_data2"]) > 2 or (values["it_data2"] and values["it_data2"][-1] not in ("0123456789")):
                self.__window.Element("it_data2").Update(values['it_data2'][:-1])
            elif len(values["it_data3"]) > 4 or (values["it_data3"] and values["it_data3"][-1] not in ("0123456789")):
                self.__window.Element("it_data3").Update(values['it_data3'][:-1])
            elif len(values["it_horario1"]) > 2 or (values["it_horario1"] and values["it_horario1"][-1] not in ("0123456789")):
                self.__window.Element("it_horario1").Update(values['it_horario1'][:-1])
            elif len(values["it_horario2"]) > 2 or (values["it_horario2"] and values["it_horario2"][-1] not in ("0123456789")):
                self.__window.Element("it_horario2").Update(values['it_horario2'][:-1])
            elif len(values["it_capacidade"]) > 10 or (values["it_capacidade"] and values["it_capacidade"][-1] not in ("0123456789")):
                self.__window.Element("it_capacidade").Update(values['it_capacidade'][:-1])
            elif len(values["it_local"]) > 40:
                self.__window.Element("it_local").Update(values['it_local'][:-1])
        return event, values
            
    def close(self):
        self.__window.Close()