def fahrenheit_a_celsius(f):
    return (f - 32) / 1.8

f = float(input("Ingresa los grados Fahrenheit: "))
c = fahrenheit_a_celsius(f)
print(f"Los {f} grados Fahrenheit son {c} grados celsius")
input("Presione una tecla para finalizar....")
