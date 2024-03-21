import redis
from redis.commands.search.query import NumericFilter, Query
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers

import redis.commands.search as Search

def read(rs: Search.Search):
    # Primeiro, vamos criar um objeto Query
    query = Query("game")
    
    # Agora, vamos adicionar um filtro numérico
    query.add_filter(NumericFilter("positive_ratio", 80, 100))

    # Agora, vamos executar a query
    result = rs.search(query)
    
    # Vamos imprimir o resultado
    print(result)