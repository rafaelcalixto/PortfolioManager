import ast
import xml.etree.ElementTree as xml
from tkinter import messagebox

class LoadInfos():
    def __init__(self):
        self.portfolio = 'portfolios' ###  NOME DO ARQUIVO COM INFORMAÇÕES DOS PORTFOLIOS
        self.aval = 'avalPort' ###  NOME DO ARQUIVO COM AS AVALIAÇÕES DOS PORTFOLIOS
        self.setup = 'setup.xml' ###  NOME DO ARQUIVO COM AS CONFIGURAÇÕES DE SETUP
        self.peso = 'peso' ###  NOME DO ARQUIVO COM INFORMAÇÕES DE PESOS PARA AS AVALIAÇÕES

    #######  IMPORTAR INFORMAÇÕES DA VIEW XML  #######
    def loadConfigPort(self, busca):
        file = xml.parse('view.xml')
        data = file.getroot()
        campos = data.findall(busca)

        infos = {}
        parametros = []

        for subTags in campos:
            for keys in subTags:
                infos[keys.tag] = subTags.find(keys.tag).text
            parametros.append(infos)
            infos = {}
            
        return parametros

    #######  CONSULTA AVALIAÇÕES CADASTRADAS E CRIA LISTA COM INFORMAÇÃO DESEJADA  ########
    def criarListAval(self, chave):
        listaInfosAval = []
        lerAval = open(self.aval, 'r')
        listAval = lerAval.readlines()
        for linhasAval in listAval:
            if linhasAval != '\n':
                dictLinhasAval = ast.literal_eval(linhasAval)
                listaInfosAval.append(dictLinhasAval[chave])
        lerAval.close()

        return listaInfosAval

    #######  RETORNA UMA LISTA COM AS INFORMAÇÕES DOS PROJETOS SELECIONADOS E O TAMANHO NECESSÁRIO PARA A TELA  ########
    def loadProjs(self, area, tipo):
        listInfosProj = []
        lerPort = open(self.portfolio, 'r+')
        listPort = lerPort.readlines()
        for linhasPort in listPort:
            if linhasPort != '\n':
                dictLinhasPort = ast.literal_eval(linhasPort)
                if area == dictLinhasPort['area'] and tipo == dictLinhasPort['tipo']:
                    listInfosProj.append(dictLinhasPort)
        return listInfosProj

    ##########  FUNÇÃO PARA DELETAR UM PROJETO  ############
    def delProj(self, idProj, nomeProj):
        confirmar = messagebox.askokcancel('Deletar Projeto', 'Tem certeza que deseja deletar o projeto "' + nomeProj + '" ?')
        if confirmar:
            ########  SCRIPT PARA DELETAR O PROJETO  #########
            lerPort = open(self.portfolio, 'r')
            listPort = lerPort.readlines()
            lerPort.close()
            lerPort = open(self.portfolio, 'w')
            for linhasPort in listPort:
                if linhasPort != '\n':
                    dictLinhasPort = ast.literal_eval(linhasPort)
                    if dictLinhasPort['id'] != idProj:
                        lerPort.write(linhasPort)

            ########  SCRIPT PARA DELETAR A AVALIAÇÃO CORRESPONDENTE AO PROJETO  #########
            lerAval = open(self.aval, 'r')
            listAval = lerAval.readlines()
            lerPort.close()
            lerAval = open(self.aval, 'w')
            for linhasAval in listAval:
                if linhasAval != '\n':
                    dictLinhasAval = ast.literal_eval(linhasAval)
                    if dictLinhasAval['id'] != idProj:
                        lerAval.write(linhasAval)
            messagebox.showinfo('Deletar Projeto', 'O projeto "' + nomeProj + '" foi deletado!')
            lerPort.close()

    #######  LER XML PARA CARREGAR INFORMAÇÕES DE SETUP  #######
    def loadXML(self, tipo, campos):
        tipo = tipo.lower()
        teste = open(self.setup, encoding='utf-8', errors='ignore')
        file = xml.parse(teste)
        data = file.getroot()
        tagInfos = data.findall(tipo)

        infos = {}

        for valores in tagInfos:
            dicioInfos = valores.attrib
            if dicioInfos['type'] == campos:
                for keys in valores:                    
                    infos[keys.tag] = ast.literal_eval(valores.find(keys.tag).text)

        return infos

    def loadInfos(self, valor, valuesComp):
        listValor = []
        for x in valuesComp[valor]:
            listValor.append(x[0])

        return listValor

    #########  LER INFORMAÇÕES DO PROJETO E AVALIAÇÃO PARA A TELA DE DETALHES  ########

    def infosProj(self, idProj):

        ###########  INFORMAÇÕES DO PROJETO  #############

        avalProj = {"esforco":"Projeto não avaliado"}
        tamTela = 600

        #######  BUSCA INFORMAÇÕES DO PROJETO  ########  
        lerPort = open(self.portfolio, 'r')
        listPort = lerPort.readlines()
        for linhasPort in listPort:
            if linhasPort != '\n':
                dictLinhasPort = ast.literal_eval(linhasPort)
                if dictLinhasPort['id'] == idProj:
                    infoProj = dictLinhasPort
        lerPort.close()

        #######  BUSCA INFORMAÇÕES DA AVALIAÇÃO  ######## 
        lerAval = open(self.aval, 'r')
        listAval = lerAval.readlines()
        for linhasAval in listAval:
            if linhasAval != '\n':
                dictLinhasAval = ast.literal_eval(linhasAval)
                if dictLinhasAval['id'] == idProj:
                    avalProj = dictLinhasAval
                    tamTela = 1150
        lerAval.close()

        return infoProj, avalProj, tamTela

    def loadInfosExportExcel(self):
        portArea = []
        avalArea = []
        portConcluidos = []

        #########  LER ARQUIVO DE INFORMAÇÕES DO PORTFOLIO  #########
        lerPort = open('portfolios', 'r')
        listPort = lerPort.readlines()
        for linhasPort in listPort:
            if linhasPort != '\n':
                dictLinhasPort = ast.literal_eval(linhasPort)
                if dictLinhasPort['id'] in listIds:
                    if dictLinhasPort['status'] != 'Em produção':
                        portArea.append(dictLinhasPort)
                    else:
                        portConcluidos.append(dictLinhasPort)

        #########  LER ARQUIVO DE AVALIAÇÃO DO PORTFOLIO  #########
        lerAval = open('avalPort', 'r')
        listAval = lerAval.readlines()
        for linhasAval in listAval:
            if linhasAval != '\n':
                dictLinhasAval = ast.literal_eval(linhasAval)
                if dictLinhasAval['id'] in listIds:
                    avalArea.append(dictLinhasAval)

        return portArea, portConcluidos, avalArea

    #######  LER ARQUIVO DE SETUP PARA TELA DE SETUP  #######
    def lerSetup(self, tipo, infos):
        lerSetup = open(self.setup, 'r')
        listSetup = lerSetup.readlines()
        lerSetup.close()
        for linhasSetup in listSetup:
            if linhasSetup != '\n':
                dictLinhasSetup = ast.literal_eval(linhasSetup)
                if dictLinhasSetup['infos'] == infos and dictLinhasSetup['tipo'] == tipo:
                    return dictLinhasSetup

    #######  LER ARQUIVO DE PESO PARA TELA DE SETUP #######
    def lerPeso(self, tipo, infos):
        lerPeso = open(self.peso, 'r')
        listPeso = lerPeso.readlines()
        lerPeso.close()
        for linhasPeso in listPeso:
            if linhasPeso != '\n':
                dictLinhasPeso = ast.literal_eval(linhasPeso)
                if dictLinhasPeso['infos'] == infos and dictLinhasPeso['tipo'] == tipo:
                    return dictLinhasPeso

    #######  SALVAR ALTERAÇÕES DE PESO #######
    def salvarPeso(self, tela_old, tipo, infos, key, new_value, criterio):
        lerPeso = open(self.peso, 'r')
        listPeso = lerPeso.readlines()
        lerPeso.close()
        lerPeso = open(self.peso, 'w')
        for linhasPeso in listPeso:
            if linhasPeso != '\n':
                dictLinhasPeso = ast.literal_eval(linhasPeso)
                if dictLinhasPeso['infos'] == infos and dictLinhasPeso['tipo'] == tipo:
                    dictLinhasPeso[key] = new_value
                lerPeso.write(str(dictLinhasPeso) + '\r\n')
        messagebox.showwarning('Peso alterado', 'O Peso de "' + criterio + '" foi alterado com sucesso!')
        lerPeso.close()
        tela_old.destroy()       

    #######  SALVAR ALTERAÇÕES NO SETUP #######
    def salvarValue(self, tela_old, tipo, infos, campo, valor_old, valor_new):

        #######  VALIDAÇÃO  #######
        if len(valor_new) > 0:
            if not valor_new.isdecimal():
                messagebox.showwarning('Erro!','Informe um valor em formato numérico')
                return False
            elif int(valor_new) < 0 or int(valor_new) > 9:
                messagebox.showwarning('Erro!','O valor informado precisa estar entre 0 e 9')
                return False
        else:
            messagebox.showwarning('Erro!','Informe o novo valor!')
            tk.BaseWidget.focus_force(mustDoV)
            return False
        
        lerSetup = open(self.setup, 'r')
        listSetup = lerSetup.readlines()
        lerSetup.close()
        lerSetup = open(self.setup, 'w')
        for linhasSetup in listSetup:
            if linhasSetup != '\n':
                dictLinhasSetup = ast.literal_eval(linhasSetup)
                if dictLinhasSetup['infos'] != infos or dictLinhasSetup['tipo'] != tipo:
                    lerSetup.write(str(dictLinhasSetup) + '\r\n')
                elif dictLinhasSetup['infos'] == infos and dictLinhasSetup['tipo'] == tipo:
                    listAlterar = dictLinhasSetup[campo]
                    for x in listAlterar:
                        if valor_old == x[0]:
                            listAlterar.remove(x)
                            x[1] = valor_new
                            listAlterar.append(x)
                            dictLinhasSetup[campo] = listAlterar
                    lerSetup.write(str(dictLinhasSetup) + '\r\n')
        messagebox.showwarning('Valor alterado', 'O valor do registro foi alterado com sucesso!')
        lerSetup.close()
        tela_old.destroy()

    ########  FORMATAR TÍTULOS DE ACORDO COM O TAMANHO  ###########

    def formatText(self, texto, tamFonte = 14, limit_1 = 30, limit_2 = 60):
        tamanho = len(texto)
        if tamanho > limit_1 and tamanho < limit_2:
            texto = texto[:(texto.find(' ', limit_1 - 5))] + '\n' + texto[(texto.find(' ', limit_1 - 5)):]
        elif len(texto) > limit_2:
            texto = texto[:(texto.find(' ', limit_1 - 5))] + '\n' + texto[(texto.find(' ', limit_1 - 5)):(texto.find(' ', limit_2 - 5))] + '\n' + texto[(texto.find(' ', limit_2 - 5)):]
            
        tamFonte -= int(tamanho / 10)
        
        return texto, tamFonte

    ########  CALCULAR PONTUAÇÃO DE CRITICIDADE E COMPLEXIDADE  ########

    def avalCompCrit(self, tipo, area, idProj, dictAvals):
        totalComp = 0
        totalCrit = 0

        ##########  CARREGAR INFORMAÇÕES DE NOTA DE CADA AVALIAÇÃO  ###########
        lerAval = open(self.setup, 'r')
        listAval = lerAval.readlines()
        for linhasAval in listAval:
            if linhasAval != '\n':
                dictLinhasAval = ast.literal_eval(linhasAval)
                if tipo == dictLinhasAval['tipo'] and dictLinhasAval['infos'] == 'complexidade':
                    compVals = dictLinhasAval
                elif tipo == dictLinhasAval['tipo'] and dictLinhasAval['infos'] == 'criticidade':
                    critVals = dictLinhasAval
        lerAval.close()
        
        ##########  PESO AVALIAÇÃO  ##########
        pesosComp = lerPeso(tipo, 'complexidade')    
        pesosCrit = lerPeso(tipo, 'criticidade')
        stringFinal = '{"id":"' + idProj + '"'

        #################  ALGORITMO DE AVALIAÇÃO DA COMPLEXIDADE DO PROJETO  ##################
        for x in ('esforco', 'conf', 'hab', 'numProfs', 'escop', 'comp', 'dispTec', 'difTec', 'impact'):
            for y in compVals[x]:
                if y[0] == dictAvals[x]:
                    totalComp += int(y[1]) * int(pesosComp[x])
                    stringFinal += ', "' + x + '":"' + str(dictAvals[x]) + '", "peso_' + x + '":"' + str(pesosComp[x]) + '"'
                    
        #################  ALGORITMO DE AVALIAÇÃO DA CRITICIDADE DO PROJETO  ##################
        for x in ('ativVital', 'numArea', 'relMetas', 'roi', 'mustDo'):
            for y in critVals[x]:
                if y[0] == dictAvals[x]:
                    totalCrit += int(y[1]) * int(pesosCrit[x])
                    stringFinal += ', "' + x + '":"' + str(dictAvals[x]) + '", "peso_' + x + '":"' + str(pesosCrit[x]) + '"'

        return totalComp, totalCrit, stringFinal

    ########  SALVA OS DADOS DO PROJETOS  ########

    def registrarNovo(self, tipo, area, ident, status, nome, solic, geren, ticket, custo, subarea, resp, budget):
        arqReg = open(self.portfolio, 'r+')

        #####  IDENTIFICAR O ÚLTIMO ID  #####
        lerReg = arqReg.readlines()
        if len(lerReg) > 0:
            for lr in lerReg:
                if lr != '\n':
                    dictLerReg = ast.literal_eval(lr)
                    ident = int(dictLerReg['id']) + 1

        reg = '{"id":' + '"' + str(ident) + '"' + ', "tipo":' + '"' + tipo + '"' + ', "area":' + '"' + area + '"' + ', "status":' + '"' + status + '"' + ', "projeto":' + '"' + nome.replace('\n', " ").replace('"', "'") + '"' + ', "ticket":' + '"' + ticket.replace('\n', " ").replace('"', "'") + '"' + ', "solicitante":' + '"' + solic.replace('\n', " ").replace('"', "'") + '"' + ', "gerencia":' + '"' + geren.replace('\n', " ").replace('"', "'") + '"' + ', "subarea":' + '"' + subarea.replace('\n', " ").replace('"', "'") + '"' + ', "budget":' + '"' + budget + '"' + ', "responsavel":' + '"' + resp + '"' + '}\r\n'

        #####  SALVAR INFOS  #####
        arqReg.write(reg)
        arqReg.close()

    def registrarEditado(self, tipo, area, ident, status, nome, solic, geren, ticket, custo, subarea, resp, budget):
        arqReg = open(self.portfolio, 'r+')
        lerReg = arqReg.readlines()
        arqReg.close()

        reg = '{"id":' + '"' + str(ident) + '"' + ', "tipo":' + '"' + tipo + '"' + ', "area":' + '"' + area + '"' + ', "status":' + '"' + status + '"' + ', "projeto":' + '"' + nome.replace('\n', " ").replace('"', "'") + '"' + ', "ticket":' + '"' + ticket.replace('\n', " ").replace('"', "'") + '"' + ', "solicitante":' + '"' + solic.replace('\n', " ").replace('"', "'") + '"' + ', "gerencia":' + '"' + geren.replace('\n', " ").replace('"', "'") + '"' + ', "subarea":' + '"' + subarea.replace('\n', " ").replace('"', "'") + '"' + ', "budget":' + '"' + budget + '"' + ', "responsavel":' + '"' + resp + '"' + '}\r\n'
        
        arqReg = open(self.portfolio, 'w')
        for linhasProj in lerReg:
            if linhasProj != '\n':
                dictLinhasProj = ast.literal_eval(linhasProj)
                if dictLinhasProj['id'] == str(ident):
                    arqReg.write(reg)
                else:
                    arqReg.write(linhasProj)

    def alterarSetupCarac():
        confirmar = messagebox.askokcancel('Salvar Setup', 'Tem certeza que deseja alterar o setup dos projetos?')
        if confirmar:           
            lerSetup = open(self.setup, 'r')
            listSetup = lerSetup.readlines()
            lerSetup.close()
            lerSetup = open(self.setup,'w')
            for linhasSetup in listSetup:
                if linhasSetup != '\n':
                    dictLinhasSetup = ast.literal_eval(linhasSetup)
                    if dictLinhasSetup['infos'] != 'projeto' or dictLinhasSetup['tipo'] != tipo:
                        lerSetup.write(linhasSetup)
                    elif dictLinhasSetup['infos'] == 'projeto' and dictLinhasSetup['tipo'] == tipo:
                        for ids in config.keys():
                            if ids not in ['tipo', 'infos']:
                                dictLinhasSetup[ids].append(config[ids])
                        lerSetup.write(str(dictLinhasSetup) + '\r\n')
                        messagebox.showwarning('Setup Salvo!', 'O Setup foi salvo com sucesso')
            lerSetup.close()

    def restaurarSetupCarac(tipo, defaultCarac):
        confirmar = messagebox.askokcancel('Restaurar Setup', 'Tem certeza que deseja restaurar o setup original?')
        if confirmar:           
            lerSetup = open('setup', 'r')
            listSetup = lerSetup.readlines()
            lerSetup.close()
            lerSetup = open('setup','w')
            for linhasSetup in listSetup:
                if linhasSetup != '\n':
                    dictLinhasSetup = ast.literal_eval(linhasSetup)
                    if dictLinhasSetup['infos'] != 'projeto' or dictLinhasSetup['tipo'] != tipo:
                        lerSetup.write(linhasSetup)
                    elif dictLinhasSetup['infos'] == 'projeto' and dictLinhasSetup['tipo'] == tipo:
                        lerSetup.write(defaultCarac)
                        messagebox.showwarning("Setup Restaurado!", "O setup original foi restaurado com sucesso")
            lerSetup.close()

    def alterarSetupAval(valores):
        work = False
        confirmar = messagebox.askokcancel('Salvar Setup', 'Tem certeza que deseja alterar o setup dos projetos?')
        if confirmar:           
            lerSetup = open('setup', 'r')
            listSetup = lerSetup.readlines()
            lerSetup.close()
            lerSetup = open('setup','w')
            for linhasSetup in listSetup:
                if linhasSetup != '\n':
                    dictLinhasSetup = ast.literal_eval(linhasSetup)
                    if dictLinhasSetup['infos'] != valores['infos'] or dictLinhasSetup['tipo'] != valores['tipo']:
                        lerSetup.write(linhasSetup)
                    elif dictLinhasSetup['infos'] == valores['infos'] and dictLinhasSetup['tipo'] == valores['tipo']:
                        for ids in valores.keys():
                            if ids not in ['tipo','infos']:
                                dictLinhasSetup[ids].append(valores[ids])
                        lerSetup.write(str(dictLinhasSetup) + '\r\n')
                        work = True
            lerSetup.close()
        return work

    def restaurarSetupAval(self, infos, tipo, restaurarDefault):
        ok_setup = False
        ok_pesos = False
            
        confirmar = messagebox.askokcancel('Restaurar Setup', 'Tem certeza que deseja restaurar o setup original?')
        if confirmar:           
            lerSetup = open('setup', 'r')
            listSetup = lerSetup.readlines()
            lerSetup.close()
            lerSetup = open('setup','w')
            for linhasSetup in listSetup:
                if linhasSetup != '\n':
                    dictLinhasSetup = ast.literal_eval(linhasSetup)
                    if dictLinhasSetup['infos'] != infos or dictLinhasSetup['tipo'] != tipo:
                        lerSetup.write(linhasSetup)
                    elif dictLinhasSetup['infos'] == infos and dictLinhasSetup['tipo'] == tipo:
                        lerSetup.write(restaurarDefault[0])
                        ok_setup = True
            lerSetup.close()

            lerPeso = open('peso', 'r')
            listPeso = lerPeso.readlines()
            lerPeso.close()
            lerPeso = open('peso','w')
            for linhasPeso in listPeso:
                if linhasPeso != '\n':
                    dictLinhasPeso = ast.literal_eval(linhasPeso)
                    if dictLinhasPeso['infos'] != infos or dictLinhasPeso['tipo'] != tipo:
                        lerPeso.write(linhasPeso)
                    elif dictLinhasPeso['infos'] == infos and dictLinhasPeso['tipo'] == tipo:
                        lerPeso.write(restaurarDefault[1])
                        ok_pesos = True
            lerPeso.close()

        if ok_setup and ok_pesos:
            messagebox.showwarning("Setup Restaurado!", "O setup original foi restaurado com sucesso")
