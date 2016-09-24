import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import asyncio
import time

import MenuConsulta as mc
import About as ab
import LoadInfos as li

#####  FONTES  #####

fontTitulo = ('Arial', 20)
fontCampos = ('Verdana', 12)
tela = None

class Principal(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'Portfolios')
        tk.Tk.wm_minsize(self, width = 640, height = 500)
        tk.Tk.wm_minsize(self, width = 641, height = 501)

        container = tk.Frame(self)
        container.place(width = 1360, height = 768, bordermode = 'outside')

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for f in (Home, busc_port):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row = 0, column = 0, sticky = 'nsew')

        self.show_frame(Home)
        tk.Tk.iconbitmap(self, default="portfolio_icone.ico")

    def show_frame(self, cont):
        frame = self.frames[cont]
        
        frame.tkraise()

#######  PAGINA INICIAL  #######
class Home(tk.Frame):
    global tela
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        
        titulo = tk.Label(self, text='Portfolio Manager', font= fontTitulo)
        titulo.place(x = 150, y = 20, width = 340)

        img = tk.PhotoImage(file = 'about.png')
        about = tk.Button(self, image = img, command = lambda: ab.About().winAbout())
        about.image = img
        about.place(x = 560, y = 20, width = 70, height = 70)

        tk.Label(self, text = 'Selecione o tipo',
                 font = fontCampos).place(x = 250, y = 170, width = 140)
        tipoPort = tk.ttk.Combobox(self,
                               text = 'Tipo',
                               state = 'readonly',
                               values = ['Causa Raiz', 'Melhoria', 'Projeto'])
        tipoPort.place(x = 260, y = 200, width = 120)

        LoadInfos = li.LoadInfos()
        valoresSetup = LoadInfos.loadXML('projeto', 'caracteristicas')

        tk.Label(self, text = 'Selecione a área',
                 font = fontCampos).place(x = 250, y = 230, width = 140)
        areaPort = tk.ttk.Combobox(self,
                               text = 'Área',
                               state = 'readonly',
                               values = valoresSetup['areas'])
        areaPort.place(x = 260, y = 260, width = 120)

        consultPort = ttk.Button(self, text = 'Iniciar',
                                 command = lambda: validInfosPort(areaPort, tipoPort, tela)
                                 ).place(x = 280, y = 290)

        def validInfosPort(area, tipo, tela):
            ## VALIDAÇÕES ##
            if len(tipo.get()) < 2:
                messagebox.showwarning('Tipo inválido', 'Informe o Tipo de Portfolio')
                tk.BaseWidget.focus_force(tipo)
            elif len(area.get()) < 2:
                messagebox.showwarning('Área inválida', 'Informe a Área do Portfolio')
                tk.BaseWidget.focus_force(area)
            else:
                controller.show_frame(busc_port)
                criarMenu = mc.MenuPort(tipo.get().replace(' ', ''), area.get(), tela)
                criarMenu.listaPort()
                criarMenu.atualizaPort()
                
#######  PAGINA DE CRIACAO DE PORTFOLIO  #######
        
class busc_port(tk.Frame):
    def __init__(self, parent, controller):
        global tela
        tk.Frame.__init__(self, parent)
        tela = self

        #######  RETORNAR A MENU PRINCIPAL  ########
        img = tk.PhotoImage(file = 'back.png')
        voltar = tk.Button(self, image = img, command = lambda: controller.show_frame(Home))
        voltar.image = img
        voltar.place(x = 10, y = 15)

app = Principal()
app.mainloop()
