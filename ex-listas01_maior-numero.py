def main():
    '''
    Faça um programa que leia 5 números e informe o maior número.
    '''
    numeros = []
    x = 0
    while x < 5:
        num = float(input('Insira um número na lista >> '))
        x = x + 1
        numeros.append(num)

    print(f'O maior número informado na lista é {max(numeros)}')
    

if __name__ == '__main__':
    main()