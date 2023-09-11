def main():
    '''
    Faça um programa para converter uma letra maiuscula em 
    letra minuscula. Use a tabela ASCII para resolver o problema.
    '''
    upper = input('Por favor, informe uma letra maiúscula: ')
    lower = chr(ord(upper)+32)
    print(lower)


if __name__ == '__main__':
    main()