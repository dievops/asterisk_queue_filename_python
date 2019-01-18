#Objetivo: Cambiar ""5000" de nombre de archivo "q-5000", por número de extensión "2XX" leyendo
#el archivo queue_log de asterisk con el formato '1546866620|NONE|5000|Carla Ochoa|UNPAUSE|\n'
from io import open
import os, re

#Abrir archivo queue_log y guardar una lista

with open('/home/diego/Documentos/metadata-anewlytics/queue_log_500','r') as q:
    lines = q.readlines()

#Expresión regular que busca COMPLETEAGENT
pattern = r'\d{10}\.\d{5}\|5000\|.*?\|'
id_queue = []

ca = "COMPLETEAGENT"
cb = "TRANSFER"
cc = "COMPLETECALLER"
cd = "ABANDON"
ce = "RINGNOANSWER"

for id in lines:
    if ca in id:
        id_queue.append(re.findall(pattern,id))  
    if cb in id:
        id_queue.append(re.findall(pattern,id))
    if cc in id:
        id_queue.append(re.findall(pattern,id))
    if cd in id:
        id_queue.append(re.findall(pattern,id))
    if ce in id:
        id_queue.append(re.findall(pattern,id))

#Removemos extensión de nombres de archivo y los agregamos a una lista

directorio = os.listdir("/home/diego/Documentos/metadata-anewlytics/entrantes")

sin_extension = []

for d in directorio:
    str(sin_extension.append(os.path.splitext(d)[0]))

#Utilizamos expresiones regulares para encontrar los datos

id_usuario = []
nombre_de_usuario = []
 
pattern_id_usuario = r"\d{10}\.\d{5}"
pattern_nombre_de_usuario = r'[A-Z]\D\D\D*[A-Z][a-z]*'

for z in re.finditer(pattern_id_usuario,str(id_queue)):
    id_usuario.append(z.group())

for y in re.finditer(pattern_nombre_de_usuario,str(id_queue)):
    nombre_de_usuario.append(y.group())

#Creamos 2 tuplas para transformarlas en diccionario

a = tuple(id_usuario)
b = tuple(nombre_de_usuario)

#Diccionario a partir de tupla a y b

dict_id_nombre = dict(zip(a,b))
nombres_de_archivo = []
wav = ".wav"

#Cruce de datos set(lista1) & set(lista2)

id_log_cruce = dict_id_nombre.keys()
id_nombre_cruce = id_usuario
common = set(id_log_cruce) & set(id_nombre_cruce)

for x in list(common):
            for v in sin_extension:            
                if x in v:
                    nombres_de_archivo.append(v[0:33]+str(dict_id_nombre[x]).replace(" ","")+wav)    

for k in directorio:
    for l in nombres_de_archivo:
        if l[0:32] == k[0:32]:
            os.chdir("/home/diego/Documentos/metadata-anewlytics/entrantes")
            os.rename(k,l)
### Fin ###

