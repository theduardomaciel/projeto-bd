import redis
from redis.commands.json.path import Path
import crud.create as create

def update(redis_client: redis.Redis):
    iso3 = input("Insira o código ISO3 do país que deseja atualizar: ")
    if not iso3:
        print("Código ISO3 inválido")
        return update(redis_client)
    
    data = redis_client.json().get(f"country:{iso3}")

    if not data:
        print(f"País com código ISO3 {iso3} não encontrado")
        return

    country = input("Insira o nome do país: (Enter para manter o mesmo) ")
    if country:
        data["country"] = country

    unit = create.request_unit(allow_none=True)
    if unit:
        data["unit"] = unit

    sub_region = create.request_sub_region(allow_none=True)
    if sub_region:
        data["sub_region"] = sub_region

    income_group = create.request_income_group(allow_none=True)
    if income_group:
        data["income_group"] = income_group

    area = input("Insira a área do país: (Enter para manter a mesma) ")
    if area:
        data["area"] = float(area)

    density = input("Insira a densidade populacional do país: (Enter para manter a mesma) ")
    if density:
        data["density"] = float(density)

    # Damos a possibilidade de inserir novos anos
    years = input("Insira os anos que deseja adicionar separados por vírgula: ")
    if years:
        for year in years.split(","):
            value = input(f"Insira o valor para o ano {year}: ")
            data[year] = float(value)

    # Atualizamos apenas os campos que foram preenchidos
    redis_client.json().set(f"country:{iso3}", Path.root_path(), data, nx=False, xx=True)

    print(f"País com código ISO3 {iso3} atualizado com sucesso!")