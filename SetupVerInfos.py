import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast

import SetupTela as st
import LoadInfos as li

class SetupVerInfos():
    def __init__(self, Portfolio):
        self.fontTitulo = ('Arial Black', 12)
        self.fontCampos = ('Verdana', 10)
        self.fontBotao = ('Arial Black', 10)
        self.Portfolio = Portfolio
        self.LoadInfos = li.LoadInfos()
        self.tipo, self.area = self.Portfolio.infoPort()
        self.FuncSetup = FuncSetup
        self.alterarPeso = self.FuncSetup.alterarPeso
        self.deletar = self.FuncSetup.deletar
        self.alterarValor = self.FuncSetup.alterarValor
        self.infoForm = self.Portfolio.infoForm()
        self.infoAvalComplex = self.Portfolio.infoAvalComplex()
        self.infoAvalCritic = self.Portfolio.infoAvalCritic()
        self.camposCarac, self.camposComplex, self.camposCritic = self.LoadInfos.loadConfigPort('AllFields')
        self.camposCarac = ast.literal_eval(self.camposCarac['valores'])
        self.camposComplex = ast.literal_eval(self.camposComplex['valores'])
        self.camposCritic = ast.literal_eval(self.camposCritic['valores'])
        self.lerInfos = None
        self.TelaSetup = None

    #######  FUNÇÃO PARA SETUP DE PROJETO #######
    def infosCarac(self, tela):
        if self.TelaSetup == None:
            self.TelaSetup = st.TelaSetup(self.Portfolio, tela)
            self.FuncSetup(self.TelaSetup)

        subTela, canvas, frameTela, infosProj = self.TelaSetup.gerarSubTelas(550, 'Informações do Projeto')
        
        roll = ttk.Scrollbar(subTela, orient = 'vertical', command = canvas.yview)
        
        canvas.configure(yscrollcommand = roll.set)

        roll.pack(side = 'right', fill = 'y')
        canvas.pack(side = 'left', fill = 'both', expand = True)

        canvas.create_window((4,4), window = frameTela, anchor = 'nw', tags = 'frameTela')
        frameTela.bind('<Configure>', canvas.configure(scrollregion = canvas.bbox('all')))

        subTela.place(x = 0, y = 0)

        ##### BOTÃO VOLTAR  #####
        voltar = tk.Button(frameTela, text = 'Voltar', font = self.fontBotao, command = lambda: funcVoltar())
        voltar.place(x = 10, y = 10)
        
        ###########  TÍTULO  #############
        tk.Label(frameTela, text='Setup de Informações\n de ' + self.tipo, font= self.fontTitulo).place(x = 80, y = 10, width = 200)

        ###########  CARACTERÍSTICAS DO PROJETO  #############
        self.lerInfos = self.LoadInfos.loadXML(self.tipo, 'caracteristicas')
        infosProj.place(x = 20, y = 70)
        posx = 20
        posy = 20
        posw = 200
        posxD = 170
        poswD = 50
        
        ##### ÁREA  #####
        chaveCampo = 'areas'
        areaL = tk.Label(infosProj, text = 'Área', bg = 'white', bd = 2, relief = 'solid', font = self.fontCampos, width = 30, height = 2)
        area = ttk.Combobox(infosProj, text = 'Área', state = 'readonly', values = self.lerInfos[chaveCampo])
        delArea = tk.Button(infosProj, text = 'Deletar', command = lambda: deletar(self.tela, self.lerInfos['tipo'], self.lerInfos['infos'], chaveCampo, area.get()))

        areaL.place(x = posx, y = posy, width = posw)
        posy += 50
        area.place(x = posx, y = posy, width = (posw - 50))
        delArea.place(x = posxD, y = posy, width = poswD)

        ##### STATUS  #####
        chaveCampo = 'status'
        statusL = tk.Label(infosProj, text = self.camposCarac[chaveCampo] + ': ', bg = 'white', bd = 2, relief = 'solid', font = self.fontCampos, width = 30, height = 2)
        status = ttk.Combobox(infosProj, text = self.camposCarac[chaveCampo], state = 'readonly', values = self.lerInfos[chaveCampo])
        delStatus = tk.Button(infosProj, text = 'Deletar', command = lambda: deletar(self.tela, self.lerInfos['tipo'], self.lerInfos['infos'], chaveCampo, status.get()))

        if self.camposCarac[chaveCampo] in self.infoForm:
            posy += 50
            statusL.place(x = posx, y = posy, width = posw)
            posy += 50
            status.place(x = posx, y = posy, width = (posw - 50))
            delStatus.place(x = posxD, y = posy, width = poswD)

        ##### BUDGET  #####
        chaveCampo = 'budget'
        budgetL = tk.Label(infosProj, text = self.camposCarac[chaveCampo] + ': ', bg = 'white', bd = 2, relief = 'solid', font = self.fontCampos, width = 30, height = 2)
        budget = ttk.Combobox(infosProj, text = self.camposCarac[chaveCampo], state = 'readonly', values = self.lerInfos[chaveCampo])
        delBudget = tk.Button(infosProj, text = 'Deletar', command = lambda: deletar(self.tela, self.lerInfos['tipo'], self.lerInfos['infos'], chaveCampo, budget.get()))

        if self.camposCarac[chaveCampo] in self.infoForm:
            posy += 50
            budgetL.place(x = posx, y = posy, width = posw)
            posy += 50
            budget.place(x = posx, y = posy, width = (posw - 50))
            delBudget.place(x = posxD, y = posy, width = poswD)
            
        ##### RESPONSÁVEL  #####
        chaveCampo = 'responsavel'
        respL = tk.Label(infosProj,text = self.camposCarac[chaveCampo] + ': ', bg = 'white', bd = 2, relief = 'solid', font = self.fontCampos, width = 30, height = 2)
        resp = ttk.Combobox(infosProj, text = self.camposCarac[chaveCampo], state = 'readonly', values = self.lerInfos['resp'])
        delResp = tk.Button(infosProj, text = 'Deletar', command = lambda: deletar(self.tela, self.lerInfos['tipo'], self.lerInfos['infos'], 'resp', resp.get()))

        if self.camposCarac[chaveCampo] in self.infoForm:
            posy += 50
            respL.place(x = posx, y = posy, width = posw)
            posy += 50
            resp.place(x = posx, y = posy, width = (posw - 50))
            delResp.place(x = posxD, y = posy, width = poswD)

        def funcVoltar():
            self.TelaSetup.setup()
            tela.destroy()
            self.TelaSetup = None

    #######  FUNÇÃO PARA SETUP DE COMPLEXIDADE #######
    def exibeSetupComp(self, tela):
        if self.TelaSetup == None:
            self.TelaSetup = st.TelaSetup(self.Portfolio, tela)

        subTela, canvas, frameTela, infosComp = self.TelaSetup.gerarSubTelas(1300, 'Informações do Projeto')
        
        roll = ttk.Scrollbar(subTela, orient = 'vertical', command = canvas.yview)
        canvas.configure(yscrollcommand = roll.set)

        roll.pack(side = 'right', fill = 'y')
        canvas.pack(side = 'left', fill = 'both', expand = True)

        canvas.create_window((4,4), window = frameTela, anchor = 'nw', tags = 'frameTela')
        frameTela.bind('<Configure>', canvas.configure(scrollregion = canvas.bbox('all')))

        subTela.place(x = 0, y = 0)

        ##### BOTÃO VOLTAR  #####
        voltar = tk.Button(frameTela, text = 'Voltar', font = self.fontBotao, command = lambda: funcVoltar())
        voltar.place(x = 10, y = 10)

        ###########  TÍTULO  #############
        tk.Label(frameTela, text='Setup de Avaliações de\nComplexidade para ' + self.tipo, font= self.fontTitulo).place(x = 20, y = 50, width = 260)

        ###########  CARACTERÍSTICAS DO PROJETO  #############
        self.lerInfos = self.LoadInfos.loadXML(self.tipo, 'complexidade')
        infosComp.place(x = 20, y = 70)
        posx = 3
        posy = -30
        posw = 240
        posxP = 140
        posxD = 170
        poswD = 50

        ######### 1  #########
        chaveCampo = 'esforco'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        esforcoLabel, esforcoLista, esforcoVal, esforcoPeso, esforcoDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            esforcoLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            esforcoLista.place(x = posx, y = posy, width = posw)
            posy += 30
            esforcoVal.place(x = posx, y = posy, width = (poswD * 2))
            esforcoPeso.place(x = (posx + 120), y = posy, width = poswD)
            esforcoDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 2  #########
        chaveCampo = 'conf'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,35)
        confLabel, confLista, confVal, confPeso, confDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            confLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            confLista.place(x = posx, y = posy, width = posw)
            posy += 30
            confVal.place(x = posx, y = posy, width = (poswD * 2))
            confPeso.place(x = (posx + 120), y = posy, width = poswD)
            confDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 3  #########
        chaveCampo = 'hab'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        habLabel, habLista, habVal, habPeso, habDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            habLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            habLista.place(x = posx, y = posy, width = posw)
            posy += 30
            habVal.place(x = posx, y = posy, width = (poswD * 2))
            habPeso.place(x = (posx + 120), y = posy, width = poswD)
            habDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 4  #########
        chaveCampo = 'numProfs'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        numProfsLabel, numProfsLista, numProfsVal, numProfsPeso, numProfsDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')     

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            numProfsLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            numProfsLista.place(x = posx, y = posy, width = posw)
            posy += 30
            numProfsVal.place(x = posx, y = posy, width = (poswD * 2))
            numProfsPeso.place(x = (posx + 120), y = posy, width = poswD)
            numProfsDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 5  #########
        chaveCampo = 'escop'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        escopLabel, escopLista, escopVal, escopPeso, escopDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            escopLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            escopLista.place(x = posx, y = posy, width = posw)
            posy += 30
            escopVal.place(x = posx, y = posy, width = (poswD * 2))
            escopPeso.place(x = (posx + 120), y = posy, width = poswD)
            escopDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 6  #########
        chaveCampo = 'comp'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        compLabel, compLista, compVal, compPeso, compDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            compLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            compLista.place(x = posx, y = posy, width = posw)
            posy += 30
            compVal.place(x = posx, y = posy, width = (poswD * 2))
            compPeso.place(x = (posx + 120), y = posy, width = poswD)
            compDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 7  #########
        chaveCampo = 'dispTec'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        dispTecLabel, dispTecLista, dispTecVal, dispTecPeso, dispTecDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            dispTecLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            dispTecLista.place(x = posx, y = posy, width = posw)
            posy += 30
            dispTecVal.place(x = posx, y = posy, width = (poswD * 2))
            dispTecPeso.place(x = (posx + 120), y = posy, width = poswD)
            dispTecDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 8  #########
        chaveCampo = 'difTec'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        difTecLabel, difTecLista, difTecVal, difTecPeso, difTecDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            difTecLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            difTecLista.place(x = posx, y = posy, width = posw)
            posy += 30
            difTecVal.place(x = posx, y = posy, width = (poswD * 2))
            difTecPeso.place(x = (posx + 120), y = posy, width = poswD)
            difTecDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 9  #########
        chaveCampo = 'impact'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        impactLabel, impactLista, impactVal, impactPeso, impactDel = self.TelaSetup.gerarSetupAval(infosComp, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'complexidade')

        if self.camposComplex[chaveCampo] in self.infoAvalComplex:
            posy += 50
            impactLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            impactLista.place(x = posx, y = posy, width = posw)
            posy += 30
            impactVal.place(x = posx, y = posy, width = (poswD * 2))
            impactPeso.place(x = (posx + 120), y = posy, width = poswD)
            impactDel.place(x = (posx + 190), y = posy, width = poswD)

        def funcVoltar():
            self.TelaSetup.setup()
            tela.destroy()
            self.TelaSetup = None

    #######  FUNÇÃO PARA SETUP DE CRITICIDADE #######
    def exibeSetupCrit(self, tela):
        if self.TelaSetup == None:
                self.TelaSetup = st.TelaSetup(self.Portfolio, tela)

        subTela, canvas, frameTela, infosCrit = self.TelaSetup.gerarSubTelas(780, 'Informações do Projeto')
        
        roll = ttk.Scrollbar(subTela, orient = 'vertical', command = canvas.yview)
        canvas.configure(yscrollcommand = roll.set)

        roll.pack(side = 'right', fill = 'y')
        canvas.pack(side = 'left', fill = 'both', expand = True)

        canvas.create_window((4,4), window = frameTela, anchor = 'nw', tags = 'frameTela')
        frameTela.bind('<Configure>', canvas.configure(scrollregion = canvas.bbox('all')))

        subTela.place(x = 0, y = 0)

        ##### BOTÃO VOLTAR  #####
        voltar = tk.Button(frameTela, text = 'Voltar', font = self.fontBotao, command = lambda: funcVoltar())
        voltar.place(x = 10, y = 10)

        ###########  TÍTULO  #############
        tk.Label(frameTela, text='Setup de Avaliações de\nCriticidade para ' + self.tipo, font= self.fontTitulo).place(x = 20, y = 50, width = 260)

        ###########  CARACTERÍSTICAS DO PROJETO  #############
        self.lerInfos = self.LoadInfos.loadXML(self.tipo, 'criticidade')
        infosCrit.place(x = 20, y = 70)
        posx = 3
        posy = -30
        posw = 240
        posxP = 140
        posxD = 170
        poswD = 50

        ######### 1  #########
        chaveCampo = 'ativVital'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        ativVitalLabel, ativVitalLista, ativVitalVal, ativVitalPeso, ativVitalDel = self.TelaSetup.gerarSetupAval(infosCrit, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'criticidade')

        if self.camposCritic[chaveCampo] in self.infoAvalCritic:
            posy += 50
            ativVitalLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            ativVitalLista.place(x = posx, y = posy, width = posw)
            posy += 30
            ativVitalVal.place(x = posx, y = posy, width = (poswD * 2))
            ativVitalPeso.place(x = (posx + 120), y = posy, width = poswD)
            ativVitalDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 2  #########
        chaveCampo = 'numArea'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        numAreaLabel, numAreaLista, numAreaVal, numAreaPeso, numAreaDel = self.TelaSetup.gerarSetupAval(infosCrit, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'criticidade')

        if self.camposCritic[chaveCampo] in self.infoAvalCritic:
            posy += 50
            numAreaLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            numAreaLista.place(x = posx, y = posy, width = posw)
            posy += 30
            numAreaVal.place(x = posx, y = posy, width = (poswD * 2))
            numAreaPeso.place(x = (posx + 120), y = posy, width = poswD)
            numAreaDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 3  #########
        chaveCampo = 'relMetas'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        relMetasLabel, relMetasLista, relMetasVal, relMetasPeso, relMetasDel = self.TelaSetup.gerarSetupAval(infosCrit, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'criticidade')

        if self.camposCritic[chaveCampo] in self.infoAvalCritic:
            posy += 50
            relMetasLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            relMetasLista.place(x = posx, y = posy, width = posw)
            posy += 30
            relMetasVal.place(x = posx, y = posy, width = (poswD * 2))
            relMetasPeso.place(x = (posx + 120), y = posy, width = poswD)
            relMetasDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 4  #########
        chaveCampo = 'roi'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        roiLabel, roiLista, roiVal, roiPeso, roiDel = self.TelaSetup.gerarSetupAval(infosCrit, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'criticidade')

        if self.camposCritic[chaveCampo] in self.infoAvalCritic:
            posy += 50
            roiLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            roiLista.place(x = posx, y = posy, width = posw)
            posy += 30
            roiVal.place(x = posx, y = posy, width = (poswD * 2))
            roiPeso.place(x = (posx + 120), y = posy, width = poswD)
            roiDel.place(x = (posx + 190), y = posy, width = poswD)

        ######### 5  #########
        chaveCampo = 'mustDo'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        mustDoLabel, mustDoLista, mustDoVal, mustDoPeso, mustDoDel = self.TelaSetup.gerarSetupAval(infosCrit, chaveCampo, nomeCampo, self.FuncSetup.separaApenasValor(self.lerInfos[chaveCampo]), self.alterarPeso, self.deletar, self.alterarValor, 'criticidade')

        if self.camposCritic[chaveCampo] in self.infoAvalCritic:
            posy += 50
            mustDoLabel.place(x = posx, y = posy, width = posw)
            posy += 50
            mustDoLista.place(x = posx, y = posy, width = posw)
            posy += 30
            mustDoVal.place(x = posx, y = posy, width = (poswD * 2))
            mustDoPeso.place(x = (posx + 120), y = posy, width = poswD)
            mustDoDel.place(x = (posx + 190), y = posy, width = poswD)

        def funcVoltar():
            self.TelaSetup.setup()
            tela.destroy()
            self.TelaSetup = None

