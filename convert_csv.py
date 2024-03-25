import re
import csv
import json
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

new_json = []

csv_path = input('Enter the path of the CSV file: ')
max_elements = int(input('Enter the maximum number of elements to be converted: '))

if not max_elements:
    max_elements = 1000

def replace_special_chars(string: str):
    return re.sub(r'\([^()]*\)', '', string).strip().replace(' ', '_').replace('-', '_').lower()

field_names = dict(config.items('field-names'))

# Primeiro, convertemos o arquivo CSV para um arquivo JSON
with open(csv_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    # Alteramos o nome das colunas para que fiquem no formato snake_case
    # Além disso, filtramos somente aquelas que estão presentes no arquivo de configurações
    for row in reader:
        new_row = {}
        for key in row:
            new_key = replace_special_chars(key)
            if new_key in config['field-names']:
                # Se o campo estiver presente no arquivo de configurações, convertemos o valor para o tipo especificado
                if field_names[new_key] == 'int':
                    new_row[new_key] = int(row[key])
                elif field_names[new_key] == 'float':
                    new_row[new_key] = float(row[key])
                else:
                    new_row[new_key] = row[key]
        new_json.append(new_row)

print("Lendo o arquivo CSV...")

json_path = csv_path.replace('.csv', '.json')

# Agora, escrevemos o arquivo JSON, limitando a quantidade de elementos
with open(json_path, 'w') as json_file:
    json.dump(new_json[:max_elements], json_file, indent=4)

print("Arquivo JSON criado com sucesso!")