def main():
    '''
    Leia um vetor contendo letras de uma frase inclusive os espaços em branco.
    Retirar os espaços em branco do vetor e depois escrever o vetor resultante.
    '''
    frase = input('Por favor, informe uma frase qualquer, que removerei seus espaços: ')
    frase_junta_vetor = []
        
    frase_vetor = [x for x in frase]
    print(f'Frase informada em forma de vetor = {frase_vetor}')
    
    for x in frase_vetor:
        if x != ' ': frase_junta_vetor.append(x)

    frase_junta = ''.join(x for x in frase_junta_vetor)
    
    print(f'Frase sem espaços = {frase_junta}')
    print(f'Vetor da frase sem espaços = {frase_junta_vetor}')
    

if __name__ == '__main__':
    main()