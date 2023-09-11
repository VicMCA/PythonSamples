def main():
    '''
    Faça um Programa que verifique se uma letra digitada é "F" ou "M".
    Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
    '''
    sexo = str(input('Por favor, informe seu sexo, "F" para feminino, "M" para masculino: '))
    sexo = sexo.upper()

    if sexo == 'F':
        print('O sexo informado é Feminino.')
    elif sexo == 'M':
        print('O sexo informado é Masculino.')
    else:
        print('O sexo informado não é válido.')


if __name__ == '__main__':
    main()