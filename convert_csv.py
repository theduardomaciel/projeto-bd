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

# Primeiro, convertemos o arquivo CSV para um arquivo JSON
with open(csv_path, 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    # Alteramos o nome das colunas para que fiquem no formato snake_case
    field_names_formatted = [replace_special_chars(field) for field in reader.fieldnames]
    reader.fieldnames = field_names_formatted

    for row in reader:
        # Iteramos pelas configurações procurando por [field-names]
        field_names = dict(config.items('field-names'))
        for key in row:
            # Se o campo estiver presente no arquivo de configurações, convertemos o valor para o tipo especificado
            if key in field_names:
                if field_names[key] == 'int':
                    row[key] = int(row[key])
                elif field_names[key] == 'float':
                    row[key] = float(row[key])

        new_json.append(row)

print("Lendo o arquivo CSV...")

json_path = csv_path.replace('.csv', '.json')

# Agora, escrevemos o arquivo JSON, limitando a quantidade de elementos
with open(json_path, 'w') as json_file:
    json.dump(new_json[:max_elements], json_file, indent=4)

print("Arquivo JSON criado com sucesso!")