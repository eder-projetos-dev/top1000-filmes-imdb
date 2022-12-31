import PySimpleGUI as psg

alfabeto = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(',')

psg.theme('SandyBeach')

layout=[[psg.Text('ATORES (A-Z)', size=(24, 0), font='Lucida', justification='center'),
     psg.Text('DIRETORES (A-Z)', size=(24, 0), font='Lucida', justification='center')],
    
    [psg.Combo(alfabeto, default_value='ESCOLHA A LETRA', key='alfa-ator', size=(30, 6)),
     psg.Combo(alfabeto, default_value='ESCOLHA A LETRA', key='alfa-diretor', size=(30, 6))],
        
    [psg.Listbox(values=[], select_mode='single', key='atores', size=(30, 6)),
     psg.Listbox(values=[], select_mode='single', key='diretores', size=(30, 6))],
        
    [psg.Text('FILMES', size=(50, 0), font='Lucida', justification='center')],

    [psg.Listbox(values=[], select_mode='single', key='fac3', size=(64, 6))]]

janela = psg.Window('IMDB TOP 1000 FILMES', layout)

evento, valores = janela.read()

janela.close()
