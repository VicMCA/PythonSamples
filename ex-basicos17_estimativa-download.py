def main():
    '''
    Faça um programa que peça o tamanho de um arquivo para download (em MB)
    e a velocidade de um link de Internet (em Mbps), calcule e informe o
    tempo aproximado de download do arquivo usando este link (em minutos).
    '''
    tamanho = float(input('Qual o tamanho do arquivo solicitado em MB? '))
    velocidade = float(input('Qual a velocidade de sua internet em Mbps? '))

    print(f'O tempo aproximado de download para seu arquivo é de {round(((tamanho * 8.0) / velocidade), 2)} segundos.')


if __name__ == '__main__':
    main()