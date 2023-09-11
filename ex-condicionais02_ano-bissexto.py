def main():
    '''
    Faça um Programa que peça um número correspondente a um determinado
    ano e em seguida informe se este ano é ou não bissexto.
    '''
    calc()

    de_novo = str(input('Deseja informar outro ano? s/n > '))
    de_novo = de_novo.lower()

    while de_novo == 's':
        calc()
        de_novo = str(input('Deseja informar outro ano? s/n > '))
        de_novo = de_novo.lower()
    else:
        print('Certo. Até a próxima.')


def calc():
    ano = int(input('Por favor, informe um ano para conferirmos se é ou não bissexto: '))

    if ((ano % 4) == 0 and (ano % 100) != 0) or (ano % 400 == 0):
        print('O ano informado é bissexto.')
    elif (ano % 100) == 0:
        print('O ano informado não bissexto.')
    else:
        print('O ano informado não bissexto.')


if __name__ == '__main__':
    main()