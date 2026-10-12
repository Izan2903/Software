###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

print("Exercici 1")
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom_encaminador = "Router oficina"
ubicació_encaminador = "Planta Baixa"
número_de_ports_encaminador = 8
encaminador_encés = True

print(f"Encaminador: {nom_encaminador}\nUbicació: {ubicació_encaminador}\n"
      f"Nombre de ports: {número_de_ports_encaminador}\nEncés: {encaminador_encés}", end = "\n\n")

print("Exercici 2")
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
gb_inclosos = 20
gb_consumits = 12.5
gb_restants = gb_inclosos - gb_consumits

print(f"GB restants: {gb_restants} GB")

gb_consumits = 18
gb_restants = gb_inclosos - gb_consumits

print(f"GB restants: {gb_restants} GB")