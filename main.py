import redis

import crud.create as create
import crud.read as read
import crud.update as update
import crud.delete as delete

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

redis_index = input('Insira o nome do índice no Redis: (Enter para usar o padrão)')

if not redis_index:
    redis_index = config['DEFAULT']['REDIS_INDEX']
    if not redis_index:
        print('Nome do índice não encontrado no arquivo config.ini')
        exit()
    print(f'Usando o índice "{redis_index}" do arquivo config.ini')

r = redis.Redis(host='localhost', port=6379)
rs = r.ft(f"idx:{redis_index}")

def request_input():
    crud_option = input('Escolha uma operação CRUD - (C)reate, (R)ead, (U)pdate, (D)elete: ').upper()

    if crud_option.lower() == 'c':
        # Create
        # Chamamos a função create presente no arquivo crud/create.py
        create.create(r)

    elif crud_option.lower() == 'r':
        # Read
        # Chamamos a função search presente no arquivo crud/search.py
        read.read(rs)

    elif crud_option.lower() == 'u':
        # Update
        # Chamamos a função update presente no arquivo crud/update.py
        update.update(r)

    elif crud_option.lower() == 'd':
        # Delete
        # Chamamos a função delete presente no arquivo crud/delete.py
        delete.delete(r)

    else:
        print("Uma opção inválida foi escolhida. Por favor, tente novamente.")
        request_input()
    
request_input()