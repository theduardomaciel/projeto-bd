import redis
from redis.commands.search.query import NumericFilter, Query
import redis.commands.search.aggregation as aggregations
import redis.commands.search.reducers as reducers

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Now, let's search for games with a rating greater than 90
query = Query('rating:>90')
results = r.ft_search('idx', query)

# Now, let's print the results
print(f'Found {results.total} games with a rating greater than 90:')
for doc in results.docs:
    print(doc)

# Now, let's search for games with a rating greater than 90 and a positive ratio greater than 95
query = Query('rating:>90 @positive_ratio:>95')
results = r.ft_search('idx', query)

# Now, let's print the results
print(f'Found {results.total} games with a rating greater than 90 and a positive ratio greater than 95:')
for doc in results.docs:
    print(doc)

# Now, let's search for games with a rating greater than 90 and a positive ratio greater than 95, and sort the results by rating in descending order
query = Query('rating:>90 @positive_ratio:>95')
query.sort_by('rating', 'DESC')
results = r.ft_search('idx', query)

# Now, let's print the results
print(f'Found {results.total} games with a rating greater than 90 and a positive ratio greater than 95, sorted by rating in descending order:')
for doc in results.docs:
    print(doc)

# Now, let's search for games with a rating greater than 90 and a positive ratio greater than 95, and sort the results by rating in descending order, and limit the results to 10
query = Query('rating:>90 @positive_ratio:>95')
query.sort_by('rating', 'DESC')
query.limit(0, 10)
results = r.ft_search('idx', query)

# Now, let's print the results
print(f'Found {results.total} games with a rating greater than 90 and a positive ratio greater than 95, sorted by rating in descending order, limited to 10 results:')
for doc in results.docs:
    print(doc)

# Now, let's search for games with a rating greater than 90 and a positive ratio greater than 95, and sort the results by rating in descending order, and limit the results to 10, and return only the app_id and title fields
query = Query('rating:>90 @positive_ratio:>95')
query.sort_by('rating', 'DESC')
query.limit(0, 10)
query.return_fields('app_id', 'title')
results = r.ft_search('idx', query)

# Now, let's print the results
print(f'Found {results.total} games with a rating greater than 90 and a positive ratio greater than 95, sorted by rating in descending order, limited to 10 results, returning only the app_id and title fields:')
for doc in results.docs:
    print(doc)

# Now, let's search for games with a rating greater than 90 and a positive ratio greater than 95, and sort the results by rating in descending order, and limit the results to 10, and return only the app_id and title fields, and aggregate the results by the win field
query = Query('rating:>90 @positive_ratio:>95')
query.sort_by('rating', 'DESC')
query.limit(0, 10)
query.return_fields('app_id', 'title')
query.aggregate_by('win', aggregations.count('win'))
results = r.ft_search('idx', query)

# Now, let's print the results
print(f'Found {results.total} games with a rating greater than 90 and a positive ratio greater than 95, sorted by rating in descending order, limited to 10 results, returning only the app_id and title fields, and aggregating the results by the win field:')
for doc in results.docs:
    print(doc)