from flask import Flask, request, redirect, url_for
from jinja2 import Template, Environment, FileSystemLoader
import json

file_loader = FileSystemLoader('templates')
env = Environment(loader = file_loader)


app = Flask(__name__)


def mensaje ():
    mensaje = 'Web String Handler'
    return mensaje

def reverse(palabra: str):
    reversedS = palabra[::-1]
    return reversedS

def length(palabra: str):
    return len(palabra)

def vowels(palabra: str):
    vowel = "AaEeIiOoUu"
    return (len([letter for letter in palabra if letter in vowel]))

def consonants(palabra: str):
    consonants = "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz"
    return (len([letter for letter in palabra if letter in consonants]))

def upper(palabra: str):
    return palabra.upper()

def lower(palabra: str):
    return palabra.lower()

def updown(palabra: str):
    contador = 0
    upalabra =  ""
    for i in palabra:
        if contador % 2 == 0:
            upalabra = upalabra + i.lower()
        else:
            upalabra = upalabra + i.upper()
        contador += 1
    return upalabra
    

def naive(palabra: str):
    newpalabra = ""
    newpalabra = palabra.replace("a", "@").replace("e", "3").replace("i", "!").replace("o", "0").replace("u", ")")
    return newpalabra

def handler(palabra: str):
    outcome = {}
    if palabra == "":
        return outcome
    outcome["Reversed"] = reverse(palabra)
    outcome["Length"] = length(palabra)
    outcome["Vowels"] = vowels(palabra)
    outcome["Consonants"] = consonants(palabra)
    outcome["Upper"] = upper(palabra)
    outcome["Lower"] = lower(palabra)
    outcome["Updown"] = updown(palabra)
    outcome["Naive"] = naive(palabra)
    return outcome

 
@app.route('/', methods = ['GET', 'POST'])
def index():
    resultado = {}
    if request.method == 'POST':
        string_arg = request.form['String']
        print(f"String a manipular {string_arg}")
        resultado = handler(string_arg)
        print(f"diccionario a manipular{resultado}")

    template = env.get_template('handler.html')

    return template.render(resultado = resultado)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
