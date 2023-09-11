def main():
    '''    
    Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
    '''
    num = int(input('Informe um número inteiro por favor: '))

    piramide(num)
    

def piramide(num):
    for x in range(1, num+1):
        line = ''
        for y in range(1, x+1):
            line = line + f'{x} '
        print(line)    


if __name__ == '__main__':
    main()