import redis
from redis.commands.json.path import Path
import random

def request_unit(allow_none=False):
    unit = input("Insira a unidade de medida de temperatura usada: [Celsius (C), Fahrenheit (F), Kelvin (K)] ")

    if allow_none and not unit:
        return None

    # print(f"Unidade de medida: {unit}")
    if unit not in ["C", "F", "K"]:
        print("Unidade de medida inválida")
        return request_unit()
    
    if unit == "C":
        return "Degree Celsius"
    
    if unit == "F":
        return "Degree Fahrenheit"
    
    if unit == "K":
        return "Kelvin"

def request_income_group(allow_none=False):
    income_group = input("Insira o grupo de renda do país: [Low income (1), Lower middle income (2), Upper middle income (3), High income (4)] ")

    if allow_none and not income_group:
        return None

    if income_group not in ["1", "2", "3", "4"]:
        print("Grupo de renda inválido")
        return request_income_group()
    
    if income_group == "1":
        return "Low income"
    
    if income_group == "2":
        return "Lower middle income"
    
    if income_group == "3":
        return "Upper middle income"
    
    if income_group == "4":
        return "High income"

sub_regions = [
    "Sub-Saharan Africa",
    "South Asia",
    "East Asia & Pacific",
    "North America",
    "Latin America & Caribbean",
    "Middle East & North Africa",
    "Europe & Central Asia",
]

def request_sub_region(allow_none=False):
    print("Sub-regiões disponíveis:")
    for i, sub_region in enumerate(sub_regions):
        print(f"{i + 1} - {sub_region}")

    sub_region = input("Insira a sub-região do país: ")

    if allow_none and not sub_region:
        return None

    if sub_region not in [str(i) for i in range(1, len(sub_regions) + 1)]:
        print("Sub-região inválida")
        return request_sub_region()
    
    sub_region = sub_regions[int(sub_region) - 1]
    
    return sub_region

def create(redis_client: redis.Redis):
    country = input("Insira o nome do país: ")

    iso3 = input("Insira o código ISO3 do país: ").upper()[0:3]

    unit = request_unit()

    sub_region = request_sub_region()

    income_group = request_income_group()

    area = float(input("Insira a área do país: (em km²)"))
    if not area.is_integer():
        print("A área do país deve ser um número inteiro")
        return create(redis_client)

    density = float(input("Insira a densidade populacional do país: (hab/km²)"))
    if not density.is_integer():
        print("A densidade populacional do país deve ser um número inteiro")
        return create(redis_client)

    new_country = {
         "country": country,
        "unit": unit,
        "sub_region": sub_region,
        "income_group": income_group,
        "area": area,
        "density": density,
    }

    # Iteramos pelo período de 1961-2022 inserindo as temperaturas médias anuais
    for year in range(1961, 2023):
        # Podemos solicitar a temperatura média anual de cada ano manualmente
        # temperatures[year] = float(input(f"Insira a temperatura média anual de {year}: "))

        # Ou gerar uma temperatura aleatória para cada ano
        new_country[year] = round(random.uniform(-2, 3), 2)
        print(f"Temperatura média anual de {year}: {new_country[year]}°C")

    redis_client.json().set(f"country:{iso3}", Path.root_path(), new_country)

    print(f"País '{country}' inserido com sucesso!")