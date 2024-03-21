import redis
from redis.commands.json.path import Path
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType

import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

new_json = []
json_path = input('Enter the path of the JSON file: ')

# Primeiro, lemos o arquivo JSON
with open(json_path, 'r') as file:
    new_json = json.load(file)

# Agora, conectamos ao Redis
r = redis.Redis(host='localhost', port=6379)

# O dataset utilizado é caracterizado por um conjunto de campos que representam os atributos de um jogo na Steam:
# app_id: int
# title: string
# date_release: string
# win: bool
# mac: bool
# linux: bool
# rating: float
# positive_ratio: float
# user_reviews: int
# price_final: float
# price_original: float
# discount: float
# steam_deck: bool

# Booleans não existem por padrão no RediSearch, então vamos mapeá-los para campos de texto

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

    """ [
        TextField('title', weight=5.0),
        TextField('date_release'),
        TextField('win'),c
        TextField('mac'),
        TextField('linux'),
        NumericField('rating'),
        NumericField('positive_ratio'),
        NumericField('user_reviews'),
        NumericField('price_final'),
        NumericField('price_original'),
        NumericField('discount'),
        TextField('steam_deck')
    ] """

    return schema

schema = map_json()

schema2 = (
    TextField("$.name", as_name="name"), 
    TagField("$.city", as_name="city"), 
    NumericField("$.age", as_name="age")
)

print(schema)
print(schema2)

# Agora, vamos criar o índice
rs = r.ft('idx:test')

rs.create_index(
    schema2, 
    definition=IndexDefinition(
        prefix=['tested:'], index_type=IndexType.JSON
    )
)


# Agora, vamos indexar o documento JSON
for i, game in enumerate(new_json):
    r.json().set(f'game:{i}', Path.root_path(), game)