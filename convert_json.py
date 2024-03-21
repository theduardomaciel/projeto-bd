import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TagField, NumericField, TextField, VectorField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

new_json = []
json_path = input('Enter the path of the JSON file: ')
if not json_path:
    exit("JSON path cannot be empty!")

# Primeiro, lemos o arquivo JSON
with open(json_path, 'r') as file:
    new_json = json.load(file)

# Agora, conectamos ao Redis
r = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def map_json():
    # Iteramos pelas configurações procurando por [field-names]
    field_names = dict(config.items('field-names'))

    # Agora, vamos mapear os campos do JSON para o schema
    schema = ()

    for key in new_json[0]:
        # Se o campo estiver presente, adicionamos o campo ao schema
        if key in field_names:
            if field_names[key] == 'int':
                schema += (NumericField(f'$.{key}', sortable=True, as_name=key),)
            elif field_names[key] == 'float':
                schema += (NumericField(f'$.{key}', sortable=True, as_name=key),)
            else:
                schema += (TextField(f'$.{key}', sortable=True, as_name=key),)

    return schema

schema = map_json()

index_name = input('Enter the name of the index: ')
if not index_name:
    exit("Index name cannot be empty!")

# Agora, vamos criar o índice
rs = r.ft(index_name)

def create_index(schema):
    try:
        rs.create_index(
            schema,
            definition=IndexDefinition(
                prefix=["game:"], index_type=IndexType.JSON
            )
        )
        print('Índice criado com sucesso!')
    except Exception as e:
        print('Erro ao criar índice:', e)

create_index(schema)

# Agora, vamos indexar o documento JSON
for i, game in enumerate(new_json):
    r.json().set(f'game:{i}', Path.root_path(), game)

print('Arquivo JSON indexado no Redis com sucesso!')