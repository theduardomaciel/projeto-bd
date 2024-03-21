import redis

r = redis.Redis(host='localhost', port=6379)
rs = r.ft("idx:games")

import crud.read as read

crud_option = input('Choose a CRUD operation (C)reate, (R)ead, (U)pdate, (D)elete: ').upper()

if crud_option == 'C':
    # Create
    app_id = input('Enter the app ID: ')
    title = input('Enter the title: ')
    date_release = input('Enter the release date: ')
    win = input('Is it available for Windows? (True/False): ')
    mac = input('Is it available for Mac? (True/False): ')
    linux = input('Is it available for Linux? (True/False): ')
    rating = input('Enter the rating: ')
    positive_ratio = input('Enter the positive ratio: ')
    user_reviews = input('Enter the number of user reviews: ')
    price_final = input('Enter the final price: ')
    price_original = input('Enter the original price: ')
    discount = input('Enter the discount: ')
    steam_deck = input('Is it available for Steam Deck? (True/False): ')
    
    rs.add_document(
        app_id=app_id,
        title=title,
        date_release=date_release,
        win=win,
        mac=mac,
        linux=linux,
        rating=rating,
        positive_ratio=positive_ratio,
        user_reviews=user_reviews,
        price_final=price_final,
        price_original=price_original,
        discount=discount,
        steam_deck=steam_deck
    )

elif crud_option == 'R':
    # Read
    # Chamamos a função search presente no arquivo crud/search.py
    read.search(rs)

elif crud_option == 'U':
    # Update
    app_id = input('Enter the app ID: ')
    title = input('Enter the title: ')
    date_release = input('Enter the release date: ')
    win = input('Is it available for Windows? (True/False): ')
    mac = input('Is it available for Mac? (True/False): ')
    linux = input('Is it available for Linux? (True/False): ')
    rating = input('Enter the rating: ')
    positive_ratio = input('Enter the positive ratio: ')
    user_reviews = input('Enter the number of user reviews: ')
    price_final = input('Enter the final price: ')
    price_original = input('Enter the original price: ')
    discount = input('Enter the discount: ')
    steam_deck = input('Is it available for Steam Deck? (True/False): ')
    
    rs.add_document(
        app_id=app_id,
        title=title,
        date_release=date_release,
        win=win,
        mac=mac,
        linux=linux,
        rating=rating,
        positive_ratio=positive_ratio,
        user_reviews=user_reviews,
        price_final=price_final,
        price_original=price_original,
        discount=discount,
        steam_deck=steam_deck
    )

elif crud_option == 'D':
    # Delete
    app_id = input('Enter the app ID: ')
    rs.delete_document(app_id)

else:
    print('Invalid option!')

# Para executar este script, é necessário ter o Redis instalado e rodando na porta 6379