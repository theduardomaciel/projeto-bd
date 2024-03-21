import redis
from redis.commands.json.path import Path
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers
from redis.commands.search.field import TextField, NumericField, TagField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import NumericFilter, Query

import json

new_json = []
json_path = input('Enter the path of the JSON file: ')

# Primeiro, lemos o arquivo JSON
with open(json_path, 'r') as file:
    new_json = json.load(file)

# Agora, conectamos ao Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Agora, vamos carregar os módulos RedisJSON e RediSearch
r.execute_command('MODULE LOAD', 'modules/redisjson.so')
r.execute_command('MODULE LOAD', 'modules/redisearch.so')

# Agora, vamos converter o JSON para um documento RedisJSON usando o comando JSON.SET
r.json_set('data', Path.rootPath(), new_json)

# The dataset used is made of games following the schema: app_id, title, date_release, win, mac, linux, rating, positive_ratio, user_reviews, price_final, price_original, discount, steam_deck. Everything is a string, but even some of them are string, they are going to be treated as numbers or booleans.

# Now, let's create a RediSearch index using the FT.CREATE command
schema = IndexDefinition(prefix=['game_'])
schema.add_field(TextField('app_id', sortable=True, no_stem=True))
schema.add_field(TextField('title', sortable=True))
schema.add_field(TextField('date_release', sortable=True))
schema.add_field(NumericField('win', sortable=True))
schema.add_field(NumericField('mac', sortable=True))
schema.add_field(NumericField('linux', sortable=True))
schema.add_field(NumericField('rating', sortable=True))
schema.add_field(NumericField('positive_ratio', sortable=True))
schema.add_field(NumericField('user_reviews', sortable=True))
schema.add_field(NumericField('price_final', sortable=True))
schema.add_field(NumericField('price_original', sortable=True))
schema.add_field(NumericField('discount', sortable=True))
schema.add_field(NumericField('steam_deck', sortable=True))

# Now, let's index the JSON document using the FT.ADD command
for i, doc in enumerate(new_json):
    r.ft_add('idx', f'doc_{i}', 1.0, 'FIELDS', 'data', doc)

# Now, let's search the index using the FT.SEARCH command
query = Query('name:John')
query.limit = 0 # We don't need the actual documents, just the count
result = r.ft_search('idx', query)
print(result.total_results)

# Now, let's aggregate the results using the FT.AGGREGATE command
query = Query('name:John')
query.load('name')
query.group_by('@city', reducers.count())
result = r.ft_aggregate('idx', query)
print(result)

# Now, let's delete the index using the FT.DROPINDEX command
r.ft_dropindex('idx')

# Now, let's delete the JSON document using the DEL command
r.delete('data')

# Now, let's delete the JSON file
os.remove('data.json')

# Now, let's delete the CSV file
os.remove('data.csv')

# Now, let's delete the RedisJSON module
r.execute_command('MODULE UNLOAD', 'RedisJSON')

# Now, let's delete the RediSearch module
r.execute_command('MODULE UNLOAD', 'RediSearch')