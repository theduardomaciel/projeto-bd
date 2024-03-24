import redis.commands.search as Search

def delete(rs: Search.Search):
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