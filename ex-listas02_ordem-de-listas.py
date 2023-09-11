def main():
    '''    
    Crie uma lista de locais que você gostaria de conhecer no mundo,
    na ordem do local que você dá mais prioridade pra o local que você dá
    menos prioridade. Exiba a lista nas seguintes configurações:
    a) ordem original
    b) ordem alfabética
    c) ordem de prioridades inversa
    d) quantidade de itens
    '''
    locais_visita = []
    locais_total = int(input('Quantos locais você deseja visitar na sua vida? >> '))
    print('Abaixo digite os locais a visitar na ordem do que mais deseja para o que menos deseja: ')
    for x in range(0, locais_total):
        local = input('Nome do local >> ')
        locais_visita.append(local)
    
    locais_alfab = sorted(locais_visita)
    locais_rever = locais_visita[:]
    locais_rever.reverse()
    
    print(f'Os locais que você deseja visitar: {locais_visita}')
    print(f'Os locais que você deseja visitar em ordem alfabética: {locais_alfab}')
    print(f'Os locais que você deseja visitar em ordem invertida: {locais_rever}')
    print(f'Quantidade de locais que deseja visitar: {len(locais_visita)}')


if __name__ == '__main__':
    main()