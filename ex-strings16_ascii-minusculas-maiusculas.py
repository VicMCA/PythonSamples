def main():
    '''
    Leia uma cadeia de caracteres e converta todos os caracteres para maiuscula.
    Dica: subtraia 32 dos caracteres cujo codigo ASCII esta entre 65 e 90.
    '''
    frase = input('Por favor, informe uma palavra qualquer em letras minúsculas: ')
    frase_m = frase

    for x in frase:
        temp = ord(x)
        if temp >= 97 and temp <= 122:
            temp = temp -32
            temp = chr(temp)
            frase_m = frase_m.replace(x, temp)
    
    print(frase_m)
    

if __name__ == '__main__':
    main()