class FuncSetup():
    def __init__(self, TelaSetup):
        self.TelaSetup = TelaSetup

    def separaApenasValor(listaDeValorePeso):
        apenasValor = []
        for valor in listaDeValorePeso:
            apenasValor.append(valor[0])
        return apenasValor
        
    #######  ALTERAR PESO DO CAMPO  #######
    def alterarPeso(self, tipo, infos, key, nome):
        print(tipo, infos, key, nome)

        pesos = li.LoadInfos().lerPeso(tipo, infos)

        tela, valOldLabel, valOld, valNewLabel = self.TelaSetup.gerarMiniTela('Peso', pesos, key)

        #val_oldL.place(x = 20, y = 20)

        #val_old.place(x = 120, y = 15)

        #val_newL.place(x = 20, y = 50)

        val_new = ttk.Combobox(self.tela, text = 'Pesos', state = 'readonly', values = [1, 2, 4, 6])
        val_new.place(x = 120, y = 50, width = 30)

        salvar = tk.Button(self.tela,
                           text = 'Salvar',
                           font = ('Arial Black', 10),
                           command = lambda: li.LoadInfos().salvarPeso())#self.tela, tipo, infos, key, val_new.get(), nome))
        salvar.place(x = 100, y = 80)

    #######  ALTERAR  VALOR ATRIBUIDO AO REGISTRO  #######
    def alterarValor(self, tipo, infos, valor_old, campo, nome_campo):
        print(tipo, infos, valor_old, campo, nome_campo)
        if len(valor_old) < 2:
            messagebox.showwarning('Alterar valor', 'Selecione uma classificação da lista de valores do campo ' + nome_campo)
            return False
 
