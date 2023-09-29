A = input("\nInsira os elementos para o conjunto A separados por espaço: ")
Ca = set(A.split())
B = input("Insira os elementos para o conjunto B separados por espaço: ")
Cb = set(B.split())
if Ca.issubset(Cb):
    print("\nA é um subconjunto de B.", "\n")
elif Cb.issubset(Ca):
    print("\nB é um subconjunto de A.", "\n")
else:
    print("\nA e B não são subconjuntos um do outro.", "\n")