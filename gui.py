import os
import sys
import time

import frog
import error
import lexico
import pe
import sintactico
import semantico
import webbrowser
import tkinter as tk
from screeninfo import get_monitors
from tkinter import filedialog
from tkinter.ttk import Progressbar
from tkinter import ttk, Frame, Menu
from ttkthemes import ThemedStyle
from tkinter.scrolledtext import ScrolledText
from tkinter import Scrollbar
import tkcode
from tkcode import CodeEditor
from pygments import highlight
from pygments.formatters import *
from pygments.styles import get_style_by_name
from pygments.formatters import get_formatter_by_name
from pygments.lexers import PrologLexer
from pygments.lexers import JLexer


import ts



def gui():
    # Barra de herramientas
    def abrir():
        # Abre el cuadro de diálogo para seleccionar el archivo
        archivo = filedialog.askopenfilename(filetypes=[("Archivos de código Frog", "*.fg")])

        # Si se selecciona un archivo, lo abrimos y mostramos el contenido en la consola
        if archivo:
            with open(archivo, "r") as f:
                contenido = f.read()
                code_editor.delete("0.0", tk.END)
                code_editor.insert("0.0", contenido)
                al_label.config(background="")
                ast_label.config(background="")
                asm_label.config(background="")
                salidadat.delete("0.0", tk.END)
                # Recorre cada fila de la tabla
                for fila in tabla.get_children():
                    # Elimina los datos de cada celda
                    tabla.delete(fila)

    def guardar():
        with open("programa.fg", 'w') as archivo:
            archivo.truncate(0)

        with open("programa.fg", "w") as archivo:
            ff = code_editor.get("1.0", tk.END)
            archivo.write(ff)

    def pausar():
        time.sleep(1)

    def ejecutar():

        print('-------------------------------------------------------------------------------')

        ts.tablasimbolos.clear()
        pe.pilaerrores.clear()

        def mostrarts(ttsabla):

            for fila in tabla.get_children():
                # Elimina los datos de cada celda
                tabla.delete(fila)

            if ttsabla:
                for i in range(0, len(ttsabla)):
                    tabla.insert(parent='', index='end', iid=str(i), text=str(i),
                                 values=(ttsabla[i]))


            else:
                salidadat.delete("0.0", tk.END)
                salidadat.insert("0.0", "Sin código")

        def mostrarpe(ppila):
            if ppila:
                salidadat.delete("0.0", tk.END)
                mi_lista = ppila
                mi_lista_limpia = [tupla for tupla in mi_lista if any(tupla)]
                for i in range(0, len(mi_lista_limpia)):
                    mi_lista = pe.pilaerrores
                    mi_lista_limpia = [tupla for tupla in mi_lista if any(tupla)]

                    sor = str(mi_lista_limpia[i][0])
                    strr = (str(sor) + ':\t' + str(error.error[sor]) +
                            '\n\tSímbolo encontrado: ' + mi_lista_limpia[i][1] +
                            '\n\tEn línea: ' + str(mi_lista_limpia[i][2]) + '\n')
                    salidadat.insert("0.0", strr)
            else:
                salidadat.delete("0.0", tk.END)
                salidadat.insert("0.0", "Pasa algo")


        pe.ban=0
        al_label.config(background="")
        ast_label.config(background="")
        asm_label.config(background="")


        al_label.config(background="blue")

        ttsabla = []

        al = lexico.analizador_lexico("programa.fg")
        print("resultado_lexico: ", al)
        ttsabla = ts.tablasimbolos

        mostrarts(ttsabla)


        if al ==0:
            al_label.config(background="green")
            ast = sintactico.analizador_sintactico("programa.fg")
            print("resultado_sintactico: ",ast)
            ttsabla = ts.tablasimbolos
            mostrarts(ttsabla)
            if ast ==0:
                ast_label.config(background="green")
                asm = semantico.analizador_semantico(ttsabla,"programa.fg")
                print("resultado_semantico: ", ast)
                ttsabla = ts.tablasimbolos
                mostrarts(ttsabla)

                if asm==0:
                    asm_label.config(background="green")
                    salidadat.delete("0.0", tk.END)
                    salidadat.insert("0.0", "¡Compilación completa!")
                else:
                    asm_label.config(background="red")
                    ttsabla = ts.tablasimbolos
                    mostrarts(ttsabla)
                    ppila = pe.pilaerrores
                    mostrarpe(ppila)
            else:
                ast_label.config(background="red")
                ttsabla = ts.tablasimbolos
                mostrarts(ttsabla)
                ppila = pe.pilaerrores
                mostrarpe(ppila)

        else:
            al_label.config(background="red")
            ttsabla = ts.tablasimbolos
            indice = len(ttsabla)

            ppila = pe.pilaerrores

            for tupla in ts.tablasimbolos:
                if tupla[7] < pe.pilaerrores[0][2]:
                    indice = ts.tablasimbolos.index(tupla)
                else:
                    indice = ts.tablasimbolos.index(tupla)
                    break;

            ttsabla = ttsabla[:indice]

            mostrarts(ttsabla)
            mostrarpe(ppila)



        print(ttsabla)

        # Recorre cada fila de la tabla











    def ayuda():
        webbrowser.open("https://drive.google.com/file/d/1IlOpESEFu9kYUjOK6p8xTpapDqrmKm22/view?usp=drive_link")

    def abirpdflen():
        webbrowser.open("https://drive.google.com/file/d/1lfOLi_zGBKtC-qtJvip9ifq85SyFgD6I/view?usp=drive_link")

    def abirpdflex():
        webbrowser.open("https://drive.google.com/file/d/1aYNaCgRkS1qy3ytrkcBsEUPXbMzAQVlH/view?usp=drive_link")

    def abirpdfsin():
        webbrowser.open("https://drive.google.com/file/d/1_0742q2jFG2o5WGRndX30sO_p3qx26-D/view?usp=drive_link")

    def abirpdfsem():
        webbrowser.open("https://drive.google.com/file/d/14ShGR_ZKug5ohIZ4sjPTSlxS9Y_YZDR5/view?usp=drive_link")

    def salir():
        print("¡Adiós!")
        window.destroy()


    # Función para resaltar la sintaxis del texto

    # Función para sincronizar el medidor de línea con el ScrolledText
    def sincronizar_medidor(event):
        listbox.delete(0, tk.END)
        contenido = textarea.get('1.0', 'end-1c')
        lineas = contenido.split('\n')
        for i in range(len(lineas)):
            listbox.insert(tk.END, str(i + 1))




    # Crear ventana
    window = tk.Tk()
    window.title("Frog IDE")
    #window.configure(bg=colorr)

    # Obtener el tamaño de la pantalla
    screen_width = get_monitors()[0].width
    screen_height = get_monitors()[0].height

    # Ajustar el tamaño de la ventana al tamaño de la pantalla
    window.geometry(f"{int(screen_width)}x{int(screen_height)}")

    # Menú
    menubar = tk.Menu(window)

    file_menu = tk.Menu(menubar)
    file_menu.add_command(label="Abrir", command=abrir)
    file_menu.add_command(label="Guardar", command=guardar)
    file_menu.add_separator()
    file_menu.add_command(label="Salir", command=salir)

    help_menu = tk.Menu(menubar)
    help_menu.add_command(label="Acerca de", command=ayuda)

    pdf_menu2 = tk.Menu(help_menu)
    pdf_menu2.add_command(label="Definición del lenguaje", command=abirpdflen)
    pdf_menu2.add_command(label="Análisis léxico", command=abirpdflex)
    pdf_menu2.add_command(label="Análisis sintáctico", command=abirpdfsin)
    pdf_menu2.add_command(label="Análisis semántico", command=abirpdfsem)


    run_menu = tk.Menu(menubar)
    run_menu.add_command(label="Ejecutar", command=ejecutar)

    menubar.add_cascade(menu=file_menu, label="Archivo")
    menubar.add_cascade(menu=help_menu, label="Ayuda")
    help_menu.add_cascade(menu=pdf_menu2, label="Ayuda")
    menubar.add_cascade(menu=run_menu, label="Ejecutar")

    window.config(menu=menubar)

    # Crear una barra de herramientas
    toolbar = ttk.Frame(window)
    toolbar.grid(row=0, column=5)

    # Semáforo
    al_label = ttk.Label(toolbar, text="AL")
    al_label.grid(row=0, column=0, padx=10, pady=10)
    al_label.config(relief="solid", borderwidth=2)
    al_label.config(padding="5")

    ast_label = ttk.Label(toolbar, text="ASt")
    ast_label.grid(row=0, column=1, padx=10, pady=10)
    ast_label.config(relief="solid", borderwidth=2)
    ast_label.config(padding="5")

    asm_label = ttk.Label(toolbar, text="ASm")
    asm_label.grid(row=0, column=2, padx=10, pady=10)
    asm_label.config(relief="solid", borderwidth=2)
    asm_label.config(padding="5")

    # Ventana de código
    def scrollbar_movimiento(*args):
        textarea.yview(*args)
        listbox.yview(*args)
        canvas.yview(*args)

    frame = Frame(window)
    #frame.grid(row=1, column=0)

    sw_cv = int(screen_width * 0.00219619)
    sh_cv = int(screen_height * 0.03125)

    canvas = tk.Canvas(frame, width=sw_cv,height=sh_cv)
    canvas.grid(row=1, column=6)
    scrollbar = ttk.Scrollbar(frame)
    scrollbar.place(relheight=0.2)
    #scrollbar.grid(row=1, column=6)
    canvas.config(yscrollcommand=scrollbar.set)

    sh_cv2 = int(screen_height * 0.03125)
    canvas.config(scrollregion=canvas.bbox("all"), height=sh_cv2)

    sw_ta = int(screen_width * 0.0549048)
    sh_ta = int(screen_height * 0.031770833)

    textarea = ScrolledText(frame, yscrollcommand=scrollbar.set, width=sw_ta, height=sh_ta)
    #textarea.grid(row=1, column=1, columnspan=4)
    textarea.config(font=('Courier', 12), wrap='none')

    sw_lb = int(screen_width * 0.00219619)
    sh_lb = int(screen_height * 0.04557291666)

    listbox = tk.Listbox(frame, width=sw_lb, height=sh_lb, yscrollcommand=scrollbar.set)
    listbox.grid(row=1, column=0)

    scrollbar.config(command=scrollbar_movimiento)
    textarea.bind('<Key>', sincronizar_medidor)

    tab_1 = ttk.Frame(window)
    tab_1.grid(row=0, column=0,rowspan=10)

    sw_cd = int(screen_width * 0.0805271)
    sh_cd = int(screen_height * 0.0390625)

    code_editor = CodeEditor(
        tab_1,
        width=70,
        height=sh_cd,
        language="frog",
        highlighter="dracula",
        autofocus=True,
        blockcursor=True,
        insertofftime=0,
        padx=10,
        pady=10,
    )

    code_editor.grid(row=0, column=1, columnspan=4,rowspan=3)

    sh_tb = int(screen_height * 0.0260416)
    # Crear el Treeview

    tabla = ttk.Treeview(window, height=sh_tb)

    # Agregar columnas a la tabla
    tabla['columns'] = ('N. Token', 'Tipo', 'Nombre', 'Valor', 'Parámetros','Retorno', 'Uso','N. Linea','Ámbito')

    # Definir las etiquetas de las columnas
    tabla.heading('#0', text='ID')
    tabla.heading('#1', text='N. Token')
    tabla.heading('#2', text='Tipo')
    tabla.heading('#3', text='Nombre')
    tabla.heading('#4', text='Valor')
    tabla.heading('#5', text='Parámetros')
    tabla.heading('#6', text='Retorno')
    tabla.heading('#7', text='Uso')
    tabla.heading('#8', text='N. Linea')
    tabla.heading('#9', text='Ámbito')

    # Configurar el tamaño de las columnas
    tabla.column('#0', width=40)
    tabla.column('#1', width=45)
    tabla.column('#2', width=70)
    tabla.column('#3', width=85)
    tabla.column('#4', width=85)
    tabla.column('#5', width=120)
    tabla.column('#6', width=70)
    tabla.column('#7', width=80)
    tabla.column('#8', width=50)
    tabla.column('#9', width=60)

    tabla.grid(row=1, column=1, padx=10, pady=10, columnspan=8)

    sw_sd = int(screen_width * 0.121523)
    sh_sd = int(screen_height * 0.01302833)

    # Ventana de output
    salidadat = ScrolledText(window, width=sw_sd, height=sh_sd, relief="solid")
    salidadat.grid(row=10, column=0, padx=10, pady=10, columnspan=15,rowspan=3)
    window.mainloop()
