def main():
    '''    
    Um palíndromo é uma palavra que se soletra da mesma forma nos dois 
    sentidos, como “osso” e “reviver”. Escreva um função que dado uma 
    plavra verifique se ela é palindro.
    '''
    palavra = input('Por favor, informe uma palavra para verificarmos se é um palíndromo ou digite "0" para sair: ')
    print('Programa encerrado.') if palavra == '0' else palindromo(palavra)

    
def palindromo(word):    
    drow = word[::-1]
    print('A palavra informada é um palíndromo.') if drow == word else print('Infelizmente NÃO é um palíndromo.')
    main()


if __name__ == '__main__':
    main()