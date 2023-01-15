import PySimpleGUI as psg
from imdb import artistas_por_letra
from imdb import diretores_por_letra
from imdb import filmes_por_artista
from imdb import filmes_por_diretor
from imdb import dados_do_filme

def criar_janela1():

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
        [psg.Listbox(values=[], select_mode='single', key='filmes', size=(64, 6), enable_events=True)]]
    
    return psg.Window('IMDB TOP 1000 FILMES', layout, size=(499, 400), finalize=True)


def criar_janela2():
    psg.theme('DarkGray13')
    layout = [[psg.Text('NOME DO FILME', key='nome_do_filme', size=(24, 0), font='Lucida', justification='center')],
              [psg.Output(size=(260, 17), key='dados_do_filme')],              
              [psg.Button('VOLTAR')]]    
    return psg.Window('IMDB TOP 1000 FILMES', layout, size=(499, 400), element_justification='c', finalize=True)


def main():

    janela1, janela2 = criar_janela1(), criar_janela2()
    janela2.hide()
    
    while True:

        janela, evento, valores = psg.read_all_windows()
        
        if evento == psg.WIN_CLOSED or evento == 'Finalizar':
            janela.close()
            if janela == janela2:
                janela2 = None
            elif janela == janela1:
                janela1 = None
            break
        
        if evento == 'alfa_ator':
            if len(valores['alfa_ator']) == 1:
                letra = valores['alfa_ator']
                count_atores, atores = artistas_por_letra(letra)
                janela["atores"].update(values=atores)
                
        if evento == 'alfa_diretor':
            if len(valores['alfa_diretor']) == 1:
                letra = valores['alfa_diretor']
                count_diretores, diretores = diretores_por_letra(letra)
                janela["diretores"].update(values=diretores)

        if evento == 'atores':
            selecionado = valores[evento]
            contagem, filmes_artista = filmes_por_artista(''.join(selecionado))
            janela["filmes"].update(values=filmes_artista)

        if evento == 'diretores':
            selecionado = valores[evento]
            contagem, filmes_diretor = filmes_por_diretor(''.join(selecionado))
            janela["filmes"].update(values=filmes_diretor)

        if evento == 'filmes':
            selecionado = valores[evento]
            janela1.hide()
            janela2.un_hide()
            filme_info = dados_do_filme(''.join(selecionado))
            janela2["nome_do_filme"].update(''.join(selecionado))
            janela2["dados_do_filme"].update(''.join(filme_info))            
           
        if janela == janela2 and evento == 'VOLTAR':
            janela2.hide()
            janela1.un_hide()

if __name__ == '__main__':
    main()
