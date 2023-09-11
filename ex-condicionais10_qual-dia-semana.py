def main():
    '''
    Faça um Programa que leia um número e exiba o dia correspondente
    da semana. (1-Domingo, 2- Segunda, etc.). Se digitar outro valor
    deve aparecer valor inválido.
    '''
    dias_semana = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado']

    dia = int(input('Informe um dia de 1 a 7, para que eu lhe diga que dia da semana é este: '))
    
    if not 0 < dia < 8:
        print('Esta dia é inválido.')
    else:
        x = dia -1
        print(f'O dia da semana informado é {dias_semana[x]}.')


if __name__ == '__main__':
    main()