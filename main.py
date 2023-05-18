import os
import random
import sys
import time


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.04)

def validar_numero(text):
    while True:
        try:
            delay_print(text)
            valor = int(input("\n=> "))
            if valor <1 or valor >20:
                 delay_print(f"\nPor favor solo ingrese números entre 1-20\n")
                 time.sleep(1)
                 os.system("clear")
                 continue
        except ValueError:
            delay_print(f"\nPor favor solo ingrese números entre 1-20\n")
            time.sleep(1)
            os.system("clear")
            continue
        return valor


delay_print("Saludos, vamos a jugar a las adivinanzas\nYo escogeré u numero entre 1-20 y tu deberás adivinar cual es")
random_number= random.randrange(1,20)

while True:
    numero = validar_numero("\nIngresa un numero entre 1-20")
    if numero < random_number:
        delay_print(f"El numero a adivinar es mayor a {numero}")
        time.sleep(1.5)
        os.system("clear")
    elif numero > random_number:
        delay_print(f"El numero a adivinar es menor a {numero}")
        time.sleep(1.5)
        os.system("clear")
    else:
        delay_print(f"Felicidades! acertaste, el numero era {numero}")
        time.sleep(1)
        break