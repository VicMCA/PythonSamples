def main():
    '''
    Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    1. o produto do dobro do primeiro com metade do segundo.
    2. soma do triplo do primeiro com o terceiro.
    3. terceiro elevado ao cubo.
    '''
    print('Vou lhe pedir três números a seguir, por favor me informe:')
    int1 = int(input('Um número inteiro: '))
    int2 = int(input('Outro número inteiro: '))
    real = float(input('Um número real: '))
    
    print(f'Produto do dobro do primeiro com a metade do segundo: (a * 2) * (b / 2) = {(int1 * 2) * (int2 / 2)}')
    print(f'Soma do triplo do primeiro com o terceiro número: (a * 3) + b = {int1 * 3 + real}')
    print(f'Terceiro número elevado ao cubo: a ** 3 = {real ** 3}')


if __name__ == '__main__':
    main()