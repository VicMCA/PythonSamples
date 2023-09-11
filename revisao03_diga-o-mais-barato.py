def main():
    '''
    Faça um programa que pergunte o preço de três produtos e informe qual 
    produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
    '''
    prod1 = float(input('Digite o preço do primeiro produto: '))
    prod2 = float(input('Digite o preço do segundo produto: '))
    prod3 = float(input('Digite o preço do terceiro produto: '))

    if (prod1 > prod2):
        if (prod2 > prod3):
            print('Leve o terceiro produto.')
        else:
            print('Leve o segundo produto.')
    elif (prod1 > prod3):
        if (prod3 > prod2):
            print('Leve o segundo produto.')
        else:
            print('Leve o terceiro produto.')
    else:
        print('Leve o primeiro produto.')

    # print(min([prod1, prod2, prod3])) resolveria a questão também

if __name__ == '__main__':
    main()