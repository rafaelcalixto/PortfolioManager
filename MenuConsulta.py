import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast

import ConsultPort as cp
import AvalPort as ap
import Detalhes as d
import ExportExcel as ee
import Adicionar as add
import SetupTela as st
import LoadInfos as li
import ClassePortfolio as port

class MenuPort:
    def __init__(self, tipo, area, tela):
        ## VARIÁVES ##
        self.tipo = tipo
        self.area = area
        self.tela = tela
        self.listIds = []
        self.fontTitulo = ('Arial', 16)
        self.fontCampos = ('Verdana', 12)

        ##########  CRIA O OBJETO PORTFOLIO  ###########
        self.Portfolio = port.Portfolio(self.tipo, self.area)

        self.LoadInfos = li.LoadInfos()
        self.TelaSetup = st.TelaSetup(self.Portfolio)
        self.ClassExcel = ee.ClassExcel()

        ###########  ELEMENTOS DO MENU COM A LISTA DE PROJETOS  ###########
        self.projsArea = self.Portfolio.load() ## CARREGA A LISTA DE PROJETOS DESTE TIPO E ÁREA E O TAMANHO DE TELA NECESSÁRIO ##
        self.tamTela = (len(self.projsArea) * 48) + 50
        self.posx = 5
        self.posy = -25
        self.img = tk.PhotoImage(file = 'seta_sel.png')
        self.subTela = tk.Canvas(tela, width = 22, height = 800)
        self.canvas = tk.Canvas(self.subTela, width = 22, height = 1000)
        self.listIdsAval = self.LoadInfos.criarListAval('id') ## ALERTA PARA PROJETOS NÃO AVALIADOS ##

    def listaPort(self):
        tk.Label(self.tela, text = 'Portfolio ' + self.area, font= self.fontTitulo).place(x = 220, y = 20, width = 230)
        
        addProj = ttk.Button(self.tela, text = 'Adicionar ' + self.tipo,
                             command = lambda: add.Formulario(self.Portfolio, self.tela).form()).place(x = 280, y = 70, width = 120)

        criarPort = tk.Button(self.tela,
                              text = 'Exportar para .xls',
                              command = lambda: self.ClassExcel.exportPort(self.listIds, self.area)).place(x = 510, y = 90)
        
        setupPort = ttk.Button(self.tela, text = 'Setup', command = lambda: self.TelaSetup.setup()).place(x = 550, y = 10)

    def atualizaPort(self):
        ##########  FUNÇÃO CENTRAL PARA CHAMAR AS FUNÇÕES DOS BOTÕES  ##########
        def funcBotoes(bot, marca, projsArea):
            posi = int((projCab.winfo_pointery() - projCab.winfo_rooty() - 45) / 48)      #####  Calcula a posição    
            idProj = self.listIds[posi]                                                   #####  do mouse na tela para
                                                                                          #####  saber qual botão foi clicado
            for dictLinhasPort in projsArea:
                if dictLinhasPort['id'] == idProj:
                    nomeProj = dictLinhasPort['projeto']

            ######  MOSTRA O PROJETO SELECIONADO  #######
            marca.place(x = -5, y = (posi * 48) + 20, height = 36)

            if bot == 'd':                                                              
                self.LoadInfos.delProj(self.tela, idProj, nomeProj)
                mc.MenuPort(self.tipo, self.area, self.tela).atualizaPort()
            elif bot == 'e':
                d.Detalhes(self.tela, idProj, self.Portfolio).form()
            elif bot == 'a':
                ap.Avaliar(self.tela, idProj, nomeProj, self.tipo, self.area).form()
        ##########  CABECALHO  ############
        projCab = tk.LabelFrame(self.canvas,
                          text = self.tipo + 's',
                          bd = 2,
                          relief = 'solid',
                          font = self.fontTitulo,
                          width = 570,
                          height = self.tamTela)
        self.posy += - 10
        ###########  ELEMENTOS DO MENU COM A LISTA DE PROJETOS  ###########
        self.listIdsAval = self.LoadInfos.criarListAval('id') ## ALERTA PARA PROJETOS NÃO AVALIADOS ##
        self.projsArea = self.Portfolio.load()
        self.tamTela = (len(self.projsArea) * 48) + 50

        ##########  LINHAS  ############
        for dictLinhasPort in self.projsArea:
            cor = 'red'
            self.posy += 48
            self.listIds.append(dictLinhasPort['id'])

            #######  CASO O NOME SEJA GRANDE DEMAIS  #######
            nomeProj = dictLinhasPort['projeto']
            if len(dictLinhasPort['projeto']) > 35:
                nomeProj = nomeProj[:32] + '...'

            tk.Label(projCab,
                      text = nomeProj,
                      bg = 'white',
                      bd = 2,
                      relief = 'solid',
                      font = self.fontCampos,
                      width = 30,
                      height = 2).place(x = self.posx, y = self.posy, width = 350, height = 50)

            #######  MARCA PARA INDICAR PROJETO SELECIONADO  ########
            marca = tk.Label(projCab, image = self.img, bd = 1, relief = 'solid')

            #######  LISTA DE PROJETOS DA ÁREA SELECIONADA  #######
            if dictLinhasPort['id'] in self.listIdsAval:
                cor = 'black'

            avaliar = tk.Button(projCab,
                                text = 'Avaliar',
                                fg = cor,
                                command = lambda:funcBotoes('a', marca, self.projsArea)).place(x = (self.posx + 355),
                                                            y = (self.posy + 6),
                                                            width = 60,
                                                            height = 38)
            
            editar = tk.Button(projCab,
                               text = 'Detalhes',
                               command = lambda:funcBotoes('e', marca, self.projsArea)).place(x = (self.posx + 420),
                                                           y = (self.posy + 6),
                                                           width = 60,
                                                           height = 38)

            deletar = tk.Button(projCab,
                                text = 'Deletar',
                                command = lambda:funcBotoes('d', marca, self.projsArea)).place(x = (self.posx + 485),
                                                            y = (self.posy + 6),
                                                            width = 60,
                                                            height = 38)
                        
        roll = ttk.Scrollbar(self.subTela, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = roll.set)
        
        roll.pack(side = 'right', fill = 'y')
        self.canvas.pack(side = 'left', fill = 'both', expand = True)
        
        self.canvas.create_window((4,4), window = projCab, anchor = 'nw', tags = 'projCab')
        projCab.bind('<Configure>', self.canvas.configure(scrollregion = self.canvas.bbox('all')))

        self.subTela.place(x = 20, y = 120, width = 600, height = 360)
