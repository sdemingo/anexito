
import sys
import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from fillpdf import fillpdfs

from datos import *
from app import *


VERSION="1.2"

#BASE_DIR="anexos"

modulos_ejemplo="""

0369, Un ejemplo de asignatura
0202, Otro ejemplo de asignatura

"""


entradas={}

root = tk.Tk()
fichero_var = tk.StringVar()
radio_var = tk.StringVar(value="anexo 1")
global text_area



def seleccionar_fichero():
    ruta = filedialog.askopenfilename()
    if ruta:
        fichero_var.set(ruta)

def generar():

    global text_area

    if (fichero_var.get() == ""):
        messagebox.showerror("Error", "Falta fichero de nombres")
        return

    datos_a1={}
    datos_a1["Grupo"]=entradas["nombre_ciclo"].get()
    datos_a1["Grupo_2"]=entradas["grupo"].get()
    datos_a1["Curso académico"]=entradas["curso"].get()
    datos_a1["Año escolar"]=entradas["año"].get()
    datos_a1["En"]=entradas["lugar"].get()
    datos_a1["Text1"]=entradas["dia"].get()
    datos_a1["de"]=entradas["mes"].get()
    datos_a1["de_2"]=entradas["año"].get()

    datos_a2={}
    datos_a2["Ciclo formativo o Curso de especialización"] = entradas["nombre_ciclo"].get()
    datos_a2["Grupo_3"] = entradas["grupo"].get()
    datos_a2["Curso académico_2"] = entradas["curso"].get()
    datos_a2["Año escolar_2"] = entradas["año"].get()
    datos_a2["EL EQUIPO DOCENTE EN SESIÓN DE EVALUACIÓN DE FECHA"] = entradas["fecha"].get()
    datos_a2["En_2"] = entradas["lugar"].get()
    datos_a2["Text2"] = entradas["dia"].get()
    datos_a2["de_3"] = entradas["mes"].get()
    datos_a2["de_4"] = entradas["año"].get()
    
    
    lista_modulos=crea_lista_modulos(text_area.get("1.0",tk.END))
    codigo_ciclo = entradas["código_ciclo"].get()

    for m in lista_modulos:            
        nombre_modulo=m[1]
        codigo_modulo=m[0]
        nombres=fichero_var.get()

        if (radio_var.get() == "anexo 1"):
            anexos_a1_de_modulo(datos_a1, codigo_ciclo, codigo_modulo, nombre_modulo, nombres)

        if (radio_var.get() == "anexo 2"):
            anexos_a2_de_modulo(datos_a2, codigo_ciclo, nombres)

    messagebox.showinfo("Listo", f"Generados generados")

def salir():
    root.destroy()



# ---------- CAMPOS DE TEXTO ----------
etiquetas =[
"Código ciclo",
"Nombre ciclo",
"Grupo",
"Curso",
"Año",
"Fecha",
"Lugar",
"Dia",
"Mes",
#"Año"
]



def main_gui():

    root.title(f"~ Anexito {VERSION} ~")


    for i in range(len(etiquetas)):
        label = tk.Label(root, text=etiquetas[i])
        label.grid(row=i, column=0, padx=5, pady=3, sticky="e")

        entry = tk.Entry(root, width=75)
        entry.grid(row=i, column=1, padx=5, pady=3)   
        entradas[etiquetas[i].replace(" ","_").lower()]=entry

    
    entradas["código_ciclo"].insert(0,"210")
    entradas["nombre_ciclo"].insert(0,"Nombre del ciclo")
    entradas["grupo"].insert(0,"Grupo")
    entradas["curso"].insert(0,"2024/2025")
    entradas["año"].insert(0,"2025")
    entradas["fecha"].insert(0,"00/00/00")
    entradas["lugar"].insert(0,"Fuenlabrada")
    entradas["dia"].insert(0,"8")
    entradas["mes"].insert(0,"Febrero")



    # ---------- ÁREA DE TEXTO ----------
    area_label = tk.Label(root, text="Módulos")
    area_label.grid(row=10, column=0, padx=5, pady=5, sticky="ne")

    global text_area

    text_area = tk.Text(root, width=75, height=10)
    text_area = tk.Text(root, width=75, height=10)
    text_area.grid(row=10, column=1, padx=5, pady=5)

    text_area.insert(1.0,modulos_ejemplo)


    # ---------- RADIOBUTTONS ----------
    radio1 = tk.Radiobutton(root, text="anexo 1", variable=radio_var, value="anexo 1")
    radio2 = tk.Radiobutton(root, text="anexo 2", variable=radio_var, value="anexo 2")

    radio1.grid(row=11, column=1, sticky="w", pady=2)
    radio2.grid(row=12, column=1, sticky="w", pady=2)


    # ---------- SELECTOR DE FICHERO ----------

    label_fichero = tk.Label(root, text="Alumnos:")
    label_fichero.grid(row=13, column=0, padx=5, pady=5, sticky="e")

    entry_fichero = tk.Entry(root, textvariable=fichero_var, width=75)
    entry_fichero.grid(row=13, column=1, padx=5, pady=5, sticky="w")

    btn_fichero = tk.Button(root, text="Seleccionar...", command=seleccionar_fichero)
    btn_fichero.grid(row=13, column=2, padx=5, pady=5)



    # ---------- BOTONES INFERIORES ----------
    btn_salir = tk.Button(root, text="❌ Salir", width=15, command=salir)
    btn_generar = tk.Button(root, text="✔️  Generar", width=15, command=generar)

    btn_salir.grid(row=14, column=1, sticky="w", padx=5, pady=10)
    btn_generar.grid(row=14, column=1, sticky="e", padx=5, pady=10)


    root.mainloop()



if __name__=='__main__':
    main_gui()
