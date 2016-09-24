import tkinter as tk
from tkinter import ttk
import ast

fontTitulo = ('Arial Black', 12)
fontCampos = ('Verdana', 10)

def form():
    global fontTitulo
    global fontCampos
    
    port = tk.Tk()
    port.wm_title('Portfolio')
    port.wm_minsize(width = 800, height = 600)

    posxC = posyC = posxL = posyL = 30
    
    ##########  CABECALHO  ############
    
    solic = tk.Label(port,
                      text = 'Solicitante',
                      bg = 'grey',
                      bd = 2,
                      relief = 'solid',
                      font = fontTitulo,
                      width = 22,
                      height = 2)
    posyC -= 10
    solic.place(x = posxC, y = posyC)
    
    geren = tk.Label(port,
                      text = 'Gerencia',
                      bg = 'grey',
                      bd = 2,
                      relief = 'solid',
                      font = fontTitulo,
                      width = 22,
                      height = 2)
    posxC += 244
    geren.place(x = posxC, y = posyC)
    
    projeto = tk.Label(port,
                      text = 'Projeto',
                      bg = 'grey',
                      bd = 2,
                      relief = 'solid',
                      font = fontTitulo,
                      width = 66,
                      height = 2)
    posxC += 244
    projeto.place(x = posxC, y = posyC)

    subarea = tk.Label(port,
                      text = 'Área',
                      bg = 'grey',
                      bd = 2,
                      relief = 'solid',
                      font = fontTitulo,
                      width = 22,
                      height = 2)
    posxC += (240 * 3)
    subarea.place(x = posxC, y = posyC)

    
    ##########  LINHAS  ############
    lerPort = open('portfolios', 'r+')
    listPort = lerPort.readlines()
    for linhasPort in listPort:
        if linhasPort != '\n':
            posyL += 36
            dictLinhasPort = ast.literal_eval(linhasPort)

            solic = tk.Label(port,
                              text = dictLinhasPort['solicitante'],
                              bg = 'white',
                              bd = 2,
                              relief = 'solid',
                              font = fontCampos,
                              width = 30,
                              height = 2)
            solic.place(x = posxL, y = posyL)

            geren = tk.Label(port,
                              text = dictLinhasPort['gerencia'],
                              bg = 'white',
                              bd = 2,
                              relief = 'solid',
                              font = fontCampos,
                              width = 30,
                              height = 2)
            posxL += 244
            geren.place(x = posxL, y = posyL)

            projeto = tk.Label(port,
                              text = dictLinhasPort['projeto'],
                              bg = 'white',
                              bd = 2,
                              relief = 'solid',
                              font = fontCampos,
                              width = 90,
                              height = 2)
            posxL += 244
            projeto.place(x = posxL, y = posyL)

            subarea = tk.Label(port,
                              text = dictLinhasPort['subarea'],
                              bg = 'white',
                              bd = 2,
                              relief = 'solid',
                              font = fontCampos,
                              width = 90,
                              height = 2)
            posxL += (240 * 3)
            subarea.place(x = posxL, y = posyL)

            posxL = 30
