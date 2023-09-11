def main():
    '''
    Digite um nome, calcule e retorne quantas letras tem esse nome.
    '''
    nome = input('Informe seu nome: ')
    nome = nome.replace(' ', '')
    print(f'Seu nome possui {len(nome)} letras.')
    

if __name__ == '__main__':
    main()