def main():
    '''    
    Faça um programa que calcule o mostre a média aritmética de N notas.
    '''
    quant_notas = int(input('Quantas notas deseja informar ao sistema? >> '))
    soma_notas = 0
    
    for x in range(0, quant_notas):
        nota = float(input('Diga a nota do aluno: '))
        soma_notas += nota
    
    media = soma_notas / quant_notas
    
    print(f'A média aritmética das notas informadas é de {media}')


if __name__ == '__main__':
    main()