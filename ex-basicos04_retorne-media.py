def main():
    '''
    Faça um Programa que peça as 4 notas bimestrais e mostre a média.
    '''
    a, b, c, d = [float(x) for x in input('Informe suas 4 notas bimestrais separadas por espaço: ').split()]
    print(f'Sua média bimestral é de {(a + b + c + d) / 4}')


if __name__ == '__main__':
    main()