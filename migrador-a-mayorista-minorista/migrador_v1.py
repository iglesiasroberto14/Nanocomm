import json
import time
from pprint import pprint
#######
# TODO
# RECEPTORA Y LINEA
########

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
        minorista_domcodpanel = minorista["domCodPanel"]
        minorista_receptor = minorista["receptorTel"]
        minorista_linea = minorista["lineaTel"]
        # Obtengo la cantidad de Dominios de ID Comunicador
        domid_len = int(len(minorista_domid)/4)
        # Obtengo la cantidad de Dominios de codigo de panel
        domcodpanel_len = int(len(minorista_domcodpanel)/4)
        i = 1
        # Recorro los Dominios de este minorista
        while i <= domid_len:
            j = 1
            # Recorro los Dominios de Cod Panel de este minorista
            while j <= domcodpanel_len:
                concat=minorista_domid[i*4-3:i*4-1]+minorista_domcodpanel[j*4-3:j*4-1]+minorista_receptor+minorista_linea
                idcom_idmin[concat]=minorista_id
                j += 1
            i += 1

        idcom_idmin[minorista_id]=[dom_id,dom_codpanel]

cuentas_error = open('cuentas_sin_minorista.txt','w')
cuentas_ok = open('cuentas_ok.txt','w')

# Abro archivo de cuentas
with open('cuenta.json') as cuentasJSON:
    cuentas = json.load(cuentasJSON)
    i,j,k=0,0,0
    for comunicador in cuentas:
        i+=1
        try:
            cuentas_ok.write(str(idcom_idmin[comunicador["idComunicador"][:2]+comunicador["codPanel"][:2]+comunicador["receptorTel"]+comunicador["lineaTel"]])+','+comunicador["idComunicador"]+'\n')
            j+=1
        except:
            print('No existe la combinacion de dominios, receptora y linea: "' + comunicador["idComunicador"][:2] + comunicador["codPanel"][:2] + comunicador["receptorTel"] + comunicador["lineaTel"] +'". ID Comunicador: ' + comunicador["idComunicador"] + ', Codigo de Panel: ' + comunicador["codPanel"][:2])
            cuentas_error.write(str(comunicador["idComunicador"][:2]+comunicador["codPanel"][:2])+'\n')
            k+=1
print('Total de cuentas: ' + str(i))
print('Cuentas asignadas a un minorista: ' + str(j))
print('Cuentas sin un mayorista: ' + str(k))

cuentas_ok.close()
cuentas_error.close()

# Abro archivo de cuentas
with open('cuenta.json') as cuentasJSON:
    cuentas = json.load(cuentasJSON)
    for comunicador in cuentas:
        cuentas_ok = open('cuentas_ok.txt', 'r')
        for line in cuentas_ok:
            if comunicador["idComunicador"] in line:
                comunicador["idMinorista"] = int(line.split(',')[0])
        cuentas_ok.seek(0)

cuentas_ok.close()

with open("cuentaNuevo.json", "w") as jsonFile:
    json.dump(cuentas, jsonFile)
            
