#you need to match queue_log unique ID with filename unique ID
from io import open
import os, re

with open('/path/to/queue/logs','r') as q:
    lines = q.readlines()

#Regular Expresion to fin ID on logs

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

#Working on .WAV(monitor) folder path

directorio = os.listdir("/path/to/audio/files")

sin_extension = []

for d in directorio:
    str(sin_extension.append(os.path.splitext(d)[0]))

#Finding the agent name

id_usuario = []
nombre_de_usuario = []
 
pattern_id_usuario = r"\d{10}\.\d{5}"
pattern_nombre_de_usuario = r'[A-Z]\D\D\D*[A-Z][a-z]*'

for z in re.finditer(pattern_id_usuario,str(id_queue)):
    id_usuario.append(z.group())

for y in re.finditer(pattern_nombre_de_usuario,str(id_queue)):
    nombre_de_usuario.append(y.group())

#Tuple for &(find match between two data sources, logs and filenames

a = tuple(id_usuario)
b = tuple(nombre_de_usuario)

#we need a dictionary like: 1234567890.12345:Agent1

dict_id_nombre = dict(zip(a,b))
nombres_de_archivo = []
wav = ".wav"

#Find match

id_log_cruce = dict_id_nombre.keys()
id_nombre_cruce = id_usuario
common = set(id_log_cruce) & set(id_nombre_cruce)

for x in list(common):
            for v in sin_extension:            
                if x in v:
                    #This defines the filename, you cant choose what you need
                    nombres_de_archivo.append(v[0:33]+str(dict_id_nombre[x]).replace(" ","")+wav)    

for k in directorio:
    for l in nombres_de_archivo:
        if l[0:32] == k[0:32]:
            os.chdir("/path/to/audio/files")
            os.rename(k,l)
### END ###
###diego@linuxeria.cl###
