import tkinter as tk
from tkinter import ttk

class About:
    def __init__(self):
        self.tela = tk.Tk()
        self.fonte = ('Ariel Black', 12)
        self.texto = 'Portfolio Manager\nVersão 1.1\n\nPortfolio Manager é um sistema\nOpen Source de gerenciamento de melhorias\ne projetos desenvolvido por\nRafael Calixto Ferreira de Araújo.\n\nContato: rafaelcf.araujo@gmail.com'
    
    def winAbout(self):
        self.tela.wm_title('About')
        self.tela.wm_minsize(width = 300, height = 180)
        tk.Label(self.tela, text = self.texto, font = self.fonte).pack(side = 'left')
