A = input("\nInsira os elementos para o conjunto A separados por espaço: ")

Ca = set(A.split())

B = input("Insira os elementos para o conjunto B separados por espaço: ")

Cb = set(B.split())

intersecao = Ca.intersection(Cb)

print(f"\nInterseção: {intersecao}", "\n")

uniao = Ca.union(Cb)

print(f"\nUnião: {uniao}", "\n")