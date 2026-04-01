from flask import Flask, render_template, request, redirect, flash

from secrets import token_hex

import model

app = Flask(__name__)
app.secret_key = token_hex()

@app.get("/adicionar_musica")
def get_musica():
    listagem_musicas = model.listar_musicas()
    return render_template("/adicionar_musica.html", info=listagem_musicas, pag_nome = "Adicionar Música")

@app.post("/adicionar_musica")
def post_musica():
    musica = request.form["musica"]
    artista = request.form["artista"]
    tablatura = request.form["tablatura"]
    letra = request.form["letra"]
    model.adicionar_musica(musica, artista, tablatura, letra)

    return redirect("/adicionar_musica") 

@app.get("/playlists")
def get_playlists():
    listagem_playlists = model.listar_playlists()
    return render_template("/playlists.html", pl = listagem_playlists, pag_nome = "Playlists")

@app.post("/playlists")
def post_playlists():
    playlistNome = request.form["playlistNome"]
    model.criar_playlist(playlistNome)

    return redirect("/playlists")

@app.get("/excluir/playlists/<id>")
def get_excluir_playlist(id):
    model.excluir_playlists(id)
    return redirect("/playlists") 

@app.get("/excluir/faixa/<id>")
def get_excluir_faixa(id):
    model.excluir_faixas(id)
    return redirect("/")

@app.get("/")
def get_faixas():
    listagem_musicas = model.listar_musicas()
    return render_template("faixas.html", info=listagem_musicas, pag_nome = "Faixas") 

@app.get("/index")
def get_index():
    return render_template("/index.html")

@app.get("/interface")
def get_styling():
    return render_template("/interface.html")


if __name__ == '__main__':
    app.run(debug=True)