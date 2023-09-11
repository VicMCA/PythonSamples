def main():
    '''
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas
    trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
    sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS
    e 5% para o sindicato, faça um programa que nos dê:
    1. salário bruto.
    2. quanto pagou ao INSS.
    3. quanto pagou ao sindicato.
    4. o salário líquido.
    5. calcule os descontos e o salário líquido, conforme a tabela abaixo:
        + Salário Bruto : R$
        - IR (11%) : R$
        - INSS (8%) : R$
        - Sindicato ( 5%) : R$
        = Salário Liquido : R$
    * Obs.: Salário Bruto - Descontos = Salário Líquido.
    '''
    print('Bem-vindo(a). Para lhe auxiliar no cálculo de seu rendimento líquido, por favor informe:')
    preco_hora = float(input('O valor/hora de seu trabalho > R$ '))
    total_horas = float(input('O total de horas trabalhadas neste mês > '))
    rend_bruto = preco_hora * total_horas
    desc_IR = rend_bruto * 0.11
    desc_INSS = rend_bruto * 0.08
    desc_sind = rend_bruto * 0.05
    rend_liq = rend_bruto - desc_INSS - desc_IR - desc_sind

    result = (f'''Rendimento bruto: R$ {rend_bruto}
    Imposto de renda: R$ {desc_IR}
    Taxa do INSS: R$ {desc_INSS}
    Taxa do sindicato: R$ {desc_sind}
    Rendimento líquido: R$ {rend_liq}''')

    result = result.replace('    ', '')
    print(result)


if __name__ == '__main__':
    main()