#importando as bibliotecas necessárias
from flask import Flask, render_template, request
from models.pokemon import Pokemon
import requests
import json

#definindo o template
app = Flask(__name__, template_folder='template')

@app.route("/")
def index():
    return render_template("index.html")
#definindo o método do formulario
@app.route("/searchPoke", methods=["GET","POST"])

def searchPoke():
    pokemon = Pokemon(request.form["nome"], "","","","","","","","")
    try:
        res = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.nome}").text)
        #res_id = json.loads(requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.id}").text)
        result = res["sprites"]
        pokemon.index = idx = res["id"]
        result = result["front_default"]
        pokemon.foto = result

        
        if len(res["types"])==2:
            pokemon.tipo1 = res["types"][0]["type"]["name"]
            pokemon.tipo2 = res["types"][1]["type"]["name"]
        else:
            pokemon.tipo1 = res["types"][0]["type"]["name"]
            pokemon.tipo2 = "null"
        
        if len(res["stats"])==6:
            pokemon.hp = res["stats"][0]["base_stat"]
            pokemon.attack = res["stats"][1]["base_stat"]
            pokemon.defense = res["stats"][2]["base_stat"]
            pokemon.speed = res["stats"][5]["base_stat"]
    except:
        return "Pokemon não encontrado."
    return render_template("index.html", 
    nome = pokemon.nome, 
    foto = pokemon.foto,
    tipo1 = pokemon.tipo1,
    tipo2 = pokemon.tipo2,
    hp = pokemon.hp,
    attack = pokemon.attack,
    defense = pokemon.defense,
    speed = pokemon.speed,
    index = pokemon.index
    )
    ##return pokemon.nome
if __name__=='__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['TESTING'] = True
    app.run(debug=True) 