import redis

def update(rs: redis.Redis):
    # Para atualizar um objeto JSON, precisamos primeiro recuperar o objeto
    app_id = input('Enter the app ID: ')
    
    # Agora, vamos recuperar o objeto JSON
    app = rs.get(app_id)

    # Agora, vamos atualizar o objeto JSON
    app['title'] = input('Enter the title: ')