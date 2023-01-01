import PySimpleGUI as psg

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
        janela["atores"].update(values=[f"A letra é {valores['alfa_ator']}"])
        
    if len(valores['alfa_diretor']) == 1:        
        janela["diretores"].update(values=[f"A letra é {valores['alfa_diretor']}"])

    if evento == 'atores':
        selection = valores[evento]        
        janela["filmes"].update(values=selection)

    if evento == 'diretores':
        selection = valores[evento]        
        janela["filmes"].update(values=selection)

janela.close()
