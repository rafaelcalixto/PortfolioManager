import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast

import LoadInfos as li
import SetupCampos as sc

class TelaSetup():
    def __init__(self, Portfolio, tela = None):
        self.fontTitulo = ('Arial Black', 12)
        self.fontCampos = ('Verdana', 10)

        ####  CRIAÇÃO DOS OBJETOS  ####
        self.Portfolio = Portfolio
        self.Setup = sc.SetupCampos(self.Portfolio)
        self.tipo, self.area = self.Portfolio.infoPort()
        
        self.tela = tela
        self.pesos = ['','1','2','3','4','5','6','7','8','9']
        
    #######  PAGINA INICIAL DO SETUP #######
    def setup(self):
        self.tela = tk.Tk()
        self.tela.wm_title('Setup')
        self.tela.wm_minsize(width = 300, height = 350)
            
        titulo = tk.Label(self.tela, text='Setup', font= self.fontTitulo)
        titulo.place(x = 120, y = 20, width = 60)

        setupCaracProj = ttk.Button(self.tela, text = 'Características\n    do Projeto',
                                 command = lambda: self.Setup.caracProj(self.tela)
                                 ).place(x = 100, y = 80, width = 100, height = 50)

        setupAvalCrit = ttk.Button(self.tela, text = '  Avaliação de\n complexidade',
                                 command = lambda: self.Setup.avalComp(self.tela)
                                 ).place(x = 100, y = 160, width = 100, height = 50)

        setupAvalComp = ttk.Button(self.tela, text = '  Avaliação de\n   criticidade',
                                 command = lambda: self.Setup.avalCrit(self.tela)
                                 ).place(x = 100, y = 240, width = 100, height = 50)
        
    def gerarSubTelas(self, maiorTela, textoLabel):
        ###########  CRIAÇÃO DOS CANVAS  #############
        subTela = tk.Canvas(self.tela, width = 300, height = 400)
        canvas = tk.Canvas(subTela, width = 300, height = 400)
        frameTela = tk.Frame(canvas, width = 300, height = maiorTela)
        
        telaLF = tk.LabelFrame(frameTela,
                          text = textoLabel,
                          bd = 2,
                          relief = 'solid',
                          font = self.fontTitulo,
                          width = 250,
                          height = (maiorTela - 100))
        
        return subTela, canvas, frameTela, telaLF

    def gerarCamposAval(self, telaLF, titulo):
        campoL = tk.Label(telaLF, text = titulo, bg = 'white', bd = 2, relief = 'solid', font = self.fontCampos, width = 30, height = 2)
        campoLP = tk.Label(telaLF, text = 'Peso:', font = self.fontCampos)
        campoP = ttk.Combobox(telaLF, state = 'readonly', values= self.pesos)
        campoLV = tk.Label(telaLF, text = 'Valor:', font = self.fontCampos)
        campoV = tk.Entry(telaLF)

        return campoL, campoLP, campoP, campoLV, campoV

    def gerarSetupAval(self, telaLF, idCampo, titulo, listValores, funcAltPeso, funcDeletar, funcAltValor, tipoAval):
        campoLabel = tk.Label(telaLF, text = titulo, bg = 'white', bd = 2, relief = 'solid', font = self.fontCampos, width = 30, height = 2)
        campoLista = ttk.Combobox(telaLF, text = titulo, state = 'readonly', values = listValores)
        campoVal = tk.Button(telaLF, text = 'Alterar Valor', command = lambda: funcAltValor(self.tipo, tipoAval, campoLista.get(), idCampo, titulo))
        campoPeso = tk.Button(telaLF, text = 'Peso', command = lambda: funcAltPeso(self.tipo, tipoAval, idCampo, titulo))
        campoDel = tk.Button(telaLF, text = 'Deletar', command = lambda: funcDeletar(self.tela, self.tipo, tipoAval, idCampo, campoLista.get()))

        return campoLabel, campoLista, campoVal, campoPeso, campoDel

    def gerarMiniTela(self, titulo, valores, key):
        tela = tk.Tk()
        tela.wm_title('Setup')
        tela.wm_minsize(width = 165, height = 115)

        valOldLabel = tk.Label(tela, text = titulo + 'antigo:', font = self.fontCampos)
        valOld = tk.Label(self.tela, text = valores[key], bg = 'white', bd = 2, relief = 'solid', font = self.fontTitulo)
        valNewLabel = tk.Label(self.tela, text = titulo + 'novo:', font = self.fontCampos)
        
        return tela, valOldLabel, valOld, valNewLabel
