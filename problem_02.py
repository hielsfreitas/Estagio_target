numero = int(input('Escreva um número: '))
fibonacci = 1
proximo_fibonacci = 2

while True:
    if numero == fibonacci:
        print(f'O número {numero} está na sequência de Fibonacci')
        break
    elif fibonacci > numero:
        print(f'O número {numero} não está na sequência de Fibonacci')
        break
    else:
        fibonacci, proximo_fibonacci = proximo_fibonacci, fibonacci + proximo_fibonacci
