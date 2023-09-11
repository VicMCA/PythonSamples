def main():
    '''
    Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo
    que calcule seu peso ideal, utilizando as seguintes fórmulas:
    Para homens: (72.7*h) - 58
    Para mulheres: (62.1*h) - 44.7
    '''
    alt = float(input('Olá, vamos calcular seu peso ideal? Para isso me informe sua altura em metros: '))
    sexo = str(input('Agora me diga, você é homem ou mulher? '))
    sexo = sexo.lower()

    if 'h' in sexo[0]:
        print(f'Seu peso ideal é de aproximadamente {round(((72.7 * alt) - 58), 2)} kg.')
    if 'm' in sexo[0]:
        print(f'Seu peso ideal é de aproximadamente {round(((62.1 * alt) - 44.7), 2)} kg.')


if __name__ == '__main__':
    main()