def main():
    '''
    Leia uma cadeia de caracteres e converta todos os caracteres para maiuscula.
    Dica: subtraia 32 dos caracteres cujo codigo ASCII esta entre 65 e 90.
    '''
    frase = input('Por favor, informe uma palavra qualquer em letras MAIÚSCULAS: ')
    frase_min = frase

    for x in frase:
        temp = ord(x)
        if temp >= 65 and temp <= 90:
            temp = temp +32
            temp = chr(temp)
            frase_min = frase_min.replace(x, temp)
    
    print(frase_min)
    

if __name__ == '__main__':
    main()