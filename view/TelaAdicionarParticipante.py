from multiprocessing.sharedctypes import Value
from optparse import Values
from pydoc import visiblename
from view.TelaAbstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaAdicionarParticipante(TelaAbstrata):

    def __init__(self):
        self.__window = None
        
    def init_components(self):
        sg.ChangeLookAndFeel("Reddit")
        
        layout = [

        
    def open(self):

            
    def close(self):
        self.__window.Close()