##        self.tela = tk.Tk()
##        self.tela.wm_title('Setup')
##        self.tela.wm_minsize(width = 165, height = 115)
##
##        list_setup = li.LoadInfos().lerSetup(tipo, infos)
##        list_setup = list_setup[campo]
##
##        for x in list_setup:
##            if x[0] == valor_old:
##                list_setup = x[1]
##
##         text = 'Valor atual:', font = fontCampos).place(x = 20, y = 20)

          #val_oldL.place(x = 20, y = 20)
          #val_old.place(x = 120, y = 15)
          #val_newL.place(x = 20, y = 50)
          #val_new.place(x = 120, y = 50, width = 30)
##
##        val_old = tk.Label(self.tela, text = list_setup, bg = 'white', bd = 2, relief = 'solid', font = fontTitulo).place(x = 120, y = 15)
##
##        val_newL = tk.Label(self.tela, text = 'Valor novo:', font = fontCampos).place(x = 20, y = 50)
##
##        val_new = tk.Entry(self.tela)
##        val_new.place(x = 120, y = 50, width = 30)
##
##        salvar = tk.Button(self.tela,
##                           text = 'Salvar',
##                           font = ('Arial Black', 10),
##                           command = lambda: li.LoadInfos().salvarValue(self.tela, tipo, infos, campo, valor_old, val_new.get()))
##        salvar.place(x = 100, y = 80)

       
    #######  DELETAR  #######
    def deletar(self, tela, tipo, infos, chave, valor):
        print(tipo, infos, chave, valor)
