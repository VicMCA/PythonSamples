def main():
    '''
    Crie um programa que possua uma lista de nomes. Peça que o usuário insira 
    um nome que será buscado nesta lista. A busca deve ser implementada em 
    uma função que retorna os valores lógicos verdadeiro ou falso.
    '''
    lista_nomes = lista_pessoas()

    nome = input('Olá, por quem você deseja procurar? ')
    nome = nome.lower()

    if (busca_nome(lista_nomes, nome) == True):
        print('Certo, encontramos aqui na lista!')
    else:
        print('Infelizmente este nome não consta aqui.')


def busca_nome(lista, pessoa):
    for x in lista:
        if x == pessoa:
            return True
    return False


def lista_pessoas():
    listaTotal = ['alice', 'ana', 'amelia', 'amanda', 'artur', 'astrid', 'aline', 'arnaldo', 'andre',
    'beatriz', 'bianca', 'bruno', 'breno', 'barbara', 'bernardo', 'camila', 'caio', 'cecilia', 'carina',
    'cintia','catarina', 'carol', 'diana', 'denis', 'darla', 'daniela', 'diego', 'douglas', 'debora', 'eva',
    'eduardo', 'eduarda', 'elezabeth', 'elize', 'edith', 'emilia', 'ellen', 'eliana', 'evandra', 'evandro', 
    'fabiana', 'flavia', 'felipe', 'filipe', 'fernando', 'fernanda', 'fred', 'francisco', 'francisca', 'flora',
    'gabriele', 'gabriela', 'gustavo', 'giovana', 'georgia', 'george', 'gregorio', 'gonçalo', 'henrique',
    'humberto', 'hannah', 'hilda', 'hugo', 'ingrid','igor', 'iara', 'iuri', 'ionara', 'joao', 'jose', 'juliana',
    'jana', 'joana', 'jessica', 'jefferson', 'janaina', 'kelly', 'karen', 'katia', 'larissa', 'lilian', 'lais',
    'leticia', 'lucas', 'luiza', 'luis', 'lucio', 'luciano', 'lucia', 'luciana', 'lorena', 'lourival', 'ligia',
    'leandro', 'leona', 'lana', 'licurgo', 'lombardi', 'manoel', 'mauricio', 'mariana', 'maria', 'mario', 
    'milena', 'melania', 'mirtes', 'marta', 'miriam', 'mirela', 'marilia', 'magno', 'magda', 'matilda', 'mel',
    'murilo', 'natalia', 'naiara', 'narele,' 'norberto', 'nona', 'osvaldo', 'olivia', 'olga', 'odara', 'oli',
    'odete', 'onofre', 'omar', 'pamela', 'paulo', 'paula', 'pedro', 'pandora', 'patricia', 'pietro', 'panthro',
    'paola', 'paulina', 'paloma', 'poliana', 'pablo', 'quiteria', 'rafael', 'rafaela', 'raul', 'renato', 'renata',
    'rebeca', 'rodrigo', 'regina', 'rodolfo', 'rufus', 'rubens', 'raissa', 'rivaldo', 'rolando', 'ronaldo', 'rita',
    'ricardo', 'rinaldo', 'sabrina', 'simone', 'saulo', 'safira', 'samara', 'sonia', 'sandra', 'sandro', 'santiago',
    'santana', 'soraya', 'suelen', 'suzana', 'tatiana', 'tatiane', 'tulio', 'tamires', 'tabata', 'tiago', 'tomas',
    'tony', 'tereza', 'umberto', 'vicente', 'victor', 'valeria', 'valentina', 'vinicius', 'voldemort', 'vampeta',
    'vitoria', 'viviana', 'viviane', 'valmir', 'wellington', 'washington', 'walmelia', 'zelia', 'zaya', 'zola']

    return listaTotal


if __name__ == '__main__':
    main()