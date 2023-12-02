
def fecho_transitivo(pares):
    fecho = set(pares)
    while True:
        novo_fecho = set(fecho)
        for a, b in fecho:
            for c, d in fecho:
                if b == c:
                    novo_fecho.add((a, d))
        if novo_fecho == fecho:
            break
        fecho = novo_fecho
    return fecho

pares = []
print('\n')
while True:
    par = input("Digite um par ordenado (0 para sair): ")
    if par.lower() == "0":
        break
    pares.append(eval(par))

resultado = fecho_transitivo(pares)
print(f"\nFecho transitivo:\n{resultado}")
print('\n')