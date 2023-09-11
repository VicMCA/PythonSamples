def main():
    '''
    Faça um programa que receba do usuario uma string. 
    O programa imprime a string sem suas vogais.
    '''
    text = input('Informe uma palavra ou frase qualquer: ')
    vogais = ['a', 'e', 'i', 'o', 'u']
    
    for x in vogais:
        text = text.replace(x, '')
    print(text)
    

if __name__ == '__main__':
    main()