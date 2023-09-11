def main():
    '''
    Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
    '''
    celsius = float(input('Por gentileza, agora informe a temperatura no medidor Celsius: '))
    print(f'A temperatura em Fahrenheit é de {round(((celsius * 1.8) + 32), 2)}')


if __name__ == '__main__':
    main()