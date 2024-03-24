import redis

import crud.create as create
import crud.read as read
import crud.update as update
import crud.delete as delete

redis_index = input('Insira o nome do índice no Redis: ')

if not redis_index:
    exit('O nome do índice não pode ser vazio.')

r = redis.Redis(host='localhost', port=6379)
rs = r.ft(f"idx:{redis_index}")

crud_option = input('Escolha uma operação CRUD - (C)reate, (R)ead, (U)pdate, (D)elete: ').upper()

def request_input():
    if crud_option == 'C':
        # Create
        # Chamamos a função create presente no arquivo crud/create.py
        create.create(r)

    elif crud_option == 'R':
        # Read
        # Chamamos a função search presente no arquivo crud/search.py
        read.search(rs)

    elif crud_option == 'U':
        # Update
        # Chamamos a função update presente no arquivo crud/update.py
        update.update(r)

    elif crud_option == 'D':
        # Delete
        # Chamamos a função delete presente no arquivo crud/delete.py
        delete.delete(r)

    else:
        print("Uma opção inválida foi escolhida. Por favor, tente novamente.")
        request_input()