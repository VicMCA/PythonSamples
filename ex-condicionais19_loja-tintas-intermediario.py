def main():
    '''
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho
    em metros quadrados da área a ser pintada. Considere que a cobertura da tinta
    é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de
    18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    1. Informe ao usuário as quantidades de tinta a serem compradas e os
    respectivos preços em 3 situações:
    1.1. comprar apenas latas de 18 litros;
    1.2. comprar apenas galões de 3,6 litros;
    1.3. misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
    considere latas cheias.
    '''
    # Cobertura galão = 21.6 m²
    # Cobertura lata = 108 m²

    print('Bem vindo(a) ao Varejo Paredarte, vamos conferir quantas latas ou galões você precisa!')
    area = float(input('Informe a área a ser pintada em m², não é necessário digitar a unidade de medida: '))
    area = area * 1.1
    quant_latas = quant_galao = 0

    opcoes = ('''Você pode consultar o preço necessário em:
    [1]\tApenas latas de 18L por R$ 80,00 cada
    [2]\tApenas galões de 3.6L por R$ 25,00 cada
    [3]\tLatas e galões
    [4]\tDesistir da compra
    Digite o número da opção escolhida >> ''')

    escolha = str(input(opcoes.replace('    ', '')))

    while escolha != '1' and escolha != '2' and escolha != '3' and escolha != '0':
        print('Desculpe, mas esta opção não é válida.')
        escolha = int(input(opcoes.replace('    ', '')))

    if escolha == '0':
        print('Tudo bem, até a próxima então!')

    if escolha == '1':
        quant_latas = (area / 108) if (area % 108 == 0) else (area // 108 + 1)
        print(f'Quantidade de litros necessária para a área informada: {round(area, 2)}')
        print(f'Você precisará de {int(quant_latas)} latas. O custo total será de R$ {quant_latas * 80}.')

    if escolha == '2':
        quant_galao = (area / 21.6) if (area % 21.6 == 0) else (area // 21.6 + 1)
        print(f'Quantidade de litros necessária para a área informada: {round(area, 2)}')
        print(f'Você precisará de {int(quant_galao)} galões. O custo total será de R$ {quant_galao * 25}.')

    if escolha == '3':
        if (area % 108 == 0):
            quant_latas = (area/108)
        else:
            excedente = (area % 108)
            quant_latas = (area // 108)
            if (area % 108 > (21.6 * 3)) and (area % 108 < (21.6 * 5)):
                quant_latas = quant_latas + 1
                quant_galao = 0
            else:
                if (area % 21.6 == 0):
                    quant_galao = (excedente / 21.6)
                else:
                    quant_galao = (excedente // 21.6 + 1)
        print(f'Quantidade de litros necessária para a área informada: {round(area, 2)}')
        print(f'Você precisará de {int(quant_latas)} latas e {quant_galao} galões.')
        print(f'O custo total será de R$ {(quant_latas * 80) + (quant_galao * 25)}.')


if __name__ == '__main__':
    main()