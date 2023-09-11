def main():
    '''
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas
    trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
    '''
    preco_hora = float(input('Qual o valor de sua hora de trabalho? R$ '))
    hora_mes = float(input('Quantas horas você trabalhou neste mês? '))
    print(f'Seu salário neste mês é será de R$ {preco_hora * hora_mes}')


if __name__ == '__main__':
    main()