import LoadInfos as li

class Portfolio():
    def __init__(self, tipo, area):
        self.tipo = tipo
        self.area = area
        self.LoadInfos = li.LoadInfos()
        self.formulario, self.avalComplex, self.avalCritic = self.LoadInfos.loadConfigPort('Carac')
        self.defaultCarac, self.defaultComplex, self.defaultCritic = self.LoadInfos.loadConfigPort('OpCore')

    def infoPort(self):
        return self.tipo, self.area

    def load(self):
        portfolio = self.LoadInfos.loadProjs(self.area, self.tipo)

        return portfolio

    def adicionar(self, editado, ident, status, nome, solic, geren, ticket, custo, subarea, resp, budget):
        if len(status) < 2:
            return 'Status'
        elif len(nome) < 2 or len(nome) > 100:
            return 'Nome'
        elif len(solic) < 1 or len(solic) > 30:
            return 'Solicitante'
        elif len(geren) < 1 or len(geren) > 30:
            return 'Gerência'
        elif len(ticket) < 1 or len(geren) > 30:
            return 'Ticket'
        elif self.area == 'Projeto' and len(custo) < 1:
            return 'Custo'
##        elif len(subarea) > 30:
##            return 'Sub Área'
        elif len(resp) < 2 or len(resp) > 100:
            return 'Funcional Responsável'
        elif len(budget) < 1 or len(budget) > 30:
            return 'Budget'

        if editado:
            self.LoadInfos.registrarEditado(self.tipo, self.area, ident, status, nome, solic, geren, ticket, custo, subarea, resp, budget)
        else:
            self.LoadInfos.registrarNovo(self.tipo, self.area, ident, status, nome, solic, geren, ticket, custo, subarea, resp, budget)

    def infoForm(self):
        return self.formulario[self.tipo]

    def infoAvalComplex(self):
        return self.avalComplex[self.tipo]

    def infoAvalCritic(self):
        return self.avalCritic[self.tipo]

    def alterarInfosCarac(self, area, status, budget, resp):
        config = {"tipo":tipo,"infos":"projeto"}
        if len(a) > 1:
            config["area"] = a.replace('\n', " ").replace("'", '"')
        if len(s) > 1:
            config["status"] = s.replace('\n', " ").replace("'", '"')
        if len(b) > 1:
            config["budget"] = b.replace('\n', " ").replace("'", '"')
        if len(r) > 1:
            config["resp"] = r.replace('\n', " ").replace("'", '"')

        if len(config.keys()) < 2:
            return False

        self.LoadInfos.alterarSetupCarac(config)

    def restaurarInfosCarac():
        self.LoadInfos.restaurarSetupCarac(self.tipo, self.defaultCarac)

    def alterarInfosAval(self, tipoAval, valores):
        camposValidos = False

        for key in valores.keys():
            infos = valores[key]
            valor = infos[0]
            peso = infos[1]
            ################  VALIDAÇÃO  ##################
            if len(valor) > 1:
                if valor.isdecimal():
                    return [key, 0, 'Informe um valor em formato de texto para ']
                if len(peso) < 1:
                    return [key, 1, 'Nenhum peso foi informado para ']
            if len(peso) > 0:
                if len(valor) < 1:
                    return [key, 0, 'Nenhum valor foi informado para ']
            if len(valor) > 1 and len(peso) > 0:
                config[key] = [valor.replace('\n', " ").replace("'", '"'), peso.replace('\n', " ").replace("'", '"')]
                camposValidos = True
                
        if camposValidos == False:
            return ['fail', 0, 'Nenhum campo foi preenchido']
        
        valores['tipo'] = self.tipo
        work = self.LoadInfos.alterarSetupAval(tipo, valores)

        if work:
            return ['work', 0, 'O Setup de ' + infos + ' foi salvo com sucesso'] 

    def restaurarInfosAval(self, infos):
        if infos == "complexidade":
            self.LoadInfos.restaurarSetupAval(infos, self.tipo, self.defaultComplex[self.tipo])
        if infos == "criticidade":
            self.LoadInfos.restaurarSetupAval(infos, self.tipo, self.defaultCritic[self.tipo])
