import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import ast

import SetupVerInfos as svi
import LoadInfos as li
import SetupTela as st

class SetupCampos():
    def __init__(self, Portfolio):
        self.fontTitulo = ('Arial Black', 12)
        self.fontCampos = ('Verdana', 10)
        self.fontBotao = ('Arial Black', 10)
        self.Portfolio = Portfolio
        self.LoadInfos = li.LoadInfos()
        self.SetupVerInfos = svi.SetupVerInfos(self.Portfolio)
        self.TelaSetup = None
        self.tipo, self.area = self.Portfolio.infoPort()
        self.infoForm = self.Portfolio.infoForm()
        self.avalComplex = self.Portfolio.infoAvalComplex()
        self.avalCritic = self.Portfolio.infoAvalCritic()
        self.camposCarac, self.camposComplex, self.camposCritic = self.LoadInfos.loadConfigPort('AllFields')
        self.camposCarac = ast.literal_eval(self.camposCarac['valores'])
        self.camposComplex = ast.literal_eval(self.camposComplex['valores'])
        self.camposCritic = ast.literal_eval(self.camposCritic['valores'])

    def caracProj(self, tela):
        if self.TelaSetup == None:
            self.TelaSetup = st.TelaSetup(self.Portfolio, tela)
        
        subTela, canvas, frameTela, caracProj = self.TelaSetup.gerarSubTelas(400, 'Informações do Projeto')

        roll = ttk.Scrollbar(subTela, orient = 'vertical', command = canvas.yview)
            
        canvas.configure(yscrollcommand = roll.set)

        roll.pack(side = 'right', fill = 'y')
        canvas.pack(side = 'left', fill = 'both', expand = True)

        canvas.create_window((4,4), window = frameTela, anchor = 'nw', tags = 'frameTela')
        frameTela.bind('<Configure>', canvas.configure(scrollregion = canvas.bbox('all')))

        subTela.pack(side='left', fill = 'y')

        ##### BOTÃO VOLTAR  #####
        voltar = tk.Button(frameTela, text = 'Voltar', font = self.fontBotao, command = lambda: funcVoltar())
        voltar.place(x = 10, y = 20)

        ####  EXIBIR CONFIG ATUAL  #####
        atual = tk.Button(frameTela,
                           text = 'Valores\natuais',
                           font = self.fontBotao,
                           command = lambda: self.SetupVerInfos.infosCarac(tela))
        atual.place(x = 210, y = 10)
        
        ###########  TÍTULO  #############
        tk.Label(frameTela, text='Setup', font= self.fontTitulo).place(x = 100, y = 20, width = 100)

        ###########  CARACTERÍSTICAS DO PROJETO  #############
        caracProj.place(x = 20, y = 70)
        posxL = 20
        posyL = 20
        posxC = 80
        posyC = 30
        
        ####  ÁREA  ####
        areaL = tk.Label(caracProj, text = 'Área: ', font = self.fontCampos, height = 2)
        area = tk.Entry(caracProj)

        areaL.place(x = posxL, y = posyL)
        area.place(x = posxC, y = posyC)

        ####  STATUS  ####
        chaveCampo = 'status'
        statusL = tk.Label(caracProj, text = self.camposCarac[chaveCampo] + ': ', font = self.fontCampos, height = 2)
        status = tk.Entry(caracProj)

        if self.camposCarac[chaveCampo] in self.infoForm:
            posyL += 50
            posyC += 50
            statusL.place(x = posxL, y = posyL)
            status.place(x = posxC, y = posyC)

        ####  BUDGET  ####
        chaveCampo = 'budget'
        budgetL = tk.Label(caracProj, text = self.camposCarac[chaveCampo] + ': ', font = self.fontCampos, height = 2)
        budget = tk.Entry(caracProj)

        if self.camposCarac[chaveCampo] in self.infoForm:
            posyL += 50
            posyC += 50
            budgetL.place(x = posxL, y = posyL)
            budget.place(x = posxC, y = posyC)

        ####  RESPONSÁVEL  ####
        chaveCampo = 'responsavel'
        respL = tk.Label(caracProj, text = self.camposCarac[chaveCampo] + ': ', font = self.fontCampos, height = 2)
        resp = tk.Entry(caracProj)

        if self.camposCarac[chaveCampo] in self.infoForm:
            posyL += 50
            posyC += 70
            respL.place(x = posxL, y = posyL)
            resp.place(x = posxL, y = posyC, width = 185)

        ####  SALVAR  #####
        salvar = tk.Button(caracProj, text = 'Salvar', command = lambda: funcSalvar())
        salvar.place(x = 195, y = 235)

        ####  DEFAULT  #####
        default = tk.Button(caracProj, text = 'Default', command = lambda: self.Portfolio.restaurarInfosCarac())
        default.place(x = 10, y = 235)

        def exibirConfig():
            self.SetupVerInfos.infosCarac(tela)
            self.TelaSetup = None

        def funcVoltar():
            self.TelaSetup.setup()
            tela.destroy()
            self.TelaSetup = None

        def funcSalvar():
            salvar = self.Portfolio.alterarInfosCarac(area.get(), status.get(), budget.get(), resp.get())
            if not salvar:
                messagebox.showwarning('Erro!','Ao menos um campo deve ser preenchido com mais de um caractere')

            area.delete(first = 0, last = len(area.get()))
            status.delete(first = 0, last = len(status.get()))
            budget.delete(first = 0, last = len(budget.get()))
            resp.delete(first = 0, last = len(resp.get()))

    def avalComp(self, tela):
        if self.TelaSetup == None:
            self.TelaSetup = st.TelaSetup(self.Portfolio, tela)
        
        subTela, canvas, frameTela, avalProj = self.TelaSetup.gerarSubTelas(1620, 'Avaliação de Complexidade')
        
        roll = ttk.Scrollbar(subTela, orient = 'vertical', command = canvas.yview)
        canvas.configure(yscrollcommand = roll.set)

        roll.pack(side = 'right', fill = 'y')
        canvas.pack(side = 'left', fill = 'both', expand = True)

        canvas.create_window((4,4), window = frameTela, anchor = 'nw', tags = 'frameTela')
        frameTela.bind('<Configure>', canvas.configure(scrollregion = canvas.bbox('all')))

        subTela.pack(side='left', fill = 'y')

        ##### BOTÃO VOLTAR  #####
        voltar = tk.Button(frameTela, text = 'Voltar', font = self.fontBotao, command = lambda: funcVoltar())
        voltar.place(x = 10, y = 20)

        ####  EXIBIR CONFIG ATUAL  #####
        atual = tk.Button(frameTela,
                           text = 'Valores\natuais',
                           font = ('Arial Black', 10),
                           command = lambda: self.SetupVerInfos.exibeSetupComp(tela))
        atual.place(x = 210, y = 10)
        
        ###########  TÍTULO  #############
        tk.Label(frameTela, text='Setup', font= self.fontTitulo).place(x = 100, y = 20, width = 100)

        ###########  CRITÉRIOS DE AVALIAÇÃO  #############
        avalProj.place(x = 20, y = 70)

        posy = 20
        posx = 20
        posyP= 70
        valWidth = 205

        dist_1 = 50
        dist_2 = 30

        campos = {}
        
        ######################################     1      #########################################
        chaveCampo = 'esforco'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        esforcoL, esforcoPL, esforcoP, esforcoLV, esforcoV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [esforcoV, esforcoP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            esforcoL.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
            esforcoPL.place(x = posx, y = posy)
            esforcoP.place(x = posyP, y = posy)
            posy += dist_2
            esforcoLV.place(x = posx, y = posy)
            posy += dist_2
            esforcoV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1

        ######################################     2      #########################################
        chaveCampo = 'conf'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,35)
        confL, confLP, confP, confLV, confV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [confV, confP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            confL.place(x = (posx - 10), y = posy, width = (valWidth + 20))
            posy += dist_1
            confLP.place(x = posx, y = posy)
            confP.place(x = posyP, y = posy)
            posy += dist_2
            confLV.place(x = posx, y = posy)
            posy += dist_2
            confV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
            
          ######################################     3      #########################################
        chaveCampo = 'hab'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        habL, habLP, habP, habLV, habV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [habV, habP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            habL.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
            habLP.place(x = posx, y = posy)
            habP.place(x = posyP, y = posy)
            posy += dist_2
            habLV.place(x = posx, y = posy)
            posy += dist_2
            habV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
        
        ######################################     4      #########################################
        chaveCampo = 'numProfs'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        numProfsL, numProfsLP, numProfsP, numProfsLV, numProfsV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [numProfsV, numProfsP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            numProfsL.place(x = (posx - 5), y = posy, width = (valWidth + 10))
            posy += dist_1
            numProfsLP.place(x = posx, y = posy)
            numProfsP.place(x = posyP, y = posy)
            posy += dist_2
            numProfsLV.place(x = posx, y = posy)
            posy += dist_2
            numProfsV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
        
        ######################################     5      #########################################
        chaveCampo = 'escop'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        escopL, escopLP, escopP, escopLV, escopV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [escopV, escopP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            escopL.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
            escopLP.place(x = posx, y = posy)
            escopP.place(x = posyP, y = posy)
            posy += dist_2
            escopLV.place(x = posx, y = posy)
            posy += dist_2
            escopV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1

        ######################################     6      #########################################
        chaveCampo = 'comp'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        compL, compLP, compP, compLV, compV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [compV, compP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            compL.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
            compLP.place(x = posx, y = posy)
            compP.place(x = posyP, y = posy)
            posy += dist_2
            compLV.place(x = posx, y = posy)
            posy += dist_2
            compV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
        
        ######################################     7      #########################################
        chaveCampo = 'dispTec'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        dispTecL, dispTecLP, dispTecP, dispTecLV, dispTecV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [dispTecV, dispTecP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            dispTecL.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
            dispTecLP.place(x = posx, y = posy)
            dispTecP.place(x = posyP, y = posy)
            posy += dist_2
            dispTecLV.place(x = posx, y = posy)
            posy += dist_2
            dispTecV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1

        ######################################     8      #########################################
        chaveCampo = 'difTec'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        difTecL, difTecLP, difTecP, difTecLV, difTecV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [difTecV, difTecP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            difTecL.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
            difTecLP.place(x = posx, y = posy)
            difTecP.place(x = posyP, y = posy)
            posy += dist_2
            difTecLV.place(x = posx, y = posy)
            posy += dist_2
            difTecV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1

        ######################################     9      #########################################
        chaveCampo = 'impact'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposComplex[chaveCampo],14,25)
        impactL, impactLP, impactP, impactLV, impactV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [impactV, impactP]

        if self.camposComplex[chaveCampo] in self.avalComplex:
            impactL.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
            impactLP.place(x = posx, y = posy)
            impactP.place(x = posyP, y = posy)
            posy += dist_2
            impactLV.place(x = posx, y = posy)
            posy += dist_2
            impactV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1

        ####  SALVAR  #####
        salvar = tk.Button(avalProj, text = 'Salvar', command = lambda: funcSalvar())
        salvar.place(x = 185, y = 1630)

        ####  DEFAULT  #####
        default = tk.Button(avalProj,
                           text = 'Default',
                           command = lambda: self.Portfolio.restaurarInfosAval('complexidade'))
        default.place(x = 10, y = 1630)

        def funcVoltar():
            self.TelaSetup.setup()
            tela.destroy()
            self.TelaSetup = None

        def funcSalvar():
            ############  DICIONÁRIO DE CAMPOS  #############
            valores = {}
            valores['infos'] = 'complexidade'
            
            for chave in campos.keys():
                valores[chave] = [campos[chave][0].get(), campos[chave][1].get()]
            
            key, local, mensagem = self.Portfolio.alterarInfosAval(valores)

            if key in campos.keys():
                listCampo = campos[key]
                messagebox.showwarning('Erro!', mensagem + self.camposComplex[key])
                tk.BaseWidget.focus_force(listCampo[local])
            elif key == 'work':
                messagebox.showwarning('Setup Salvo!', mensagem)
                for key in campos.keys():
                    infosCampos = campos[key]
                    valorCampos = infosCampos[0]
                    pesoCampos = infosCampos[1]

                    valorCampos.delete(first = 0, last = len(valorCampos.get()))
                    pesoCampos.delete(first = 0, last = len(pesoCampos.get()))

    def avalCrit(self, tela):
        if self.TelaSetup == None:
            self.TelaSetup = st.TelaSetup(self.Portfolio, tela)
        
        subTela, canvas, frameTela, avalProj = self.TelaSetup.gerarSubTelas(1020, 'Critérios de Avaliação')
        
        roll = ttk.Scrollbar(subTela, orient = 'vertical', command = canvas.yview)
        canvas.configure(yscrollcommand = roll.set)

        roll.pack(side = 'right', fill = 'y')
        canvas.pack(side = 'left', fill = 'both', expand = True)

        canvas.create_window((4,4), window = frameTela, anchor = 'nw', tags = 'frameTela')
        frameTela.bind('<Configure>', canvas.configure(scrollregion = canvas.bbox('all')))

        subTela.pack(side='left', fill = 'y')

        ##### BOTÃO VOLTAR  #####
        voltar = tk.Button(frameTela, text = 'Voltar', font = self.fontBotao, command = lambda: funcVoltar())
        voltar.place(x = 10, y = 20)

        ####  EXIBIR CONFIG ATUAL  #####
        atual = tk.Button(frameTela,
                           text = 'Valores\natuais',
                           font = self.fontBotao,
                           command = lambda: self.SetupVerInfos.exibeSetupCrit(tela))
        atual.place(x = 210, y = 10)
        
        ###########  TÍTULO  #############
        titulo = tk.Label(frameTela, text='Setup', font= self.fontTitulo).place(x = 100, y = 20, width = 100)
        
            ###########  CRITÉRIOS DE AVALIAÇÃO  #############
        avalProj.place(x = 20, y = 70)

        posy = 20
        posx = 20
        posyP= 70
        valWidth = 205

        dist_1 = 50
        dist_2 = 30

        campos = {}

        ###########################################     1      #########################################
        chaveCampo = 'ativVital'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        ativVitalL, ativVitalPL, ativVitalP, ativVitalLV, ativVitalV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [ativVitalV, ativVitalP]

        if self.camposCritic[chaveCampo] in self.avalCritic:
            ativVitalL.place(x = (posx - 10), y = posy, width = (valWidth + 20))
            posy += dist_1
            ativVitalPL.place(x = posx, y = posy)
            ativVitalP.place(x = posyP, y = posy)
            posy += dist_2
            ativVitalLV.place(x = posx, y = posy)
            posy += dist_2
            ativVitalV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1

        ######################################     2      #########################################
        chaveCampo = 'numArea'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        numAreaL, numAreaPL, numAreaP, numAreaLV, numAreaV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [numAreaV, numAreaP]

        if self.camposCritic[chaveCampo] in self.avalCritic:
            numAreaL.place(x = (posx - 10), y = posy, width = (valWidth + 20))
            posy += dist_1
            numAreaPL.place(x = posx, y = posy)
            numAreaP.place(x = posyP, y = posy)
            posy += dist_2
            numAreaLV.place(x = posx, y = posy)
            posy += dist_2
            numAreaV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
        
        ######################################     3      #########################################
        chaveCampo = 'relMetas'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        relMetasL, relMetasPL, relMetasP, relMetasLV, relMetasV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [relMetasV, relMetasP]

        if self.camposCritic[chaveCampo] in self.avalCritic:
            relMetasL.place(x = (posx - 10), y = posy, width = (valWidth + 20))
            posy += dist_1
            relMetasPL.place(x = posx, y = posy)
            relMetasP.place(x = posyP, y = posy)
            posy += dist_2
            relMetasLV.place(x = posx, y = posy)
            posy += dist_2
            relMetasV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
        
        ######################################     4      #########################################
        chaveCampo = 'roi'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        roiL, roiPL, roiP, roiLV, roiV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [roiV, roiP]

        if self.camposCritic[chaveCampo] in self.avalCritic:
            roiL.place(x = (posx - 10), y = posy, width = (valWidth + 20))
            posy += dist_1
            roiPL.place(x = posx, y = posy)
            roiP.place(x = posyP, y = posy)
            posy += dist_2
            roiLV.place(x = posx, y = posy)
            posy += dist_2
            roiV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1
        
        ######################################     5      #########################################
        chaveCampo = 'mustDo'
        nomeCampo, fonte = self.LoadInfos.formatText(self.camposCritic[chaveCampo],14,25)
        mustDoL, mustDoPL, mustDoP, mustDoLV, mustDoV = self.TelaSetup.gerarCamposAval(avalProj, nomeCampo)
        campos[chaveCampo] = [mustDoV, mustDoP]

        if self.camposCritic[chaveCampo] in self.avalCritic:
            mustDoL.place(x = (posx - 10), y = posy, width = (valWidth + 20))
            posy += dist_1
            mustDoPL.place(x = posx, y = posy)
            mustDoP.place(x = posyP, y = posy)
            posy += dist_2
            mustDoLV.place(x = posx, y = posy)
            posy += dist_2
            mustDoV.place(x = posx, y = posy, width = valWidth)
            posy += dist_1

        ####  SALVAR  #####
        salvar = tk.Button(avalProj, text = 'Salvar', command = lambda: funcSalvar())
        salvar.place(x = 185, y = 910)

        def funcVoltar():
            self.TelaSetup.setup()
            tela.destroy()
            self.TelaSetup = None

        def funcSalvar():
            ############  DICIONÁRIO DE CAMPOS  #############
            valores = {}
            valores['infos'] = 'criticidade'
            for chave in campos.keys():
                valores[chave] = [campos[chave][0].get(), campos[chave][1].get()]
            
            key, local, mensagem = self.Portfolio.alterarInfosAval(valores)

            if key in campos.keys():
                listCampo = campos[key]
                messagebox.showwarning('Erro!', mensagem + self.camposCritic[key])
                tk.BaseWidget.focus_force(listCampo[local])
            elif key == 'fail':
                messagebox.showwarning('Erro!', mensagem)
            elif key == 'work':
                messagebox.showwarning('Setup Salvo!', mensagem)
                for key in campos.keys():
                    infosCampos = campos[key]
                    valorCampos = infosCampos[0]
                    pesoCampos = infosCampos[1]

                    valorCampos.delete(first = 0, last = len(valorCampos.get()))
                    pesoCampos.delete(first = 0, last = len(pesoCampos.get()))
                
            if len(config.keys()) < 3:
                messagebox.showwarning('Erro!','Ao menos um campo deve ser preenchido com mais de um caractere')
                return False
        
        ####  DEFAULT  #####
        default = tk.Button(avalProj,
                           text = 'Default',
                           command = lambda: self.Portfolio.restaurarInfosAval('criticidade'))
        default.place(x = 10, y = 910)