##        if len(valor) < 2:
##            messagebox.showwarning('Deletar Registro', 'Selecione um registro para ser deletado')
##            return False
##        
##        confirmar = messagebox.askokcancel('Deletar Registro', 'Tem certeza que deseja deletar este registro do setup?')
##        if confirmar:           
##            lerSetup = open('setup', 'r')
##            listSetup = lerSetup.readlines()
##            lerSetup.close()
##            lerSetup = open('setup','w')
##            for linhasSetup in listSetup:
##                if linhasSetup != '\n':
##                    dictLinhasSetup = ast.literal_eval(linhasSetup)
##                    if dictLinhasSetup['infos'] != infos or dictLinhasSetup['tipo'] != tipo:
##                        lerSetup.write(linhasSetup)
##                    elif dictLinhasSetup['infos'] == infos and dictLinhasSetup['tipo'] == tipo:
##                        if infos == 'projeto':
##                            dictLinhasSetup[chave].remove(valor)
##                        else:
##                            listValor = dictLinhasSetup[chave]
##                            for x in listValor:
##                                if x[0] == valor:
##                                    dictLinhasSetup[chave].remove(x)
##                        lerSetup.write(str(dictLinhasSetup) + '\r\n')
##                        messagebox.showwarning('Registro deletado', 'O registro foi deletado com sucesso!')
##            lerSetup.close()
##            if infos == 'projeto':
##                exibeSetupProj(self.tela, tipo)
##            elif infos == 'criticidade':
##                exibeSetupCrit(self.tela, tipo)
##            elif infos == 'complexidade':
##                exibeSetupComp(self.tela, tipo)
