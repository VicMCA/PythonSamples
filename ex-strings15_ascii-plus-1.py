def main():
    '''
    Faça um programa que leia uma palavra e some 1 no valor ASCII
    de cada caractere da palavra. Imprima a string resultante.
    '''
    word = input('Por favor, informe uma palavra qualquer: ')
    word_p1 = []

    for x in word:
        temp = chr(ord(x)+1)
        word_p1.append(temp)
    
    word_p1 = ('').join(word_p1)
    print(word_p1)
    

if __name__ == '__main__':
    main()