def main():
    '''
    Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
    '''
    vogais = ['a', 'e', 'i', 'o', 'u']

    letra = str(input('Informe uma letra e lhe direi se é vocal ou consoante: '))

    if letra in vogais:
        print('A letra informada é uma vogal.')
    else:
        print('A letra informada é uma consoante.')


if __name__ == '__main__':
    main()