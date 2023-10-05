#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 16:23:15 2023

@author: Horacio Herrera garcía
"""
### Instrucciones
#### Debes instalar spacy con lo siguiente: pip install flask spacy
#### Después necesitas descargar el modelo en español: python -m spacy download es_core_news_sm
#### Después corres el siguiente código y en la terminal corres el ejemplo que se encuentra al final.

    
from flask import Flask, request, jsonify
import spacy

# Inicializa Flask y Spacy
app = Flask(__name__)
# Carga el modelo en español
nlp = spacy.load("es_core_news_sm")

@app.route('/recognize_entities', methods=['POST'])
def recognize_entities():
    
    # Obtener datos del JSON 
    data = request.get_json()
    sentences = data['oraciones']
    response = {'resultado': []}
    
    for sentence in sentences:
        doc = nlp(sentence)     
        #Construir un diccionario para cada entidad detectada
        entities = {ent.text: ent.label_ for ent in doc.ents}
        response['resultado'].append({
            'oración': sentence,
            'entidades': entities
        })
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, port=5000)



### Ejemplo de como meterlo en la terminal 
"""curl -X POST -H "Content-Type: 
   application/json" -d '{"oraciones": ["El presidente de México anunció una nueva política de educación.", 
   "La torre Eiffel es uno de los monumentos más icónicos de París.", 
   "Microsoft y Google son competidores en el mercado de tecnología."]}' http://127.0.0.1:5000/recognize_entities"""

    
### Y esto da como resultado
""" {
  "resultado": [
    {
      "entidades": {
        "M\u00e9xico": "LOC"
      },
      "oraci\u00f3n": "El presidente de M\u00e9xico anunci\u00f3 una nueva pol\u00edtica de educaci\u00f3n."
    },
    {
      "entidades": {
        "Par\u00eds": "PER",
        "torre Eiffel": "LOC"
      },
      "oraci\u00f3n": "La torre Eiffel es uno de los monumentos m\u00e1s ic\u00f3nicos de Par\u00eds."
    },
    {
      "entidades": {
        "Google": "ORG",
        "Microsoft": "ORG"
      },
      "oraci\u00f3n": "Microsoft y Google son competidores en el mercado de tecnolog\u00eda."
    }
  ]
}
"""
