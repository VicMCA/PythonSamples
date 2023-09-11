import random

def main():
    '''    
    Construa uma função que receba uma string como parâmetro e devolva outra 
    string com os carateres embaralhados. Por exemplo: se função receber a 
    palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação 
    possível, de forma aleatória. Padronize em sua função que todos os 
    caracteres serão devolvidos em caixa alta ou caixa baixa, 
    independentemente de como foram digitados.
    '''
    string = input('Informe uma palavra ou frase que será embaralhada: ')
    embaralha(string)


def embaralha(termo):
    scramble = ''.join(random.sample(termo, len(termo)))
    scramble = scramble.lower()
    print(scramble)


if __name__ == '__main__':
    main()