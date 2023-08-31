##prueba spacy es_core_news_sm
import spacy

response = spacy.load('es_core_news_sm')

text = "Apple esta buscando comprar una startup del reino Unido por mil millones de dolares"

parser = response(text)

for entity in parser.ents:
    print(f'Found: {entity.text} of type: {entity.label_}')