def main():
    '''
    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho 
    em metros quadrados da área a ser pintada. Considere que a cobertura da tinta 
    é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 
    18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de 
    tinta a serem compradas e o preço total. Obs.: somente são vendidos um 
    número inteiro de latas.
    '''
    print('Bem vindo(a) ao Varejo Paredarte, vamos conferir quantas latas você precisa!')
    area = float(input('Informe a área a ser pintada em m², não é necessário digitar a unidade de medida: '))
    area_tinta = area / 3
    quant_latas = (area_tinta / 18) if (area_tinta % 18 == 0) else (area_tinta // 18 + 1)
    
    print(f'Você precisará de {int(quant_latas)} latas. O custo total será de R$ {quant_latas * 80}.')


if __name__ == '__main__':
    main()