from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/pokeapi', methods=['GET', 'POST'])
def pokeapi():
    if request.method == 'POST':
        # Obtener el nombre del Pokémon del formulario
        pokemon_name = request.form.get('pokemon_name')
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}'
        response = requests.get(url)
        if response.ok:
            pokemon_data = response.json()
            image_url = pokemon_data['sprites']['front_default']
        else:
            image_url = None
    else:
        image_url = None
    return render_template('index.html', image_url=image_url)

@app.route('/')
def presentacion():
    # Esta ruta renderiza presentacion.html
    return render_template('presentacion.html')

@app.route('/tienda')
def tienda():
    # Esta ruta renderiza presentacion.html
    return render_template('tienda.html')

@app.route('/proyecto')
def proyecto():
    # Esta ruta renderiza presentacion.html
    return render_template('proyecto.html')

@app.route('/donaciones')
def donaciones():
    # Esta ruta renderiza presentacion.html
    return render_template('donaciones.html')

if __name__ == '__main__':
    app.run(debug=True)