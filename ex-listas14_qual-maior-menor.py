def main():
    '''
    Faça um Programa que leia três números e mostre o maior e o menor deles.
    '''
    print('Informe três números e retornarei o maior e menor dentre eles.')
    num1 = float(input('Informe o primeiro número: '))
    num2 = float(input('Informe o segundo número: '))
    num3 = float(input('Informe o terceiro número: '))

    numeros = [num1, num2, num3]

    menor = maior = numeros[0]

    for x in numeros:
        if x > maior:
            maior = x

    for x in numeros:
        if x < menor:
            menor = x

    print(f'O maior número informado é {maior} e o menor é {menor}.')


if __name__ == '__main__':
    main()