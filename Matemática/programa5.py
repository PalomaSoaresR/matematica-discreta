conj1 = input("\nInsira os elementos para o conjunto A separados por espaço: ")
conj2 = input("\nInsira os elementos para o conjunto B separados por espaço: ")
elemento = int(input("Insira o elemento a ser verificado: "))

def verifica_pertinencia(elemento, conj1, conj2):
    if elemento in conj1:
        print('\n', elemento, 'pertence ao conjunto A.')
    elif elemento in conj2:
        print('\n', elemento, 'pertence ao conjunto B.')
    else:
        print('\n', elemento, 'não pertence nem ao conjunto A nem ao conjunto B.')
