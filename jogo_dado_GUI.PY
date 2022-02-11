from random import randint
import PySimpleGUI as sg

class SimuladorDeDado:
    def __init__(self,):
        self.valor_minimo = 1
        self.valor_maximo = 6
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
        self.size = [500, 500]

    def Iniciar(self):
        # Criar a janela
        self.janela = sg.Window('Simulador de Dado',layout=self.layout, size=self.size)
        # ler os valores da tela
        self.eventos, self.valores = self.janela.Read()
        try:
            if self.eventos == 'sim' or self.eventos== 's':
                self.GerarValorDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agredecemos a sua participação!')
            else:
                print('Favor digitar somente sim ou não!')
        except:
            print('Ocorreu um erro com sua resposta!')


    def GerarValorDado(self):
        valor_sorteado = randint(self.valor_minimo,self.valor_maximo)
        print(f'O valor sorteado foi {valor_sorteado}\n')

        
simulador = SimuladorDeDado()
simulador.Iniciar()


    
