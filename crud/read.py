from redis.commands.search.query import NumericFilter, Query
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers

import json
import redis.commands.search as Search

def get_average_temperature(result_json: dict, start_year: int, end_year: int) -> float:
    temperatures = []
    for year in range(start_year, end_year + 1):
        temperatures.append(result_json[str(year)])

    return sum(temperatures) / len(temperatures)

def get_max_temperature(result_json: dict, start_year: int, end_year: int) -> float:
    temperatures = []
    for year in range(start_year, end_year + 1):
        temperatures.append(result_json[str(year)])

    max_temperature = max(temperatures)
    # print(f"Temperatura máxima: {max_temperature} do ano {temperatures.index(max_temperature) + start_year} em {result_json['country']}")

    return max_temperature, temperatures.index(max_temperature) + start_year
    
def consulta1(redis_search_client: Search.Search):
    # Consulta 1
    # Obter a temperatura média entre 2012-2022 dos 10 países com maior densidade populacional e área maior que 1.000.000 km²

    query = Query("@area:[1000000 +inf]").sort_by("density", asc=False)

    # Executa a consulta
    result = redis_search_client.search(query).docs
    
    # Imprime o resultado
    print("\nTemperatura média entre 2012-2022 dos 10 países com maior densidade populacional e área maior que 1.000.000 km²")
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])
        print(f"{i + 1}º - {result_json['country']} - {doc['density']} (hab/km²) - {'{:,}'.format(int(result_json['area'])).replace(',', '.')} (km²)")

        print(f"Temperatura média entre 2012-2022: {'{:.2f}'.format(get_average_temperature(result_json=result_json, start_year=2012, end_year=2022))}°C\n")

def consulta2(redis_search_client: Search.Search):
    print("\n10 países com maiores temperaturas médias em 2022")
    print("----------------------------------------------")

    query = Query("*").sort_by("2022", asc=False)

    # Executa a consulta
    result = redis_search_client.search(query).docs

    # Imprime o resultado
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])
        print(f"{i + 1}º - {result_json['country']} - {'{:.2f}'.format(result_json['2022'])}°C")

def consulta3(redis_search_client: Search.Search):
    # Consulta 3
    # Obter os anos de maior temperatura média na região da Europa e Ásia Central (Europe & Central Asia)
    # É possível fazer uma comparação entre as regiões da América Latina e Caribe (Latin America & Caribbean)

    query = Query("@sub_region:Europe & Central Asia")

    # Executa a consulta
    result = redis_search_client.search(query).docs


    print("\nAnos de maior temperatura média na região da Europa e Ásia Central (Europe & Central Asia)")
    print("----------------------------------------------")
    # Imprime o resultado
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])

        max_temperature, max_temperature_year = get_max_temperature(result_json=result_json, start_year=1961, end_year=2022)

        print(f"{result_json['country']} - {'{:.2f}'.format(max_temperature)}°C em {max_temperature_year}")

def consulta4(redis_search_client: Search.Search):
    # Consulta 4
    # Obter a média de temperatura entre 2012-2022 dos países com grupo de renda "High income" e densidade populacional maior que 10
    # Obter a média de temperatura entre 2012-2022 dos países com grupo de renda "Low income"

    print("\nMédia de temperatura entre 2012-2022 de:")

    query = Query("@income_group:High income @density:[10 +inf]").sort_by("density", asc=False)

    # Executa a consulta
    result = redis_search_client.search(query).docs

    # Imprime o resultado
    print("\nPaíses com grupo de renda 'High income'")
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])

        print(f"{result_json['country']} - {'{:.2f}'.format(get_average_temperature(result_json=result_json, start_year=2012, end_year=2022))}°C")

    query = Query("@income_group:Low income @density:[10 +inf]").sort_by("density", asc=False)

    # Executa a consulta
    result = redis_search_client.search(query).docs

    # Imprime o resultado
    print("\nPaíses com grupo de renda 'Low income'")
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])

        print(f"{result_json['country']} - {'{:.2f}'.format(get_average_temperature(result_json=result_json, start_year=2012, end_year=2022))}°C")

