def main():
    '''
    Faça um Programa que peça dois números e imprima a soma.
    '''
    x, y = [int(x) for x in input('Me informe dois números separados por um espaço, por gentileza: ').split()]
    print(f'A soma dos números informados é de {x+y}, confere?')


if __name__ == '__main__':
    main()