def fibonacci(n):
    sequencia = [0, 1]  
    for i in range(2, n):
        next_number = sequencia[i-1] + sequencia[i-2]  
        sequencia.append(next_number)  
    return sequencia

n = int(input('\nEntre com a quantidade de termos: '))  
fib_sequencia = fibonacci(n)
print(f'\nA sequência para {n} termos é: \n{fib_sequencia}')
print("\n")