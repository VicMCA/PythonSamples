import random

def main():
    '''
    Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes 
    e armazene os resultados em um vetor . Depois, mostre quantas vezes cada 
    valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função 
    para gerar numeros aleatórios, simulando os lançamentos dos dados.
    '''
    results = []
    count = [0, 0, 0, 0, 0, 0]
    temp = 0

    for x in range(100):
        temp = random.randint(1, 6)
        results.append(temp)
        count[temp -1] += 1 # Não usado na solução alternativa

    # solução alternativa
    # for n in results:
    #     count[results -1] += 1

    print(f'Após 100 lançamentos, o dado caiu:\n'
    +f'{count[0]} vezes na posição 1\n'
    +f'{count[1]} vezes na posição 2\n'
    +f'{count[2]} vezes na posição 3\n'
    +f'{count[3]} vezes na posição 4\n'
    +f'{count[4]} vezes na posição 5\n'
    +f'{count[5]} vezes na posição 6\n')


if __name__ == '__main__':
    main()