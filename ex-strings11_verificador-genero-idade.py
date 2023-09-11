def main():
    '''
    Ler nome, sexo e idade. Se sexo for feminino e idade menor que 25,
    imprime o nome da pessoa e a palavra “ACEITA”, caso contrario
    imprimir “NÃO ACEITA”.
    '''
    nome = input('Por favor, informe seu nome: ')
    idade = int(input('Qual sua idade? '))
    sexo = input('Qual gênero você se identifica? ')

    sexo = sexo.lower()

    if sexo[0] == 'f':
        if idade >= 25:
            print('ACEITA')
        else:
            print('NÃO ACEITA')
    else:
        print('NÃO ACEITA')


if __name__ == '__main__':
    main()