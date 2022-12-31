import PySimpleGUI as psg

alfabeto = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(',')

lista = ["teste", "com", "lista"]

psg.theme('SandyBeach')

layout = [
    [psg.Text('ATORES (A-Z)', size=(24, 0), font='Lucida', justification='center'),
     psg.Text('DIRETORES (A-Z)', size=(24, 0), font='Lucida', justification='center')],    
    [psg.Combo(alfabeto, default_value='ESCOLHA A LETRA', key='alfa_ator', size=(30, 6), enable_events=True),
     psg.Combo(alfabeto, default_value='ESCOLHA A LETRA', key='alfa_diretor', size=(30, 6), enable_events=True)],        
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
    
    if valores['alfa_ator'] != "ESCOLHA A LETRA":
        #print((valores['alfa_ator']))
        janela["atores"].update(values=[f"A letra é {valores['alfa_ator']}"]) # Se não colocar o valor entre colchetes, imprimirá um caracter em cada linha da listbox
        
    if valores['alfa_diretor'] != "ESCOLHA A LETRA":
        #print((valores['alfa_diretor']))        
        janela["diretores"].update(values=[f"A letra é {valores['alfa_diretor']}"]) # Se não colocar o valor entre colchetes, imprimirá um caracter em cada linha da listbox

    if evento == 'atores':
        selection = valores[evento]
        #print(selection)
        janela["filmes"].update(values=selection)

    if evento == 'diretores':
        selection = valores[evento]
        #print(selection)
        janela["filmes"].update(values=selection)

janela.close()
