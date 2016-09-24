import tkinter as tk
from tkinter import ttk
import ast
from tkinter import messagebox

import LoadInfos as li
import MenuConsulta as mc

class Formulario:
    def __init__(self, Portfolio, tela_lista, infosProj = None, tela_dead = None):
        self.tela_dead = tela_dead
        self.tela = tk.Tk()
        self.tela_lista = tela_lista
        self.Portfolio = Portfolio
        self.LoadInfos = li.LoadInfos()
        self.tipo, self.area = Portfolio.infoPort()
        self.infoForm = self.Portfolio.infoForm()
        self.infosProj = infosProj
        self.editado = False
        self.valores = self.LoadInfos.loadXML(self.tipo, 'caracteristicas')
        self.fontTitulo = ('Arial', 20)
        self.fontCampos = ('Verdana', 12)
        self.ident = '1'

    def form(self):
        self.tela.wm_title('Registrar ' + self.tipo + ' de ' + self.area)
        self.tela.wm_minsize(width = 640, height = 500)

        if self.tela_dead != None:
            self.tela_dead.destroy()

        ################  FORMULÁRIO DO PORTFOLIO  ###############
        
        tk.Label(self.tela, text = 'Adicionar ' + self.tipo, font = self.fontTitulo).place(x = 210, y = 20, width = 230)

        #######  ÁREA DE PORTFOLIO  #######

        statusL = tk.Label(self.tela, text = 'Status', font = self.fontCampos)
        status = ttk.Combobox(self.tela, state = 'readonly', values = self.valores['status'])
        
        if 'Status' in self.infoForm:
            statusL.place(x = 10, y = 90)
            status.place(x = 10, y = 120, width = 120)

        #######  BUDGET  #######

        budgetL = tk.Label(self.tela, text = 'Budget', font = self.fontCampos)
        budget = ttk.Combobox(self.tela, state = 'readonly', values = self.valores['budget'])
        
        if 'Budget' in self.infoForm:
            budgetL.place(x = 510, y = 90)
            budget.place(x = 510, y = 120, width = 100)

        ######  NOME DO PROJETO  #######

        nomeL = tk.Label(self.tela, text = 'Nome:', font = self.fontCampos)
        nome = tk.Entry(self.tela)

        if 'Nome' in self.infoForm:
            nomeL.place(x = 10, y = 180)
            nome.place(x = 10, y = 210, width = 500)

        #######  SOLICITANTE  ########

        solicL = tk.Label(self.tela, text = 'Solicitante:', font = self.fontCampos)
        solic = tk.Entry(self.tela)
        
        if 'Solicitante' in self.infoForm:
            solicL.place(x = 10, y = 270)
            solic.place(x = 10, y = 300, width = 200)

        #######  GERÊNCIA  ########
    
        gerenL = tk.Label(self.tela, text = 'Gerência:', font = self.fontCampos)
        geren = tk.Entry(self.tela)

        if 'Gerência' in self.infoForm:
            gerenL.place(x = 260, y = 270)
            geren.place(x = 260, y = 300, width = 200)

        #######  REGISTRO NO CA  #######

        ticketL = tk.Label(self.tela, text = 'Ticket: ', font = self.fontCampos)
        ticket = tk.Entry(self.tela)
            
        if 'Ticket' in self.infoForm:
            ticketL.place(x = 510, y = 270)
            ticket.place(x = 510, y = 300, width = 100)

        #######  CUSTO  ########

        custoL = tk.Label(self.tela, text = 'Custo:', font = self.fontCampos)
        custo = tk.Entry(self.tela)
        
        if 'Custo' in self.infoForm:
            custoL.place(x = 10, y = 360)
            custo.place(x = 10, y = 390, width = 200)

        #######  SUB ÁREA  ########

        subareaL = tk.Label(self.tela, text = 'Sub Área:', font = self.fontCampos)
        subarea = tk.Entry(self.tela)
            
        if 'Sub Área' in self.infoForm:
            subareaL.place(x = 10, y = 360)
            subarea.place(x = 10, y = 390, width = 200)

        #######  FUNCIONAL RESPONSAVEL  ########

        respL = tk.Label(self.tela, text = 'Analista Responsavel:', font = self.fontCampos)
        resp = ttk.Combobox(self.tela, state = 'readonly', values = self.valores['resp'])

        if 'Analista Responsavel' in self.infoForm:
            respL.place(x = 230, y = 360)
            resp.place(x = 230, y = 390, width = 300)

        #######  CARREGAR INFOS NO MODO DE EDIÇÃO  ########

        if self.infosProj != None:
            self.editado = True
            status.set(self.infosProj['status'])
            budget.set(self.infosProj['budget'])
            projeto.insert(0, self.infosProj['projeto'])
            solic.insert(0, infosProj['solicitante'])
            geren.insert(0, infosProj['gerencia'])
            chamadoCA.insert(0, infosProj['ticket'])
            subarea.insert(0, infosProj['subarea'])
            resp.set(infosProj['responsavel'])

            self.ident = self.infosProj['id']

        #######  DICIONÁRIO DOS OBJETOS  ########

        objetos = {
                     'Status':status
                   , 'Nome':nome
                   , 'Solicitante':solic
                   , 'Gerência':geren
                   , 'Ticket':ticket
                   , 'Custo':custo
                   , 'Sub Área':subarea
                   , 'Funcional Responsável':resp
                   , 'Budget':budget
                   }

        #######  SALVAR PROJETO  ########

        salvar = tk.Button(self.tela,
                           text = 'Salvar ' + self.tipo,
                           command = lambda: registrar())
        salvar.place(x = 530, y = 450, width = 100)

        #######  TESTE  ########

    ##    visual = tk.Button(self, text = 'TESTAR', command = lambda: registrar('Em análise', 'Teste' + projeto.get(), 'Teste', 'Teste', 'Teste', 'Teste', 'Ilma Oliveira', 'Outros', False))
    ##    visual.place(x = 200, y = 450, width = 100)

        def registrar():
            validar = self.Portfolio.adicionar(self.editado, self.ident, status.get(), nome.get(), solic.get(), geren.get(), ticket.get(), custo.get(), subarea.get(), resp.get(), budget.get())

            if validar in objetos.keys():
                messagebox.showwarning(validar + ' inválida!', 'O campo ' + validar + ' é obrigatório!')
                tk.BaseWidget.focus_force(objetos[validar])
                return False

            ########  LIMPAR CAMPOS  ########

            messagebox.showinfo('Registro Realizado', 'O Projeto foi registrado com sucesso!')
            
            if not self.editado:
                mc.MenuPort(self.tipo, self.area, self.tela_lista).atualizaPort()
                Formulario(self.Portfolio, self.tela_lista, tela_dead = self.tela).form()
