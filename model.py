import sqlite3

def adicionar_musica(musica, artista, tablatura, letra):
    with sqlite3.connect("Acorde.db") as conn:
        sql_insert_info = '''
        INSERT INTO info (musica, artista, tablatura, letra)
        VALUES (?, ?, ?, ?)
        '''
        conn.execute(sql_insert_info, (musica, artista, tablatura, letra))

def listar_musicas():
    with sqlite3.connect("Acorde.db") as conn:
        sql_listar_info = '''
        SELECT id, musica, artista, tablatura, letra
        FROM info
        '''
        cur = conn.cursor()        
        cur.execute(sql_listar_info)        
        return cur.fetchall() 
    

def listar_playlists():
    with sqlite3.connect("Acorde.db") as conn:
        sql_listar_playlists = '''
        SELECT nomes, id
        FROM playlists
        '''
        cur = conn.cursor()        
        cur.execute(sql_listar_playlists)        
        return cur.fetchall() 
    
def criar_playlist(nomes):
    with sqlite3.connect("Acorde.db") as conn:
        sql_criar_playlist = '''
        INSERT INTO playlists (nomes)
        VALUES (?)
        '''
        conn.execute(sql_criar_playlist, (nomes,))

def excluir_playlists(id):
    with sqlite3.connect("Acorde.db") as conn:
        sql_excluir_playlists = '''
        DELETE FROM playlists
        WHERE id = (?)
        '''
        conn.execute(sql_excluir_playlists, (id,)) 


def excluir_faixas(id):
    with sqlite3.connect("Acorde.db") as conn:
        sql_excluir_faixas = '''
        DELETE FROM info
        WHERE id = (?)
        '''
        conn.execute(sql_excluir_faixas, (id,)) 

def seek_musica(id, musica):
    with sqlite3.connect("Acorde.db") as conn:
        sql_seek_musica = '''
        SELECT id,musica
        FROM info
        WHERE musica = (?)
        '''
        conn.execute(sql_seek_musica, (id,musica)) 

