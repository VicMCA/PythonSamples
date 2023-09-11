def main():
    '''
    Faça um programa, com uma função que necessite de três 
    argumentos, e que forneça a soma desses três argumentos.
    '''
    x = (float(input('Informe o primeiro número: ')))
    y = (float(input('Informe o segundo número: ')))
    z = (float(input('Informe o terceiro número: ')))

    print(f'A soma é {soma(x, y, z)}')


def soma(a, b, c):
    return a + b + c


if __name__ == '__main__':
    main()