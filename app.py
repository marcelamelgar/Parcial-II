from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)


app = Flask(__name__)
with open('data.json') as json_file:
    jsonfile = json.load(json_file)


def mensaje ():
    mensaje = 'Web String Handler'
    return "alert('" + mensaje + "')"

@app.route('/')
def index():
    template = env.get_template('handler.html')
    picture = url_for('static', filename = jsonfile['fotografia'])
    return template.render(torender = jsonfile['Render'], palabra = ['Word'], picture = picture)

@app.route('/new', methods = ['GET', 'POST'])
def nueva():
    if request.method == 'POST':
        _string = request.form['String']
        _length = request.form['Length']
        _vowels = request.form['Vowels']
        _consonants = request.form['Consonants']
        _upper = request.form['Upper']
        _lower = request.form['Lower']
        _updown = request.form['UpDown']
        _naive = request.form['Naive']
        print (f'{_string}{_length}{_vowels}{_consonants}{_upper}{_lower}{_updown}{_naive}')

        jsonfile['Render'].append({"Length": _length}, {"Vowels":_vowels}, {"Consonants": _consonants}, {"Upper": _upper}, {"Lower": _lower}, {"UpDown":_updown}, {"Naive": _naive})
        jsonfile['Word'].append({"String": _string})
        return redirect(url_for('handler'))
    template = env.get_template('form.html')
    return template.render()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
