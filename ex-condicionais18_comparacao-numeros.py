def main():
    '''
    Faça um Programa que peça dois números e imprima o maior deles.
    '''
    print('Por favor, informe dois números quaisquer abaixo:')
    a = float(input('1º número >> '))
    b = float(input('2º número >> '))

    print(f'O maior número é {a}') if a > b else print(f'O maior número é {b}') if b > a else print('Ambos são iguais')


if __name__ == '__main__':
    main()