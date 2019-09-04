from flask import Flask
from flask import jsonify
from flask import abort
app = Flask(__name__)

import requests
import json

def buscaArtista(ID):
    url = "https://api.genius.com"
    token = "D-33xCvktKud227T4BN3bryzCMQo3yKkdQN4Zz73U7E_m08IAyzUhcmR4MXfbLku"
    headers = {"Authorization": "Bearer " + token}
    search_url = url + "/search" + "?q=" + ID
    response = requests.get(search_url, headers=headers)
    json = response.json()
    if json['response']['hits'] == []:
        return None
    else:
        r = json['response']['hits'][0]['result']['primary_artist']['id']
    return r

def buscaMusica(artista):
    url = "https://api.genius.com"
    token = "D-33xCvktKud227T4BN3bryzCMQo3yKkdQN4Zz73U7E_m08IAyzUhcmR4MXfbLku"
    headers = {"Authorization": "Bearer " + token}
    musico = buscaArtista(artista)
    if musico is None:
        return None
    search_url = url + "/artists" + "/" + str(musico) + "/songs?sort=popularity"
    response = requests.get(search_url, headers=headers)
    json = response.json()
    r = json['response']['songs']
    return r


@app.route('/songs/<string:name>', methods=['GET'])
def songs(name):
    s = []
    songs = buscaMusica(name)
    if (songs is None):
        abort(404, description="Artista nao encontrado!")

    elif (len(songs) < 10):
        return "Artista com menos de 10 musicas!"

    else:

        for i in range (0,10):
            s.append(songs[i]['title'])
    
    return jsonify(s)

if __name__ == '__main__':
   app.run(debug = True)

