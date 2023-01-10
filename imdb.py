arquivo = 'imdb_top_1000.csv'

filmes = []
arq = open(arquivo, 'r', encoding="utf8")
for linha in arq:
    split_linha = linha.split(";")
    filmes.append(split_linha)
arq.close()


""" Busca por artistas
Exemplos: Jennifer Connelly
Jennifer Lawrence
Scarlett Johansson
Julia Roberts """

def buscar_por_artista(artista):    
    for coluna in filmes:
        if (coluna[10] == artista or coluna[11] == artista or
            coluna[12] == artista or coluna[13] == artista):
            print(coluna[1])
            print("Nota:", coluna[6])
            print("Gênero:", coluna[5])
            print(coluna[10])
            print(coluna[11])
            print(coluna[12])
            print(coluna[13])
            print("Diretor:", coluna[9])
            print("-----------------------------")


""" Retorna todos os artistas
em ordem alfabética e a quantidade encontrada """

def artistas():
    lista_artistas = []
    for coluna in filmes:        
        lista_artistas.append(coluna[10])
        lista_artistas.append(coluna[11])
        lista_artistas.append(coluna[12])
        lista_artistas.append(coluna[13])
        artistas = set(lista_artistas)
        artistas = sorted(artistas)
    return len(artistas), artistas


""" Todos os artistas cujo nome começam com a letra informada,
em ordem alfabética e retorna a quantidade encontrada """

def artistas_por_letra(letra):
    lista_artistas = []
    for coluna in filmes:
        if coluna[10][0] == letra:
            lista_artistas.append(coluna[10])
        if coluna[11][0] == letra:
            lista_artistas.append(coluna[11])
        if coluna[12][0] == letra:
            lista_artistas.append(coluna[12])
        if coluna[13][0] == letra:
            lista_artistas.append(coluna[13])
        artistas = set(lista_artistas)        
    return len(artistas), sorted(artistas)


""" Busca por diretores
Exemplos: Sofia Coppola
Woody Allen
Joss Whedon
Anthony Russo """

def buscar_por_diretor(diretor):
    for coluna in filmes:
        if (coluna[9] == diretor):
            print(coluna[1])
            print("Nota:", coluna[6])
            print("Gênero:", coluna[5])
            print(coluna[10])
            print(coluna[11])
            print(coluna[12])
            print(coluna[13])
            print("Diretor:", coluna[9])
            print("-----------------------------")
            

""" Retorna todos os diretores
em ordem alfabética e a quantidade encontrada """

def diretores():
    lista_diretores = []
    for coluna in filmes:
        lista_diretores.append(coluna[9])
        diretores = set(lista_diretores)
        diretores = sorted(diretores)
    return len(diretores), diretores


""" Todos os diretores cujo nome começam com a letra informada,
em ordem alfabética e retorna a quantidade encontrada """

def diretores_por_letra(letra):
    lista_diretores = []
    for coluna in filmes:
        if coluna[9][0] == letra: 
            lista_diretores.append(coluna[9])
            diretores = set(lista_diretores)            
    return len(diretores), sorted(diretores)


""" Retorna a contagem e a lista de filmes estrelados por determinado artista """

def filmes_por_artista(artista):
    lista_de_filmes = []
    for coluna in filmes:
        if (coluna[10] == artista or coluna[11] == artista or
            coluna[12] == artista or coluna[13] == artista):
            lista_de_filmes.append(coluna[1])
    return len(lista_de_filmes), sorted(lista_de_filmes)


""" Retorna a contagem e a lista de filmes dirigidos por determinado diretor """

def filmes_por_diretor(diretor):
    lista_de_filmes = []
    for coluna in filmes:
        if (coluna[9] == diretor):
            lista_de_filmes.append(coluna[1])            
    return len(lista_de_filmes), sorted(lista_de_filmes)
