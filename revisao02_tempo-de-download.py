def main():
    '''
    Faça um programa que peça o tamanho de um arquivo para download (em MB) e 
    a velocidade de um link de Internet (em Mbps), calcule e informe o tempo 
    aproximado de download do arquivo usando este link (em minutos).
    '''
    download = float(input('Digite o tamanho do arquivo: '))
    speed = float(input('Digite a velocidade de sua internet: '))

    print(f'O tempo aproximado de download deste arquivo ({download}MB)'
    +f' é de {round((download/((speed*60)/8)), 2)}min')


if __name__ == '__main__':
    main()