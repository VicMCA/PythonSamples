def main():
    '''
    Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro 
    número elevado ao segundo número. Não utilize a função de potência da linguagem.
    '''
    base = float(input('Vamos exponenciar? Digite a base: '))
    expo = int(input('Agora digite o expoente: '))

    resultado = 1

    for x in range(0, expo):
        resultado *= base

    print(f'O resultado é {resultado}')


if __name__ == '__main__':
    main()