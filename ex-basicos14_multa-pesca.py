def main():
    '''
    João Papo-de-Pescador, comprou um microcomputador para controlar o rendimento 
    diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o 
    estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
    deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você 
    faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. 
    Gravar na variável excesso a quantidade de quilos além do limite e na variável 
    multa o valor da multa que João deverá pagar. Imprima os dados do programa 
    com as mensagens adequadas.
    '''
    peso = float(input('Bem vindo, João. Quantos quilos sua pesca rendeu hoje? '))
    excesso = peso - 50

    if excesso < 0:
        excesso = 0

    multa = 4.00 * excesso

    if multa == 0:
        print('A quantidade pescada não está sujeita a multa.')
    else:
        print(f'Você excedeu o limite em {excesso} kg. A multa será de {multa}.')


if __name__ == '__main__':
    main()