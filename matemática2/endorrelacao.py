def verificar_relacao(pares):
    simetrico = True
    antissimetrico = True
    reflexivo = True
    irreflexivo = True
    transitivo = True

    for par in pares:
        x, y = par

        #Simetria
        if (y, x) not in pares:
            simetrico = False

        #Antissimetria
        if x != y and (y, x) in pares:
            antissimetrico = False

        #Reflexivo
        if (x, x) not in pares:
            reflexivo = False

        #Irreflexivo
        if (x, x) in pares:
            irreflexivo = False

    #Transitividade
    for par1 in pares:
        x, y = par1
        for par2 in pares:
            if y == par2[0] and (x, par2[1]) not in pares:
                transitivo = False

    return simetrico, antissimetrico, reflexivo, irreflexivo, transitivo

quantia_pares = int(input("\nDigite a quantia de pares ordenados: "))
pares_ordenados = []
for i in range(quantia_pares):
    print('\n')
    x = int(input(f"Digite o valor de x para o {i+1}º termo: "))
    y = int(input(f"Digite o valor de y para o {i+1}º termo: "))
    pares_ordenados.append((x, y))

resultado = verificar_relacao(pares_ordenados)
print('\n')
print("Simétrico:", "sim" if resultado[0] else "não")
print("Antissimétrico:", "sim" if resultado[1] else "não")
print("Reflexivo:", "sim" if resultado[2] else "não")
print("Irreflexivo:", "sim" if resultado[3] else "não")
print("Transitivo:", "sim" if resultado[4] else "não")
print('\n')