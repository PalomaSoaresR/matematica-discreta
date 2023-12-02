soma = 0
i = 1
while i <= 19:
    if i % 4 == 1:
        soma += 1 / (i ** 5)
    else:
        soma -= 1 / (i ** 5)
    i += 2
print(f'\nO valor dos dez primeiros termos da série é: {soma:.4f}')
print('\n')
#valor dos dez primeiros termos, em que: 1/pot(1,5)-1/pot(3,5)+1/pot(5,5)-1/pot(7,5)+1/pot(9,5)- ...