def main():
    '''    
    Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
    '''
    for x in range(1, 50, 2): print(x)

    for x in range(0,51):
        if x % 2 != 0: print(x)


if __name__ == '__main__':
    main()