#Maritrini Velázquez Ruiz
#Api Restful para reconocimiento de entidades nombradas
from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

response = spacy.load('es_core_news_sm')


@app.route('/extract_ner', methods = ['POST'])
def return_ner():
    try:
        data = request.json
        sentences = data.get('oraciones',[])

        result = []
        for sentence in sentences:
            document = response(sentence)
            list_of_ner = []
            for entity in document.ents:
                list_of_ner.append({
                    'text': entity.text,
                    'label': entity.label_
                })
            result.append({
                'Oración': sentence,
                'Entidades':list_of_ner
            })
        return jsonify({'resultado':result})
    
    except Exception as e:
        return jsonify({'error': str(e)}),500


if __name__ == '__main__':
    app.run(port=3000,debug=True)
