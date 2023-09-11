def main():
    '''
    Faça um programa que conte o numero de 1's e 0's que aparecem em um string. Exemplo:
    0011001 -> 4 "0's", 3 "1's"
    '''
    frase = input('Por favor, informe uma frase qualquer, ela será convertida em binário: ')
    print(f'Frase informada  = {frase}')
    
    f_bin = ''.join(format(ord(x), '08b') for x in frase)
    print(f'Frase em binário = {f_bin}')
    
    count_zero = 0
    count_one = 0

    for x in f_bin:
        if x == '0': count_zero += 1
        if x == '1': count_one += 1

    print(f'Total de "0"s na frase= {count_zero}')
    print(f'Total de "1"s na frase= {count_one}')
    

if __name__ == '__main__':
    main()