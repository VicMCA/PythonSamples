def main():
    '''
    Faça um Programa que peça uma data no formato dd/mm/aaaa e
    determine se a mesma é uma data válida.
    '''
    dia, mes, ano = [int(x) for x in input('Informe dia, mês e ano separados por /: ').split('/')]

    mes30 = [4, 6, 9, 11]

    bissexto = ((ano % 4) == 0 and (ano % 100) != 0) or (ano % 400 == 0)

    if (0 < mes < 13) and 0 < dia:
        if dia > 31:
            print('Esta data é inválida. Nenhum mês tem mais de 31 dias.')
        else:
            if mes == 2:
                if dia <=28:
                    print(f'Esta data é válida. A data informada é {dia}/{mes}/{ano}.')
                elif dia == 29 and bissexto == False:
                    print('Esta data é inválida. Neste ano Fevereiro não é bissexto.')
                elif dia == 29 and bissexto == True:
                    print(f'Esta data é válida. A data informada é {dia}/{mes}/{ano}.')
                else:
                    print('Esta data é inválida. Fevereiro nunca tem mais de 29 dias.')
            elif mes in mes30:
                if dia < 31:
                    print(f'Esta data é válida. A data informada é {dia}/{mes}/{ano}.')
                else:
                    print('Esta data é inválida. Este mês não tem mais de 30 dias.')
            else:
                print(f'Esta data é válida. A data informada é {dia}/{mes}/{ano}.')



if __name__ == '__main__':
    main()