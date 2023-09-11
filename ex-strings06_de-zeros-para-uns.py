def main():
    '''
    Escreva um programa que substitui as ocorrencias de um 
    caractere 0 em uma string por outro caractere 1.
    '''
    texto = input('Informe um texto que contenha zeros e uns: ')
    texto = texto.replace('0', '1')
    print(texto)
    

if __name__ == '__main__':
    main()