def consulta5(redis_search_client: Search.Search):
    # Obter a média das temperaturas médias de 2012-2022 de países da Europa e Ásia Central (Europe & Central Asia)
    # Obter a média das temperaturas médias de 2012-2022 de países da América Latina e Caribe (Latin America & Caribbean)

    query = Query("@sub_region:Europe & Central Asia")

    # Executa a consulta
    result = redis_search_client.search(query).docs

    # Imprime o resultado
    print("\nTemperatura média entre 2012-2022")
    print("----------------------------------------------")
    
    temperatures = []
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])
        temperatures.append(get_average_temperature(result_json=result_json, start_year=2012, end_year=2022))

    print(f"Países da região 'Europe & Central Asia': {'{:.2f}'.format(sum(temperatures) / len(temperatures))}°C")

    query = Query("@sub_region:Latin America & Caribbean")

    # Executa a consulta
    result = redis_search_client.search(query).docs

    # Imprime o resultado
    temperatures = []
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])
        temperatures.append(get_average_temperature(result_json=result_json, start_year=2012, end_year=2022))

    print(f"Países da região 'Latin America & Caribbean': {'{:.2f}'.format(sum(temperatures) / len(temperatures))}°C")

def consulta6(redis_search_client: Search.Search):
    print("\nObter a contagem de países por grupo de renda")
    req =  aggregations.AggregateRequest("*").group_by('@income_group', reducers.count().alias('count'))
    print(redis_search_client.aggregate(req).rows)
    
    print("\nObter a contagem de países por sub-região")
    req =  aggregations.AggregateRequest("*").group_by('@sub_region', reducers.count().alias('count'))
    print(redis_search_client.aggregate(req).rows)

def consulta7(redis_search_client: Search.Search):
    # Consulta 7
    # Obter os anos mais quentes dos países do Mercosul (Argentina, Brasil, Paraguai, Uruguai)

    query = Query("@country:Argentina | @country:Brazil | @country:Paraguay | @country:Uruguay")

    # Executa a consulta
    result = redis_search_client.search(query).docs

    # Imprime o resultado
    print("\nAnos mais quentes dos países do Mercosul")
    print("----------------------------------------------")
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])

        max_temperature, max_temperature_year = get_max_temperature(result_json=result_json, start_year=1961, end_year=2022)

        print(f"{result_json['country']} - {'{:.2f}'.format(max_temperature)}°C em {max_temperature_year}")

    # Obter os anos mais quentes de países da União Europeia (Alemanha, Áustria, Bélgica, Bulgária, Chipre, Croácia, Dinamarca, Eslováquia, Eslovênia, Espanha, Estônia, Finlândia, França, Grécia, Hungria, Irlanda, Itália, Letônia, Lituânia, Luxemburgo, Malta, Países Baixos, Polônia, Portugal, República Tcheca, Romênia, Suécia)
        
    query = Query("(@country:Germany) | (@country:Austria) | (@country:Belgium) | (@country:Bulgaria) | (@country:Cyprus) | (@country:Croatia) | (@country:Denmark) | (@country:Slovakia) | (@country:Slovenia) | (@country:Spain) | (@country:Estonia) | (@country:Finland) | (@country:France) | (@country:Greece) | (@country:Hungary) | (@country:Ireland) | (@country:Italy) | (@country:Latvia) | (@country:Lithuania) | (@country:Luxembourg) | (@country:Malta) | (@country:Netherlands) | (@country:Poland) | (@country:Portugal) | (@country:Czech Republic) | (@country:Romania) | (@country:Sweden)")

    # Executa a consulta
    result = redis_search_client.search(query).docs

    # Imprime o resultado
    print("\nAnos mais quentes dos países da União Europeia")
    print("----------------------------------------------")
    for i, doc in enumerate(result):
        result_json = json.loads(doc['json'])

        max_temperature, max_temperature_year =  get_max_temperature(result_json=result_json, start_year=1961, end_year=2022)

        print(f"{result_json['country']} - {'{:.2f}'.format(max_temperature)}°C em {max_temperature_year}")

consultas = [consulta1, consulta2, consulta3, consulta4, consulta5, consulta6, consulta7]

def read(redis_search_client: Search.Search):
    consulta =  input('Escolha uma consulta - (1), (2), (3), (4), (5), (6), (7): ')

    if consulta not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Consulta inválida")
        return read(redis_search_client)
    
    consultas[int(consulta) - 1](redis_search_client)