
import os
import sys

from fillpdf import fillpdfs
from datos import *

data_dict_anexo_1 = {
'Grupo': nombre_ciclo,
'Grupo_2': grupo,
'Curso académico': curso,
'Año escolar': anio,
#'NO': nombre_modulo,
'En': lugar_firma,
'Text1': dia_firma,
'de': mes_firma,
'de_2':anio_firma
}

data_dict_anexo_2 = {
'Ciclo formativo o Curso de especialización':nombre_ciclo,
'Grupo_3': grupo,
'Curso académico_2': curso,
'Año escolar_2': anio,
'EL EQUIPO DOCENTE EN SESIÓN DE EVALUACIÓN DE FECHA': fecha_reunion,
'En_2': lugar_firma,
'Text2': dia_firma,
'de_3':mes_firma,
'de_4':anio_firma
}

BASE_DIR="anexos"



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


def crea_lista_modulos(texto_modulos):    
    lista_modulos=[]

    for linea in texto_modulos.split("\n"):
        flinea=linea.split(",")
        if len(flinea)>1:
            mod=(flinea[0],flinea[1])
            lista_modulos.append(mod)

    return lista_modulos




def anexos_a1_de_modulo(data_dict_anexo_1, codigo_ciclo, codigo_modulo, nombre_modulo,fichero_nombres):

    directorio=f"{BASE_DIR}/anexos_a1_{codigo_modulo}"
    os.makedirs(directorio, exist_ok = True)
    with open(fichero_nombres, encoding="utf-8") as f:
        for linea in f:
            if ((len(linea.strip())==0) or (linea.strip()[0]=="#")):
                continue
            linea=linea.replace("\n","").replace("\t"," ")
            campos=linea.split(",")
            if len(campos)==1:
                nombre=campos[0].strip(" ")
                apellidos=""
            else:
                nombre=campos[0].strip(" ")
                apellidos=campos[1].strip(" ")
            if len(nombre)>0:
                print ("Genero anexo I para "+nombre+" "+apellidos)
                data_dict_anexo_1['Alumnoa']=nombre+" "+apellidos
                prefijo="{0}_{1}_".format(apellidos.replace(" ","_"), nombre.replace(" ","_"))
                subfijo="{0}_{1}_ANEXOI.pdf".format(codigo_ciclo,codigo_modulo)
                data_dict_anexo_1["NO"]=nombre_modulo
                genera_anexo(directorio, prefijo,"plantilla-anexito-1.pdf",data_dict_anexo_1,subfijo)
    



def anexos_a2_de_modulo(data_dict_anexo_2, codigo_ciclo, fichero_nombres):

    directorio=f"{BASE_DIR}/anexos_a2_{codigo_ciclo}"
    os.makedirs(directorio, exist_ok = True)
    with open(fichero_nombres, encoding="utf-8") as f:
        for linea in f:
            if ((len(linea.strip())==0) or (linea.strip()[0]=="#")):
                continue
            linea=linea.replace("\n","").replace("\t"," ")
            campos=linea.split(",")
            if len(campos)==1:
                nombre=campos[0].strip(" ")
                apellidos=""
            else:
                nombre=campos[0].strip(" ")
                apellidos=campos[1].strip(" ")
            if len(nombre)>0:
                print ("Genero anexo II para "+nombre+" "+apellidos)
                data_dict_anexo_2['Alumnoa_2']=nombre+" "+apellidos
                prefijo="{0}_{1}_".format(apellidos.replace(" ","_"), nombre.replace(" ","_"))
                subfijo="{0}_ANEXOII.pdf".format(codigo_ciclo)
                genera_anexo(directorio, prefijo,"plantilla-anexito-2.pdf",data_dict_anexo_2,subfijo)



