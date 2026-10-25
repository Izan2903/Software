###
# EXERCICIS (while)
###

print("\nExercici 1: Compte enrere")
# Imprimeix els números del 10 a l'1 fent servir un bucle while.

num = 10

while num > 0:
    print(f"{num}")
    num -= 1

print("\nExercici 2: Suma de números parells (while)")
# Calcula la suma dels números parells entre 1 i 20 (inclosos) fent servir un bucle while.

num = 1
suma = 0

while num <= 20:
    if num % 2 == 0:
        suma += num
    num += 1

else:
    print(f"La suma dels numeros parells ha sigut {suma}")

print("\nExercici 3: Factorial d'un número")
# Demana a l'usuari que introdueixi un número enter positiu.
# Calcula el seu factorial fent servir un bucle while.
# El factorial d'un número enter positiu és el producte de tots els números de l'1 fins a aquest número. Per exemple, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.

num = int(input("Introdueix un número enter positiu: "))
factorial = 1
num1 = num
while num >= 1:
    factorial = num * factorial
    num -= 1
else:
    print(f"{num1}! = {factorial}")

print("\nExercici 4: Validació de contrasenya")
# Demana a l'usuari que introdueixi una contrasenya.
# La contrasenya ha de tenir almenys 8 caràcters.
# Fes servir un bucle while per continuar demanant la contrasenya fins que compleixi els requisits.
# Si la contrasenya és vàlida, imprimeix "Contrasenya vàlida".

contrasenya = input("Introdueix una contrasenya (almenys 8 caràcters): ")

while len(contrasenya) < 8:
    print("La contrasenya ha de tenir minim 8 caràcters.")
    contrasenya = input("Introdueix una altre contrasenya: ")


print("\nExercici 5: Taula de multiplicar")
# Demana a l'usuari que introdueixi un número.
# Imprimeix la taula de multiplicar d'aquest número (de l'1 al 10) fent servir un bucle while.

num = int(input("Introdueix un número: "))
multiplicacio = 1

while multiplicacio <= 10:
    resultat = num * multiplicacio
    print(f"{num} x {multiplicacio} = {resultat}")
    multiplicacio += 1

print("\nExercici 6: Números primers fins a N")
# Demana a l'usuari que introdueixi un número enter positiu N.
# Imprimeix tots els números primers menors o iguals que N fent servir un bucle while.
# Un número és primer si només és divisible per 1 i per ell mateix.

num = int(input("Introdueix un número enter positiu N: "))

while num >= 2:
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            break
        divisor += 1
    else:
        print(num)

    num -= 1

print("\nExercici 7: Suma fins al zero")
# Demana a l'usuari que introdueixi números enters.
# Ves sumant els números introduïts fins que l'usuari introdueixi el 0.
# Al final, imprimeix la suma total. El 0 només serveix per acabar i no s'ha de sumar.



print("\nExercici 8: Comptar les xifres d'un número")
# Demana a l'usuari que introdueixi un número enter positiu.
# Comptabilitza quantes xifres té fent servir un bucle while.
# Finalment, imprimeix el nombre de xifres.



print("\nExercici 9: Seqüència de Fibonacci")
# Demana a l'usuari quants termes de la seqüència de Fibonacci vol veure.
# Imprimeix aquest nombre de termes fent servir un bucle while.
# La seqüència comença per 0 i 1; cada terme següent és la suma dels dos anteriors.



print("\nExercici 10: Joc d'endevinar el número")
# El número secret és el 7.
# Demana a l'usuari que provi d'endevinar-lo i continua demanant números amb un bucle while
# fins que l'encerti.
# Després de cada intent incorrecte, indica si el número secret és més gran o més petit.

