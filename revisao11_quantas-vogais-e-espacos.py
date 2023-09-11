def main():
    '''    
    Conte espaços e vogais. Dado uma string com uma frase informada pelo 
    usuário (incluindo espaços em branco), conte quantos espaços em branco 
    existem na frase e quantas vezes aparecem as vogais a, e, i, o, u.

    '''
    frase = (str(input('Informe uma frase: ')))
    frase = frase.lower()

    print(vogais(frase))


def vogais(string):
    aeiou = {' ': 0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    
    for x in string:
        if x in aeiou.keys():
            aeiou[x] += 1

    resultado = (f'Vogal "a" aparece {aeiou["a"]} vezes\n'
    +f'Vogal "e" aparece {aeiou["e"]} vezes\n'
    +f'Vogal "i" aparece {aeiou["i"]} vezes\n'
    +f'Vogal "o" aparece {aeiou["o"]} vezes\n'
    +f'Vogal "u" aparece {aeiou["u"]} vezes\n'
    +f'A frase possui {aeiou[" "]} espaços')

    return resultado


if __name__ == '__main__':
    main()