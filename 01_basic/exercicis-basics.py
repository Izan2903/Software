###
# exercicis-basics.py
# Exercicis per practicar els conceptes apresos a les lliçons.
###

print("\nExercici 1: Imprimir missatges")
print("Escriu un programa que imprimeixi el teu nom i la teva ciutat en línies separades.")

nom = 'Izan'
ciutat = 'Hospitalet de Llobregat'

print(nom)
print(ciutat)

print("--------------")

print("\nExercici 2: Mostra els tipus de dades de les variables següents:")
print("Utilitza la comanda 'type()' per determinar el tipus de dades de cada variable.")
a = 15
b = 3.14159
c = "Hola món"
d = True
e = None

print("El tipus de a és:", type(a))
print("El tipus de b és:", type(b))
print("El tipus de c és:", type(c))
print("El tipus de d és:", type(d))
print("El tipus de e és:", type(e))

print("--------------")

print("\nExercici 3: Conversió de tipus")
print("Converteix la cadena \"12345\" a un enter i després a un float.")
print("Converteix el float 3.99 a un enter. Què passa?")

cadena = "12345"
print(f"Cadena a integer: {int(cadena)}")
print(f"Cadena a float: {float(cadena)}")

decimal = 3.99
decimal_a_enter = int(decimal)
print(f"Decimal original: {decimal}")
print(f"Decimal a enter (es treuria la part decimal): {decimal_a_enter}")



print("--------------")

print("\nExercici 4: Variables")
print("Crea variables per al teu nom, edat i alçada.")
print("Utilitza f-strings per imprimir una presentació.")

# "Hola! Em dic Marc, tinc 38 anys i faig 1.75 metres"
#name = "Marc"
#age = 38

nom = "Izan"
edat = 19
alçada = 1.71

print(f'"Hola! Em dic {nom}, tinc {edat} anys i faig {alçada} metres"')

print("--------------")

print("\nExercici 5: Nombres")
print("1. Utilitza el valor aproximat de PI (3.1416) sense desar-lo en una variable")
print("2. Arrodoneix el nombre amb round()")
print("3. Fes la divisió entera entre el nombre resultant i el nombre 2")
print("4. El resultat hauria de ser 1")

print("Valor aproximat de PI és:", 3.1416)
print("Valor arrodonit:", round(3.1416))
divisió = int(round(3.1416) / 2)
print(f"PI dividit entre 2 arrodonit és {divisió}")

print("--------------")

print("\nExercici 6: Conversor de temperatura")
print("Demana a l'usuari una temperatura en graus Celsius.")
print("Converteix aquest valor a Fahrenheit amb la fórmula: F = (C * 9/5) + 32")
print("Mostra els dos valors amb un missatge clar.")

celcius = float(input("Temperatura en ºC: "))
fahrenheit = (celcius * 9/5) + 32
print(f"{celcius}ºC es equivalent a {fahrenheit}F")

print("--------------")

print("\nExercici 7: Calculadora de propina")
print("Demana el total d'un compte i el percentatge de propina.")
print("Calcula quant és la propina i el total final que s'ha de pagar.")
print("Mostra els resultats amb 2 decimals.")

total_compte = float(input("Quin és el total del compte: "))
propina_percentatge = float(input("Quin és el percentatge de la propina? "))

propina = total_compte * (propina_percentatge / 100)
total_pagar = total_compte + propina

print(f"Propina: {propina:.2f}€")
print(f"Total a pagar: {total_pagar:.2f}€")

print("--------------")

print("\nExercici 8: Validador de contrasenya simple")
print("Demana una contrasenya a l'usuari.")
print("Comprova si té almenys 8 caràcters.")
print("Mostra 'Contrasenya vàlida' o 'Contrasenya no vàlida'.")

contrasenya = input("Genera una contrasenya: ")

if len(contrasenya) >= 8:
    print("Contrasenya vàlida")
else:
    print("Contrasenya no vàlida")