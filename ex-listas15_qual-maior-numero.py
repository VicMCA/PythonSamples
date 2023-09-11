def main():
    '''
    Faça um Programa que leia três números e mostre o maior deles.
    '''
    print('Informe três números e retornarei o maior dentre eles.')
    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))
    num3 = float(input('Informe o terceiro número: '))

    numeros = [num1, num2, num3]

    maior = numeros[0]

    for x in numeros:
        if x > maior:
            maior = x

    print(f'O maior número informado é {maior}.')


if __name__ == '__main__':
    main()