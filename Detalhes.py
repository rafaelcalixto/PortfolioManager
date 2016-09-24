import tkinter as tk
from tkinter import ttk

import Adicionar as add
import AvalPort as ap
import LoadInfos as li

import ast

class Detalhes():
    def __init__(self, tela_old, idProj, Portfolio):
        self.idProj = idProj
        self.tela_old = tela_old
        self.tela = tk.Tk()
        self.Portfolio = Portfolio
        self.LoadInfos = li.LoadInfos()

        #####  FUNÇÃO PARA RETORNAR AS INFOS DOS PROJETOS  #####
        self.dictLinhasPort, self.dictLinhasAval, self.tamTela = self.LoadInfos.infosProj(self.idProj)

        ###########  BARRA DE ROLAGEM  #############
        self.subTela = tk.Canvas(self.tela, width = 600, height = self.tamTela)
        self.canvas = tk.Canvas(self.subTela, width = 600, height = self.tamTela)
        self.frameTela = tk.Frame(self.canvas, width = 600, height = self.tamTela)

        self.fontTitulo = ('Arial', 16)
        self.fontCampTit = ('Verdana', 12)
        self.fontCampInfo = ('Arial', 14)
        
    def form(self):
        self.tela.wm_title('Detalhes do Projeto')
        self.tela.wm_minsize(width = 600, height = 500)
        
        roll = ttk.Scrollbar(self.subTela, orient = 'vertical', command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = roll.set)

        roll.pack(side = 'right', fill = 'y')
        self.canvas.pack(side = 'left', fill = 'both', expand = True)

        self.canvas.create_window((4,4), window = self.frameTela, anchor = 'nw', tags = 'frameTela')
        self.frameTela.bind('<Configure>', self.canvas.configure(scrollregion = self.canvas.bbox('all')))

        self.subTela.pack(side='left', fill = 'y')

        #############  INFORMAÇÕES DO PROJETO  ###############

        ########  AJUSTAR O TAMANHO DO TÍTULO DO PROJETO PARA A TELA  #########
        titulo, tamFonte = self.LoadInfos.formatText(self.dictLinhasPort['projeto'], 22, 40, 80)

        tk.Label(self.frameTela, text = titulo, font = ('Ariel Black', tamFonte)).place(x = 5, y = 20, width = 590)

        ttk.Separator(self.frameTela, orient = 'horizontal').place(x = 20, y = 120, width = 560)

        ########  BOTÃO PARA EDITAR  ########
        editar = tk.Button(self.frameTela,
                           text = 'Editar',
                           font = self.fontCampTit,
                           command = lambda: add.Formulario(self.Portfolio, self.tela_old, infosProj = self.dictLinhasPort, tela_dead = self.tela).form()
                           ).place(x = 520, y = 80)

        ########  ÁREA  #########
        tk.Label(self.frameTela, text = 'Área:', font = self.fontCampTit).place(x = 30, y = 140)
        tk.Label(self.frameTela, text = self.dictLinhasPort['area'], font = self.fontCampInfo).place(x = 30, y = 170)

        ########  SUBAREA  #########
        tk.Label(self.frameTela, text = 'Sub Área:', font = self.fontCampTit).place(x = 250, y = 140)
        tk.Label(self.frameTela, text = self.dictLinhasPort['subarea'], font = self.fontCampInfo).place(x = 250, y = 170)

        ########  TIPO  #########
        tk.Label(self.frameTela, text = 'Tipo:', font = self.fontCampTit).place(x = 460, y = 140)
        tk.Label(self.frameTela, text = self.dictLinhasPort['tipo'], font = self.fontCampInfo).place(x = 460, y = 170)

        ########  FUNCIONAL RESPONSÁVEL  #########
        tk.Label(self.frameTela, text = 'Funcional Responsável:', font = self.fontCampTit).place(x = 20, y = 270)
        funcResp, tamFonte = self.LoadInfos.formatText(self.dictLinhasPort['responsavel'])
        tk.Label(self.frameTela, text = funcResp, font = ('Arial', tamFonte)).place(x = 20, y = 300)

        ########  STATUS  #########
        tk.Label(self.frameTela, text = 'Status:', font = self.fontCampTit).place(x = 250, y = 270)
        campStatus, tamFonte = self.LoadInfos.formatText(self.dictLinhasPort['status'])
        tk.Label(self.frameTela, text = campStatus, font = ('Arial', tamFonte)).place(x = 250, y = 300)

        ########  TICKET  #########
        tk.Label(self.frameTela, text = 'Chamado CA:', font = self.fontCampTit).place(x = 470, y = 270)
        tk.Label(self.frameTela, text = self.dictLinhasPort['ticket'], font = self.fontCampInfo).place(x = 470, y = 300)

        ########  GERENCIA  #########
        tk.Label(self.frameTela, text = 'Gerência:', font = self.fontCampTit).place(x = 30, y = 380)
        gerencia, tamFonte = self.LoadInfos.formatText(self.dictLinhasPort['gerencia'], 14, 12, 24)
        tk.Label(self.frameTela, text = gerencia, font = ('Arial', tamFonte)).place(x = 30, y = 410)

        ########  BUDGET  #########
        tk.Label(self.frameTela, text = 'Budget:', font = self.fontCampTit).place(x = 250, y = 380)
        tk.Label(self.frameTela, text = self.dictLinhasPort['budget'], font = self.fontCampInfo).place(x = 250, y = 410)

        ########  SOLICITANTE  #########
        tk.Label(self.frameTela, text = 'Solicitante:', font = self.fontCampTit).place(x = 460, y = 380)
        solicitante, tamFonte = self.LoadInfos.formatText(self.dictLinhasPort['solicitante'], 14, 12, 24)
        tk.Label(self.frameTela, text = solicitante, font = ('Arial', tamFonte)).place(x = 460, y = 410)

        #############  AVALIAÇÃO DO PROJETO  ###############

        ttk.Separator(self.frameTela, orient = 'horizontal').place(x = 20, y = 470, width = 560)

        if self.dictLinhasAval['esforco'] == 'Projeto não avaliado':
            tk.Label(self.frameTela,
                     text = self.dictLinhasAval['esforco'],
                     font = ('Areal black', 22),
                     fg = 'red',
                     width = 30,
                     height = 2).place(x = 150, y = 500, width = 300)
        else:

            ########  BOTÃO PARA EDITAR  ########
            editar = tk.Button(self.frameTela,
                              text = 'Editar',
                              font = self.fontCampTit,
                              command = lambda: ap.Avaliar(self.tela, self.dictLinhasPort['id'], self.dictLinhasPort['projeto'], self.dictLinhasPort['tipo'], self.dictLinhasPort['area'], self.dictLinhasAval, self.tela).form()
                              ).place(x = 520, y = 490)
            ########  COMPLEXIDADE  ########
            tk.Label(self.frameTela,
                     text = 'COMPLEXIDADE',
                     bg = '#99ccff',
                     bd = 2,
                     relief = 'solid',
                     font = self.fontCampInfo,
                     width = 30,
                     height = 2).place(x = 22, y = 530, width = 280, height = 50)
            ##############  1  ###############
            esforco, tamFonte = self.LoadInfos.formatText(self.dictLinhasAval['esforco'], 13, 35, 65)
            tk.Label(self.frameTela,
                     text = esforco,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', tamFonte),
                     width = 30,
                     height = 2).place(x = 22, y = 578, width = 280, height = 50)
            ##############  2  ###############
            conf = self.dictLinhasAval['conf']
            if conf != 'Não há fornecedores':
                conf = conf + ' nos fornecedores'
            tk.Label(self.frameTela,
                     text = conf,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 22, y = 626, width = 280, height = 50)
            ##############  3  ###############
            if self.dictLinhasAval['hab'] != 'Não serão utilizados profissionais internos':
                hab = 'Profissionais internos ' + self.dictLinhasAval['hab'].lower()
            hab, tamFonte = self.LoadInfos.formatText(self.dictLinhasAval['hab'], 13, 35, 65)
            tk.Label(self.frameTela,
                     text = hab,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', tamFonte),
                     width = 30,
                     height = 2).place(x = 22, y = 674, width = 280, height = 50)
            ##############  4  ###############
            numProfs = 'Profissionais técnicos envolvidos: ' + self.dictLinhasAval['numProfs']
            numProfs, tamFonte = self.LoadInfos.formatText(numProfs, 13, 35, 65)
            tk.Label(self.frameTela,
                     text = numProfs,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', tamFonte),
                     width = 30,
                     height = 2).place(x = 22, y = 722, width = 280, height = 50)
            ##############  5  ###############
            escop = self.dictLinhasAval['escop'] + ' tendência de variação do escopo'
            tk.Label(self.frameTela,
                     text = escop,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 22, y = 770, width = 280, height = 50)
            ##############  6  ###############
            comp, tamFonte = self.LoadInfos.formatText(self.dictLinhasAval['comp'], 13, 35, 65)
            tk.Label(self.frameTela,
                     text = comp,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', tamFonte),
                     width = 30,
                     height = 2).place(x = 22, y = 818, width = 280, height = 50)
            ##############  7  ###############
            dispTec = self.dictLinhasAval['dispTec'] + ' disponibilidade de recursos tecnológicos'
            dispTec, tamFonte = self.LoadInfos.formatText(self.dictLinhasAval['dispTec'], 13, 35, 65)       
            tk.Label(self.frameTela,
                     text = dispTec,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', tamFonte),
                     width = 30,
                     height = 2).place(x = 22, y = 866, width = 280, height = 50)
            ##############  8  ###############
            difTec = self.dictLinhasAval['difTec'] + ' dificuldade técnica do projeto'
            tk.Label(self.frameTela,
                     text = difTec,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 22, y = 914, width = 280, height = 50)
            ##############  9  ###############
            impact = self.dictLinhasAval['impact'] + ' impacto no \nprocesso de negócio atual'
            tk.Label(self.frameTela,
                     text = impact,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 22, y = 962, width = 280, height = 50)
            ##############  total complexidade ###############
            tk.Label(self.frameTela,
                     text = 'Grau de complexidade: ' + self.dictLinhasAval['complexidade'],
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 22, y = 1010, width = 280, height = 50)
            ########  CRITICIDADE  ########
            tk.Label(self.frameTela,
                     text = 'CRITICIDADE',
                     bg = '#99ccff',
                     bd = 2,
                     relief = 'solid',
                     font = self.fontCampInfo,
                     width = 30,
                     height = 2).place(x = 300, y = 530, width = 280, height = 50)
            ##############  1  ###############
            ativVital = self.dictLinhasAval['ativVital'] + '\ncom atividade de negócio vital'
            tk.Label(self.frameTela,
                     text = ativVital,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 300, y = 578, width = 280, height = 50)
            ##############  2  ###############
            numArea = self.dictLinhasAval['numArea']
            if numArea != 'Abrangência global':
                numArea += '\nbeneficiada(s) com o projeto'
            tk.Label(self.frameTela,
                     text = numArea,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 300, y = 626, width = 280, height = 50)
            ##############  3  ###############
            relMetas = self.dictLinhasAval['relMetas'] + '\nas metas atuais de diretoria'
            tk.Label(self.frameTela,
                     text = relMetas,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 300, y = 674, width = 280, height = 50)
            ##############  4  ###############
            tk.Label(self.frameTela,
                     text = 'ROI = ' + self.dictLinhasAval['roi'],
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 300, y = 722, width = 280, height = 50)
            ##############  5  ###############
            tk.Label(self.frameTela,
                     text = self.dictLinhasAval['mustDo'],
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 300, y = 770, width = 280, height = 50)
            ##############  6  ###############
            just, tamFonte = self.LoadInfos.formatText(self.dictLinhasAval['just'], 13, 35, 65)
            tk.Label(self.frameTela,
                     text = just,
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', tamFonte),
                     width = 30,
                     height = 2).place(x = 300, y = 818, width = 280, height = 50)
            ##############  total criticidade  ###############
            tk.Label(self.frameTela,
                     text = 'Grau de criticidade: ' + self.dictLinhasAval['criticidade'],
                     bg = 'white',
                     bd = 2,
                     relief = 'solid',
                     font = ('Verdana', 9),
                     width = 30,
                     height = 2).place(x = 300, y = 866, width = 280, height = 50)
