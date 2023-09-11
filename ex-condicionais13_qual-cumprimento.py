def main():
    '''
    Faça um Programa que pergunte em que turno você estuda. 
    Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
    Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
    ou "Valor Inválido!", conforme o caso.
    '''
    print('Olá! Qual o turno de seus estudos?')
    turno = str(input('Informe "M" para manhã, "T" para tarde ou "N" para noite >> '))
    turno = turno.upper()

    if turno == 'M':
        print('Bom dia e bons estudos!')
    elif turno == 'T':
        print('Boa tarde e bons estudos!')
    elif turno == 'N':
        print('Boa noite e bons estudos!')
    else:
        print('Desculpe, mas este valor é inválido.')


if __name__ == '__main__':
    main()