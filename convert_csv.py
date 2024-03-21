import csv
import json

new_json = []

csv_path = input('Enter the path of the CSV file: ')

# Primeiro, convertemos o arquivo CSV para um arquivo JSON
with open(csv_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        new_json.append(row)

print("Lendo o arquivo CSV...")

json_path = csv_path.replace('.csv', '.json')

# Agora, escrevemos o arquivo JSON
with open(json_path, 'w') as file:
    json.dump(new_json, file, indent=2)

print("Arquivo JSON criado com sucesso!")

""" # Now, let's convert the JSON file to a RedisJSON document
# using the JSON.SET command
r.json_set('data', Path.rootPath(), new_json)

# Now, let's create a RediSearch index on the JSON document
# using the FT.CREATE command
index_definition = IndexDefinition(prefix=['data'])
index_definition.add_field(TextField('name'))
index_definition.add_field(NumericField('age'))
index_definition.add_field(TagField('city'))
index_definition.index_type = IndexType.HASH
r.ft_create('idx', index_definition)

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
r.execute_command('MODULE UNLOAD', 'RediSearch') """