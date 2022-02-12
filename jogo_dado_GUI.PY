from random import randint
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self,):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?'),],
            [sg.Button('sim'),sg.Button('não')]
        ]


    def Iniciar(self):

        # Criar a janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout)

        while True:

            # ler os valores da telai
            self.eventos, self.valores = self.janela.Read()
            if self.eventos == 'sim':
                self.GerarValorDado()
            elif self.eventos == 'não':
                sg.popup('Agredecemos a sua participação!')
                break


    def GerarValorDado(self):
        resultado = randint(self.valor_minimo,self.valor_maximo)
        sg.popup('VALOR SORTEADO', resultado)
    

simulador = SimuladorDeDado()
simulador.Iniciar()


    
