def main():
    '''
    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo
    que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
    '''
    alt = float(input('Por gentileza, informe sua altura em m: '))
    print(f'Seu peso ideal atual é de aproximadamente {round(((alt * 72.7) - 58), 2)} kg')


if __name__ == '__main__':
    main()