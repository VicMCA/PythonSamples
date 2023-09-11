def main():
    '''
    Crie um programa para um circo, no qual dada a idade de uma pessoa, 
    seja indicado o valor do ingresso segundo as regras:
    a) A entrada para qualquer pessoa com menos de 4 anos ou maior que 60 é gratuita;
    b) a entrada para qualquer pessoa com idade entre 4 e 18 custa 20 reais;
    c) a entrada para qualquer pessoa com 18 ou mais custa 30 reais;
    d) estudantes e professores pagam meia-entrada.
    '''
    idade = int(input('Bem vindo ao Circo Lando! Por favor, informe sua idade: '))
    
    if 4 > idade or idade > 60:
        print('Seja bem-vindo(a), sua entrada é gratúita!')
    elif 3 < idade < 19:
        estudante = str(input('Você é estudante? s/n : '))
        estudante = estudante.lower()
        if estudante == 's':
            print('Sua entrada custa R$ 10,00. Seja bem-vindo(a)!')
        else:
            print('Sua entrada custa R$ 20,00. Seja bem-vindo(a)!')
    else:
        prof_estudante = str(input('Você é estudante ou professor? s/n : '))
        prof_estudante = prof_estudante.lower()
        if prof_estudante == 's':
            print('Sua entrada custa R$ 15,00. Seja bem-vindo(a)!')
        else:
            print('Sua entrada custa R$ 30,00. Seja bem-vindo(a)!')


if __name__ == '__main__':
    main()