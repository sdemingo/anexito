
import sys
import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from fillpdf import fillpdfs

from datos import *


BASE_DIR="anexos"

modulos_ejemplo="""

0369, Un ejemplo de asignatura
0202, Otro ejemplo de asignatura

"""


def ruta_recurso(path_relativo):
    # Esta función permite encontrar las plantillas
    # incluso si las hemos añadido al empaquetado EXE con
    # pyinstaller

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, path_relativo)
    return path_relativo


def limpia_nombre(nombre):
    return nombre.replace("á","a").replace("é","e").replace("í","i").replace("ó","o").replace("ú","u").replace("ñ","n").replace(" ","_")


def genera_anexo(directorio, nombre,plantilla,campos,suffix):
    plantilla_pdf = ruta_recurso(plantilla)
    fichero=limpia_nombre(nombre)+suffix
    fillpdfs.write_fillable_pdf(plantilla_pdf, f"{directorio}/{fichero}", campos)


def crea_lista_modulos():    
    lista_modulos=[]
    for linea in modulos.split("\n"):
        flinea=linea.split(",")
        if len(flinea)>1:
            mod=(flinea[0],flinea[1])
            lista_modulos.append(mod)

    return lista_modulos




def anexos_a1_de_modulo(data_dict_anexo_1, codigo_modulo, nombre_modulo,fichero_nombres):

    directorio=f"{BASE_DIR}/anexos_a1_{codigo_modulo}"
    os.makedirs(directorio, exist_ok = True)
    with open(fichero_nombres, encoding="utf-8") as f:
        for linea in f:
            if ((len(linea.strip())==0) or (linea.strip()[0]=="#")):
                continue
            linea=linea.replace("\n","").replace("\t"," ")
            campos=linea.split(",")
            if len(campos)==1:
                nombre=campos[0]
                apellidos=""
            else:
                nombre=campos[0]
                apellidos=campos[1]
            if len(nombre)>0:
                print ("Genero anexo I para "+nombre+" "+apellidos)
                data_dict_anexo_1['Alumnoa']=nombre+" "+apellidos
                prefijo="{0}_{1}_".format(apellidos.replace(" ","_"), nombre.replace(" ","_"))
                subfijo="{0}_{1}_ANEXOI.pdf".format(codigo_ciclo,codigo_modulo)
                data_dict_anexo_1["NO"]=nombre_modulo
                genera_anexo(directorio, prefijo,"plantilla-anexito-1.pdf",data_dict_anexo_1,subfijo)
    



def anexos_a2_de_modulo(codigo_modulo, nombre_modulo,fichero_nombres):

    directorio=f"{BASE_DIR}/anexos_a2_{codigo_modulo}"
    os.makedirs(directorio, exist_ok = True)
    with open(fichero_nombres, encoding="utf-8") as f:
        for linea in f:
            if ((len(linea.strip())==0) or (linea.strip()[0]=="#")):
                continue
            linea=linea.replace("\n","").replace("\t"," ")
            campos=linea.split(",")
            if len(campos)==1:
                nombre=campos[0]
                apellidos=""
            else:
                nombre=campos[0]
                apellidos=campos[1]
            if len(nombre)>0:
                print ("Genero anexo II para "+nombre+" "+apellidos)
                data_dict_anexo_2['Alumnoa_2']=nombre+" "+apellidos
                prefijo="{0}_{1}_".format(apellidos.replace(" ","_"), nombre.replace(" ","_"))
                subfijo="{0}_{1}_ANEXOII.pdf".format(codigo_ciclo,codigo_modulo)
                genera_anexo(directorio, prefijo,"plantilla-anexito-2.pdf",data_dict_anexo_2,subfijo)




entradas={}

root = tk.Tk()
fichero_var = tk.StringVar()

def seleccionar_fichero():
    ruta = filedialog.askopenfilename()
    if ruta:
        fichero_var.set(ruta)

def generar():

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
    
    lista_modulos=crea_lista_modulos()
    

    for m in lista_modulos:
        nombre_modulo=m[1]
        codigo_modulo=m[0]
        nombres=fichero_var.get()

        # Por ahora solo genero anexos 1
        anexos_a1_de_modulo(datos_a1, codigo_modulo, nombre_modulo, nombres)

        # if (sys.argv[1] == "-a1"):
        #     anexos_a1_de_modulo(codigo_modulo, nombre_modulo, sys.argv[2])
        # if (sys.argv[1] == "-a2"):
        #     anexos_a2_de_modulo(codigo_modulo, nombre_modulo, sys.argv[2])

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

    root.title("~ Anexito ~")


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

    text_area = tk.Text(root, width=75, height=10)
    text_area.grid(row=10, column=1, padx=5, pady=5)

    text_area.insert(1.0,modulos_ejemplo)


    # ---------- RADIOBUTTONS ----------
    radio_var = tk.StringVar(value="anexo 1")

    radio1 = tk.Radiobutton(root, text="anexo 1", variable=radio_var, value="anexo 1")
    radio2 = tk.Radiobutton(root, text="anexo 2", variable=radio_var, value="anexo 2")

    radio1.grid(row=11, column=1, sticky="w", pady=2)
    radio2.grid(row=12, column=1, sticky="w", pady=2)
    radio2.config(state="disabled") # Por ahora deshabilito la opción del anexo II


    # ---------- SELECTOR DE FICHERO ----------

    label_fichero = tk.Label(root, text="Fichero:")
    label_fichero.grid(row=13, column=0, padx=5, pady=5, sticky="e")

    entry_fichero = tk.Entry(root, textvariable=fichero_var, width=75)
    entry_fichero.grid(row=13, column=1, padx=5, pady=5, sticky="w")

    btn_fichero = tk.Button(root, text="Seleccionar...", command=seleccionar_fichero)
    btn_fichero.grid(row=13, column=2, padx=5, pady=5)



    # ---------- BOTONES INFERIORES ----------
    btn_generar = tk.Button(root, text="Generar", width=15, command=generar)
    btn_salir = tk.Button(root, text="Salir", width=15, command=salir)

    btn_generar.grid(row=14, column=1, sticky="w", padx=5, pady=10)
    btn_salir.grid(row=14, column=1, sticky="e", padx=5, pady=10)


    root.mainloop()



if __name__=='__main__':
    main_gui()
