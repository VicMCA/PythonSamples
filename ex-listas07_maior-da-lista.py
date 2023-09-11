def main():
    '''    
    Faça um programa que recebe do usuário 10 valores de números inteiros,
    armazena em um vetor e apos percorre-lo exibe qual é o maior valor e a sua posição.
    '''
    print('Vou lhe pedir 10 números inteiros abaixo')
    lista = []
    for x in range(1, 11):
        num = int(input('Diga um número inteiro: '))
        lista.append(num)
    print(max(lista))
    print(f'O maior número é {max(lista)} que se encontra no índice {lista.index(max(lista))}')


if __name__ == '__main__':
    main()