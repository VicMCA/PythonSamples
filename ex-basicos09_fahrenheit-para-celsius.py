def main():
    '''
    Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    A fórmula para isso é C = 5 * ((F-32) / 9).
    '''
    fahr = float(input('Por gentileza, informe a temperatura no medidor Fahrenheit: '))
    print(f'A temperatura em Celsius é de {round(5 * ((fahr - 32) / 9), 2)}')


if __name__ == '__main__':
    main()