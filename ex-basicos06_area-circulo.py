def main():
    '''
    Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
    '''
    r = float(input('Por favor, informe o raio de seu círculo em cm para calcularmos sua área: '))
    print(f'A área de seu círculo é de aproximadamente {(r ** 2) * 3.14} cm²')


if __name__ == '__main__':
    main()