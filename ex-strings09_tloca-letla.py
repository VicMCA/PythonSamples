def main():
    '''
    Faça um programa em que troque todas as ocorrencias de uma letra L1 
    pela letra L2 em uma string. A string e as letras L1 e L2 devem 
    ser fornecidas pelo usuario.
    '''
    text = input('Informe uma palavra ou frase qualquer: ')
    L1 = input('Qual a primeira letra que deve ser trocada? ')
    L2 = input('Qual a segunda letra que deve ser trocada? ')
    
    print(text.replace(L1, L2))
    

if __name__ == '__main__':
    main()