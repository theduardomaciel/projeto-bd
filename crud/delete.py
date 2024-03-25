import redis

def delete(redis_client: redis.Redis):
    iso3 = input("Insira o código ISO3 do país que deseja excluir: ")
    redis_client.delete(f"country:{iso3}")

    print(f"País com código ISO3 {iso3} excluído com sucesso!")