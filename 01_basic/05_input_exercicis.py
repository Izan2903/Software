###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

print("Exercici 1")
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
# Després, mostra un missatge amb aquesta informació.
nom_tècnic, nom_xarxa = input("Nom del tècnic i la xarxa: ").split()

print(f"{nom_tècnic} està instal·lant la xarxa {nom_xarxa}", end = "\n\n")

print("Exercici 2")
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud_km = float(input("Inserta el valor de la longitud (km): "))
velocitat_gbps = float(input("Inserta el valor de la velocitat de transmissió (Gbps): "))
temps = 8 / velocitat_gbps
print(f"L'enllaç de {longitud_km} km necessitaria {temps} segons per transmetre 1 GB ", end = "\n\n")
print("Exercici 3")
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores_feina = int(input("Inserta el nombre d'hores de feina: "))
preu_instalació = float(input("Inserta el preu per hora de la instalació de la xarxa: "))
preu_material = float(input("Insert el preu del material: "))
preu_total = hores_feina * preu_instalació + preu_material

print(f"El preu total son {preu_total}€")