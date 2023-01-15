from imdb import artistas
from imdb import diretores
from imdb import artistas_por_letra
from imdb import diretores_por_letra

from imdb import filmes_por_artista
from imdb import filmes_por_diretor

from imdb import buscar_por_artista
from imdb import buscar_por_diretor

from imdb import informacoes_do_filme

#buscar_por_artista("Julia Roberts")
#buscar_por_artista("Scarlett Johansson")

#buscar_por_diretor("Woody Allen")
#buscar_por_diretor("Joss Whedon")
#buscar_por_diretor("Anthony Russo")
#buscar_por_diretor("Oliver Stone")

#buscar_por_diretor("Stanley Kubrick")

poster_link, filme_info = informacoes_do_filme("Captain America: The Winter Soldier")

print(poster_link)


"""
contagem, filmes = filmes_por_artista("Scarlett Johansson")

print("\n---- filmes por artista ----")

for filme in filmes:
    print(filme)

print(contagem)

"""


"""
contagem, filmes = filmes_por_diretor("Stanley Kubrick")

print("\n---- filmes por diretor ----")

for filme in filmes:
    print(filme)

print(contagem)

"""

"""
# Testando - artistas

quantidade, artistas = artistas()

for nome in artistas:
    print(nome)

print("\nQuantidade:", quantidade)

"""

"""
# Testando - diretores

quantidade, diretores = diretores()

for nome in diretores:
    print(nome)

print("\nQuantidade:", quantidade)

"""

"""
# Testando - diretores por letra

quantidade, diretores = diretores_por_letra("S")

for nome in diretores:
    print(nome)

print("\nQuantidade:", quantidade)

"""

"""
# Testando - artistas por letra

quantidade, artistas = artistas_por_letra("J")

for nome in artistas:
    print(nome)

print("\nQuantidade:", quantidade)

"""
