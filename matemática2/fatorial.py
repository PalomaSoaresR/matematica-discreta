def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

numero = int(input("\nDigite um número inteiro positivo: "))
resultado = calcular_fatorial(numero)
print(f"\nO fatorial de {numero} é {resultado}")
print("\n")