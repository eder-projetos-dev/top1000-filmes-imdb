import PySimpleGUI as psg
from imdb import artistas_por_letra
from imdb import diretores_por_letra
from imdb import filmes_por_artista
from imdb import filmes_por_diretor

alfabeto = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(',')

psg.theme('DarkGray13')

layout = [
    [psg.Text('ATORES (A-Z)', size=(24, 0), font='Lucida', justification='center'),
     psg.Text('DIRETORES (A-Z)', size=(24, 0), font='Lucida', justification='center')],
    [psg.Combo(alfabeto, default_value='  ESCOLHA UMA LETRA', key='alfa_ator', readonly=True, size=(30, 6), enable_events=True),
     psg.Combo(alfabeto, default_value='  ESCOLHA UMA LETRA', key='alfa_diretor', readonly=True, size=(30, 6), enable_events=True)],
    [psg.Listbox(values=[], select_mode='single', key='atores', size=(30, 6), enable_events=True),
     psg.Listbox(values=[], select_mode='single', key='diretores', size=(30, 6), enable_events=True)],
    [psg.Text('FILMES', size=(50, 0), font='Lucida', justification='center')],
    [psg.Listbox(values=[], select_mode='single', key='filmes', size=(64, 6))]
]

janela = psg.Window('IMDB TOP 1000 FILMES', layout)

while True:
    evento, valores = janela.read()
    if evento == psg.WIN_CLOSED or evento == "Cancelar":
        break
    
    if len(valores['alfa_ator']) == 1:
        letra = valores['alfa_ator']
        count_atores, atores = artistas_por_letra(letra)
        janela["atores"].update(values=atores)
                 
    if len(valores['alfa_diretor']) == 1:
        letra = valores['alfa_diretor']
        count_diretores, diretores = diretores_por_letra(letra)
        janela["diretores"].update(values=diretores)

    if evento == 'atores':
        selection = valores[evento]
        contagem, filmes_artista = filmes_por_artista(''.join(selection)) 
        janela["filmes"].update(values=filmes_artista)

    if evento == 'diretores':
        selection = valores[evento]
        contagem, filmes_diretor = filmes_por_diretor(''.join(selection))
        janela["filmes"].update(values=filmes_diretor)        

janela.close()
