def main():
    '''
    Ler uma frase e contar quantos caracteres sao brancos. Lembre-se que
    uma frase e um conjunto de caracteres (vetor).
    '''
    frase = input('Olá, me informe uma frase qualquer por favor: ')
    count = 0
    
    for x in frase:
        if x == ' ':
            count += 1
    
    print(f'Sua frase tem {count} espaços.')


if __name__ == '__main__':
    main()