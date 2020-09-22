import json
import os

# Aca voy a guardar la relacion idCom - idMinorista
idcom_idmin = {}
# Abro el archivo de minoristas
with open('minorista.json') as minoristaJSON:
    minoristas = json.load(minoristaJSON)
    # Recorro cada minorista
    for minorista in minoristas:
        dom_id=[]
        dom_codpanel=[]
        minorista_id = minorista["id"]
        minorista_domid = minorista["domIdCom"]
        domid_len = int(len(minorista_domid)/4)
        i = 1
        # Recorro los Dominios de este minorista
        while i <= domid_len:
            # Recorro los Dominios de Cod Panel de este minorista
            idcom_idmin[minorista_domid[i*4-3:i*4-1]]=minorista_id
            i += 1

cuentas_error = open('cuentas_sin_minorista.txt','w')
cuentas_ok = open('cuentas_ok.txt','w')

# Abro archivo de cuentas
with open('cuenta.json') as cuentasJSON:
    cuentas = json.load(cuentasJSON)
    i,j,k=0,0,0
    for comunicador in cuentas:
        i+=1
        try:
            cuentas_ok.write(str(idcom_idmin[comunicador["idComunicador"][:2]])+','+comunicador["idComunicador"]+'\n')
            j+=1
        except:
            cuentas_error.write(str(comunicador["idComunicador"])+'\n')
            k+=1
# Cierro los archivos de log
cuentas_ok.close()
cuentas_error.close()

# Abro archivo de cuentas modificarlo y escribir el nuevo
with open('cuenta.json') as cuentasJSON:
    cuentas = json.load(cuentasJSON)
    for comunicador in cuentas:
        #cuentas_ok = open('cuentas_ok.txt', 'r')
        #for line in cuentas_ok:
        #    if comunicador["idComunicador"] in line:
        #        comunicador["idMinorista"] = int(line.split(',')[0])
        #cuentas_ok.seek(0)
        try:
            comunicador["idMinorista"] = int(idcom_idmin[comunicador["idComunicador"][:2]])
        except:
            print("Error: " + str(comunicador["idComunicador"]))

# Escribo el nuevo archivo de cuentas
with open("cuentaNuevo.json", "w") as jsonFile:
    json.dump(cuentas, jsonFile)

print('Total de cuentas: ' + str(i))
print('Cuentas asignadas a un minorista: ' + str(j))
print('Cuentas sin un minorista: ' + str(k))

os.system("pause")
