def main():
    '''
    Entre com um nome e imprima o nome somente se a primeira 
    letra do nome for “a” (maiuscula ou minuscula).
    '''
    nome = input('Informe seu primeiro nome: ')
    nome = nome.lower()
    if nome[0] == 'a':
        print(nome)
    

if __name__ == '__main__':
    main()