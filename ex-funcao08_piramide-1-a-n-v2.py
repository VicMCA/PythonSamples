def main():
    '''    
    Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
    '''
    num = int(input('Informe um número inteiro por favor: '))

    piramide(num)


def piramide(num):
    line = ''
    print(line)
    for x in range(1, num+1):
        line = line + f'{x} '
        print(line)


if __name__ == '__main__':
    main()