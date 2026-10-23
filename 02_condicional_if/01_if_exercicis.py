###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble

nivell_senyal = float(input("Introduiex el nivel de senyal rebut (RSSI) en dBm: "))

if nivell_senyal >= -50:
    print("Cobertura excel·lent")
elif nivell_senyal >= -67:
    print("Cobertura bona")
elif nivell_senyal >= -75:
    print("Cobertura feble")
else:
    print("Cobertura molt feble")

# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.

potencia_optica = float(input("Introdueix la potència òptica en dBm: "))

if potencia_optica >= -27 and potencia_optica <= -8:
    print("Potència òptica aceptable")
elif potencia_optica < -27:
    print("Potència òptica massa baixa")
else:
    print("Potència òptica massa alta")

# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.

consum_dades = float(input("Introdueix el consum de dades en GB: "))

pla = 20

if consum_dades <= pla:
    print("Està dins del límit")
else:
    gb_adicionals = consum_dades - pla

    print(f"Ha superat el límit, ha consumit {gb_adicionals}GB adicionals")

# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.

terminal_ences = int(input("L'indicador està encés o apagat (0 o 1): "))

if terminal_ences:
    print("Està encés")
else:
    print("Està apagat")

# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.

percentatge = float(input("Introdueix el percentatge de bateria disponible: "))

if percentatge >= 0 and percentatge < 20:
    print("Nivell crític")
elif percentatge >= 20 and percentatge < 50:
    print("Nivell baix")
elif percentatge >= 50 and percentatge <= 100:
    print("Nivell suficient")
else:
    print("Error! Percentatge de bateria incorrecte")

# Exercici 6: Qualitat d'una connexió de xarxa
# Demana la latència en mil·lisegons i el percentatge de paquets perduts.
# Rebutja una latència negativa o una pèrdua fora del rang del 0 % al 100 %.
# Classifica la connexió com a excel·lent si la latència és de 30 ms o menys
# i la pèrdua és de l'1 % o menys; bona si és de 80 ms o menys i la pèrdua és
# del 3 % o menys; acceptable si és de 150 ms o menys i la pèrdua és del 5 %
# o menys; en qualsevol altre cas, deficient.

latencia = float(input("Introdueix la latència en mil·lisegons: "))
percentatge = float(input("Introdueix el percentatge de paquets perduts: "))

if percentatge >= 0 and percentatge <= 100:
    if latencia <= 30 and percentatge <= 1:
        print("Connexió excel·lent")
    elif latencia <= 80 and percentatge <= 3:
        print("Connexió bona")
    elif latencia <= 150 and percentatge <= 5:
        print("Connexió acceptable")
    else:
        print("Connexió deficient")
else:
    print("Latencia rebutjada")

# Exercici 7: Cost mensual d'un pla de dades
# Demana el tipus de pla (bàsic o plus) i el consum mensual en GB.
# El pla bàsic costa 10 € i inclou 10 GB; cada GB addicional costa 1,50 €.
# El pla plus costa 20 € i inclou 30 GB; cada GB addicional costa 0,75 €.
# Rebutja un consum negatiu o un tipus de pla desconegut. Calcula i mostra el
# cost total, tenint en compte que no es cobra l'excés si no se supera el límit.



# Exercici 8: Accés a un compte de client
# Demana si el compte està actiu, si la contrasenya és correcta i si el codi
# de doble verificació és correcte. Demana el codi només si el compte és actiu
# i la contrasenya és correcta. Indica si l'accés es denega perquè el compte
# està desactivat, perquè la contrasenya és incorrecta o perquè falla el codi;
# si totes les comprovacions necessàries són correctes, permet l'accés.



# Exercici 9: Diagnòstic d'un router
# Demana si el router està encès, si l'indicador LOS del terminal òptic està
# encès i si l'indicador d'Internet del router està encès. Indica primer si
# cal encendre el router; si ja està encès, comprova si cal revisar el cable
# de fibra (LOS encès), si cal contactar amb el proveïdor (Internet apagat) o
# si la connexió funciona correctament. Considera els casos en aquest ordre.



# Exercici 10: Prioritat d'una incidència de xarxa
# Demana si la incidència afecta un servei crític, el nombre d'usuaris afectats
# i si hi ha una alternativa de connexió disponible. Rebutja un nombre negatiu
# d'usuaris. Assigna prioritat crítica si afecta un servei crític i no hi ha
# alternativa, o si afecta almenys 50 usuaris i no hi ha alternativa; alta si
# afecta almenys 10 usuaris o un servei crític; en qualsevol altre cas, baixa.

