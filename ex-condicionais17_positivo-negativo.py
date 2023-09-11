def main():
    '''
    Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
    '''
    num = float(input('Por favor, informe um valor de sua preferência: '))

    print(f'{num} é positivo.') if num >= 0 else print(f'{num} é negativo')


if __name__ == '__main__':
    main()