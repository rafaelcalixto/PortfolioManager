import tkinter as tk
from tkinter import ttk
import ast
from tkinter import messagebox

import LoadInfos as li
import MenuConsulta as mc

fontTitulo = ('Arial', 16)
fontCampos = ('Verdana', 10)

class Avaliar():
    def __init__(self, tela_old, idProj, nomeProj, tipo, area, infosAval = None, tela_dead = None):
        self.tela_old = tela_old
        self.idProj = idProj
        self.nomeProj = nomeProj
        self.tipo = tipo
        self.area = area
        self.infosAval = infosAval
        self.tela_dead = tela_dead
        self.tela = tk.Tk()
        self.LoadInfos = li.LoadInfos()

        ######  ELEMENTOS DA TELA DE COMPLEXIDADE  ######
        self.widthComp = 660
        self.heightComp = 420
        self.telaComp = tk.Canvas(self.tela, width = self.widthComp, height = self.heightComp)
        self.canvasComp = tk.Canvas(self.telaComp, width = self.widthComp, height = self.heightComp)

        ######  ELEMENTOS DA TELA DE CRITICIDADE  ######
        self.widthCrit = 660
        self.heightCrit = 305
        self.telaCrit = tk.Canvas(self.tela, width = self.widthCrit, height = self.heightCrit)
        self.canvasCrit = tk.Canvas(self.telaCrit, width = self.widthCrit, height = self.heightCrit)
        
        ######  PARAMETRO DE POSICIONAMENTO PARA ELEMENTOS DO FORMULÁRIO  ######
        self.posXLabel = 10
        self.posYLabel = 20
        self.posXList = 320
        self.posYList = 30

        self.distRow = 38
        self.tamLabel = 300
        self.altLabel = 40
        self.tamList = 330

    def form(self):
        self.tela.wm_title('Avaliação de Portifolios')
        self.tela.wm_minsize(width = 700, height = 640)

        #########  TÍTULOS DAS ÁREAS  ##########

        ######  COMPLEXIDADE  ######
        complexidade = tk.LabelFrame(self.canvasComp,
                              text = 'Complexidade',
                              bd = 2,
                              relief = 'solid',
                              font = fontTitulo,
                              width = self.widthComp,
                              height = self.heightComp)
        
        rollComp = ttk.Scrollbar(self.telaComp, orient = 'vertical', command = self.canvasComp.yview)
        self.canvasComp.configure(yscrollcommand = rollComp.set)
        
        rollComp.pack(side = 'right', fill = 'y')
        self.canvasComp.pack(side = 'left', fill = 'both', expand = True)

        self.canvasComp.create_window((4,4), window = complexidade, anchor = 'nw', tags = 'complexidade')
        complexidade.bind('<Configure>', self.canvasComp.configure(scrollregion = self.canvasComp.bbox('all')))

        self.telaComp.place(x = 20, y = 170, height = 200)

        #######  CRITICIDADE  #######        
        criticidade = tk.LabelFrame(self.canvasCrit,
                              text = 'Criticidade',
                              bd = 2,
                              relief = 'solid',
                              font = fontTitulo,
                              width = self.widthCrit,
                              height = self.heightCrit)

        rollCrit = ttk.Scrollbar(self.telaCrit, orient = 'vertical', command = self.canvasCrit.yview)
        self.canvasCrit.configure(yscrollcommand = rollCrit.set)
        
        rollCrit.pack(side = 'right', fill = 'y')
        self.canvasCrit.pack(side = 'left', fill = 'both', expand = True)

        self.canvasCrit.create_window((4,4), window = criticidade, anchor = 'nw', tags = 'criticidade')
        criticidade.bind('<Configure>', self.canvasCrit.configure(scrollregion = self.canvasCrit.bbox('all')))

        self.telaCrit.place(x = 20, y = 380, height = 200)

        #######  TÍTULOS  #######

        tk.Label(self.tela, text = 'Avaliação de Portifolios', font = fontTitulo).place(x = 200, y = 10, width = 300)

        self.nomeProj, tamFonte = self.LoadInfos.formatText(self.nomeProj, 22, 40, 80)

        tk.Label(self.tela, text = self.nomeProj, font = ('Ariel Black', tamFonte)).place(x = 55, y = 70, width = 590)

        ttk.Separator(self.tela, orient = 'horizontal').place(x = 50, y = 150, width = 600)

        ########  CAMPOS PARA AVALIAÇÃO DO PORTFOLIO  ########

        ############  CARREGAR INFORMAÇÕES DO SETUP DE COMPLEXIDADE #################
        
        valuesComp = self.LoadInfos.loadXML(self.tipo, 'complexidade')

        esforco = self.LoadInfos.loadInfos('esforco', valuesComp)

        conf = self.LoadInfos.loadInfos('conf', valuesComp)

        hab = self.LoadInfos.loadInfos('hab', valuesComp)

        numProfs = self.LoadInfos.loadInfos('numProfs', valuesComp)

        escop = self.LoadInfos.loadInfos('escop', valuesComp)

        comp = self.LoadInfos.loadInfos('comp', valuesComp)

        dispTec = self.LoadInfos.loadInfos('dispTec', valuesComp)

        difTec = self.LoadInfos.loadInfos('difTec', valuesComp)

        impact = self.LoadInfos.loadInfos('impact', valuesComp)

        ######################################     1      #########################################
        tk.Label(complexidade,
                    text = 'Esforço do Projeto',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)

        esforco = ttk.Combobox(complexidade,
                               text = 'Esforço do Projeto',
                               state = 'readonly',
                               values = esforco)
        esforco.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     2      #########################################
        self.posYLabel += self.distRow
        tk.Label(complexidade,
                    text = 'Confiabilidade nos fornecedores',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow
        conf = ttk.Combobox(complexidade, 
                            text = 'Confiabilidade nos fornecedores',
                            state = 'readonly',
                            values = conf)
        conf.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     3      #########################################
        self.posYLabel += self.distRow
        tk.Label(complexidade,
                    text = 'Habilidade interna dos profissionais',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        hab = ttk.Combobox(complexidade, 
                           text = 'Habilidade interna dos profissionais',
                           state = 'readonly',
                           values = hab)
        hab.place(x = self.posXList, y = self.posYList, width = self.tamList)
        
        ######################################     4      #########################################
        self.posYLabel += self.distRow
        tk.Label(complexidade,
                    text = 'Número de profissionais \ntécnicos envolvidos no projeto',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        numProfs = ttk.Combobox(complexidade,
                                state = 'readonly',
                                text = 'Número de profissionais técnicos envolvidos no projeto',
                                values = numProfs)
        numProfs.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     5      #########################################
        self.posYLabel += self.distRow
        tk.Label(complexidade,
                    text = 'Tendência de variação do escopo',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        escop = ttk.Combobox(complexidade,
                             text = 'Tendência de variação do escopo',
                             state = 'readonly',
                             values = escop)
        escop.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     6      #########################################
        self.posYLabel += self.distRow
        tk.Label(complexidade,
                    text = 'Comprometimento das partes interessadas',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        comp = ttk.Combobox(complexidade, 
                            text = 'Comprometimento das partes interessadas',
                            state = 'readonly',
                            values = comp)
        comp.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     7      #########################################
        self.posYLabel += self.distRow
        tk.Label(complexidade,
                    text = 'Disponibilidade de recursos técnológicos',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        dispTec = ttk.Combobox(complexidade, 
                               text = 'Disponibilidade de recursos técnológicos',
                               state = 'readonly',
                               values = dispTec)
        dispTec.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     8      #########################################
        self.posYLabel += self.distRow
        tk.Label(complexidade,
                    text = 'Dificuldade técnica do projeto',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        difTec = ttk.Combobox(complexidade, 
                              text = 'Dificuldade técnica do projeto',
                              state = 'readonly',
                              values = difTec)
        difTec.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     9      #########################################
        self.posYLabel += self.distRow
        tk.Label(complexidade,
                    text = 'Impacto no processo de negócio atual',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        impact = ttk.Combobox(complexidade, 
                              text = 'Impacto no processo de negócio atual',
                              state = 'readonly',
                              values = impact)
        impact.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ############  CARREGAR INFORMAÇÕES DO SETUP DE CRITICIDADE #################
        
        valuesCrit = self.LoadInfos.loadXML(self.tipo, 'criticidade')

        ativVital = self.LoadInfos.loadInfos('ativVital', valuesCrit)

        numArea = self.LoadInfos.loadInfos('numArea', valuesCrit)

        relMetas = self.LoadInfos.loadInfos('relMetas', valuesCrit)

        roi = self.LoadInfos.loadInfos('roi', valuesCrit)

        mustDo = self.LoadInfos.loadInfos('mustDo', valuesCrit)

        ######################################     1      #########################################
        self.posYLabel = 20
        tk.Label(criticidade,
                    text = 'Relacionado a alguma atividade\n de negócio vital',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList = 30
        ativVital = ttk.Combobox(criticidade, 
                                 text = 'Relacionado a alguma atividade de negócio vital',
                                 state = 'readonly',
                                 values = ativVital)
        ativVital.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     2      #########################################
        self.posYLabel += self.distRow
        tk.Label(criticidade,
                    text = 'Número de áreas negócio beneficiadas \ncom o projeto',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        numArea = ttk.Combobox(criticidade, 
                               text = 'Número de áreas negócio beneficiadas com o projeto',
                               state = 'readonly',
                               values = numArea)
        numArea.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     3      #########################################
        self.posYLabel += self.distRow
        tk.Label(criticidade,
                    text = 'Relacionado as metas atuais da diretoria',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        relMetas = ttk.Combobox(criticidade, 
                                text = 'Relacionado as metas atuais da diretoria',
                                state = 'readonly',
                                values = relMetas)
        relMetas.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     4      #########################################
        self.posYLabel += self.distRow
        tk.Label(criticidade,
                    text = 'ROI',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        roi = ttk.Combobox(criticidade, 
                           text = 'ROI',
                           state = 'readonly',
                           values = roi)
        roi.place(x = self.posXList, y = self.posYList, width = self.tamList)

        ######################################     5      #########################################
        self.posYLabel += self.distRow
        tk.Label(criticidade,
                    text = 'Must Do',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        mustDo = ttk.Combobox(criticidade, 
                              text = 'Must Do',
                              state = 'readonly',
                              values = mustDo)
        mustDo.place(x = self.posXList, y = self.posYList, width = self.tamList) 
        
        ######################################     6      #########################################
        self.posYLabel += self.distRow
        tk.Label(criticidade,
                    text = 'Justificativa',
                    bg = 'white',
                    bd = 2,
                    relief = 'solid',
                    font = fontCampos,
                    width = 30,
                    height = 2).place(x = self.posXLabel, y = self.posYLabel, width = self.tamLabel, height = self.altLabel)
        
        self.posYList += self.distRow 
        just = tk.Entry(criticidade)
        just.place(x = self.posXList, y = self.posYList, width = self.tamList) 

        ##################  CARREGAR INFORMAÇÕES CASO A AVALIAÇÃO SEJA EDITADA  ###################

        if self.tela_dead != None:
            self.tela_dead.destroy()

            esforco.set(infosAval['esforco'])
            conf.set(infosAval['conf'])
            hab.set(infosAval['hab'])
            numProfs.set(infosAval['numProfs'])
            escop.set(infosAval['escop'])
            comp.set(infosAval['comp'])
            dispTec.set(infosAval['dispTec'])
            difTec.set(infosAval['difTec'])
            impact.set(infosAval['impact'])
            
            ativVital.set(infosAval['ativVital'])
            numArea.set(infosAval['numArea'])
            relMetas.set(infosAval['relMetas'])
            roi.set(infosAval['roi'])
            mustDo.set(infosAval['mustDo'])
            just.insert(0, infosAval['just'])

        ######################################     BOTÕES      ####################################

        salvar = tk.Button(self.tela,
                           text = 'Salvar',
                           font = fontCampos,
                           command = lambda: registrar(self.tela_old, self.tipo, self.area, self.idProj, self.nomeProj, esforco.get(), conf.get(), hab.get(), numProfs.get(), escop.get(), comp.get(), dispTec.get(), difTec.get(), impact.get(), ativVital.get(), numArea.get(), relMetas.get(), roi.get(), mustDo.get(), just.get()))   
        salvar.place(x = 590, y = 600, width = 100)

    ##    testar = tk.Button(tela,
    ##                       text = 'Testar',
    ##                       font = fontCampos,
    ##                       command = lambda: registrar('000', 'teste', 'De 160HH até 720HH (3 meses de 2 pessoas)', 'Não há fornecedores', 'Possuem as habilidades necessárias', 'Até 3 pessoas', 'Alto', 'Partes interessadas são comprometidas', 'Alto', 'Alto', 'Alto', 'Não tem relação', '1 diretoria', 'Diretamente relacionado', 'Negativo', 'É obrigatório', 'teste'))#messagebox.showinfo('Salvar', 'Avaliação salva: ' + nomeProj))    
    ##    testar.place(x = 380, y = 600)

        ########  AVALIAÇÃO  ########

        def registrar(tela_old, tipo, area, idProj, nomeProj, esforcoV, confV, habV, numProfsV, escopV, compV, dispTecV, difTecV, impactV, ativVitalV, numAreaV, relMetasV, roiV, mustDoV, justV):

            #################  VALIDAÇÃO DOS DADOS  ##################
            dictAvals = {}
            
            for x in ([esforcoV, esforco, 'esforco', 'Esforço do Projeto (HH)'], [confV, conf, 'conf', 'Confiabilidade nos fornecedores'], [habV, hab, 'hab','Habilidade interna dos profissionais'], [numProfsV, numProfs, 'numProfs', 'Número de profissionais técnicos envolvidos no projeto'], [escopV, escop, 'escop', 'Tendência de variação do escopo'], [compV, comp, 'comp', 'Comprometimento das partes interessadas'], [dispTecV, dispTec, 'dispTec', 'Disponibilidade de recursos técnológicos'], [difTecV, difTec, 'difTec', 'Dificuldade técnica do projeto'], [impactV, impact, 'impact', 'Impacto no processo de negócio atual'], [ativVitalV, ativVital, 'ativVital', 'Relacionado a alguma atividade de negócio vital'], [numAreaV, numArea, 'numArea', 'Número de áreas negócio beneficiadas com o projeto'], [relMetasV, relMetas, 'relMetas', 'Relacionado as metas atuais da diretoria'], [roiV, roi, 'roi','ROI'], [mustDoV, mustDo, 'mustDo', 'Must Do']):
                dictAvals[x[2]] = x[0]
                if len(x[0]) < 2:
                    messagebox.showwarning('Opção inválida!', 'Selecione uma opção da lista de valores para o campo "' + x[3] + '"')
                    tk.BaseWidget.focus_force(x[1])
                
            totalComp, totalCrit, reg = self.LoadInfos.avalCompCrit(tipo, area, str(idProj), dictAvals)

            ########  SALVAR DADOS  ########
            confirmar = messagebox.askokcancel('Salvar Avaliação','Deseja salvar avaliação?\nNível de Complexidade: ' + str(totalComp) + '\nNível de Criticidade: ' + str(totalCrit))
            if confirmar:
                #reg = '{"id":"' + str(idProj) + '", "esforco":"' + esforcoV + '", "conf":"' + confV + '", "hab":"' + habV + '", "numProfs":"' + numProfsV + '", "escop":"' + escopV + '", "comp":"' + compV + '", "dispTec":"' + dispTecV + '", "difTec":"' + difTecV + '", "impact":"' + impactV + '", "ativVital":"' + ativVitalV + '", "numArea":"' + numAreaV + '", "relMetas":"' + relMetasV + '", "roi":"' + roiV + '", "mustDo":"' + mustDoV + '", "just":"' + justV.replace('\n', " ").replace('"', "'") + '", "complexidade":"' + str(totalComp) + '", "criticidade":"' + str(totalCrit) + '", "peso_esforco":"' + str(esforcoP) + '", "peso_conf":"' + str(confP) + '", "peso_hab":"' + str(habP)  + '", "peso_numProfs":"' + str(numProfsP) + '", "peso_escop":"' + str(escopP) + '", "peso_comp":"' + str(compP) + '", "peso_dispTec":"' + str(dispTecP) + '", "peso_difTec":"' + str(difTecP) + '", "peso_impact":"' + str(impactP) + '", "peso_ativVital":"' + str(ativVitalP) + '", "peso_numArea":"' + str(numAreaP) + '", "peso_relMetas":"' + str(relMetasP) + '", "peso_roi":"' + str(roiP) + '", "peso_mustDo":"' + str(mustDoP) + '"}\r\n'
                reg += ', "just":"' + justV.replace('\n', " ").replace('"', "'") + '", "complexidade":"' + str(totalComp) + '", "criticidade":"' + str(totalCrit) + '"}\r\n'
                lerAval = open('avalPort', 'r')
                listAval = lerAval.readlines()
                lerAval.close()
                lerAval = open('avalPort', 'w')
                lerAval.write(reg)
                for linhasAval in listAval:
                    if linhasAval != '\n':
                        dictLinhasAval = ast.literal_eval(linhasAval)
                        if dictLinhasAval['id'] != idProj:
                            lerAval.write(linhasAval)
                messagebox.showinfo('Salvar Avaliação', 'A Avaliação do projeto "' + nomeProj + '" foi salva com sucesso!')
                lerAval.close()
                mc.MenuPort(self.tipo, self.area, self.tela_old).atualizaPort()
                self.tela.destroy()
