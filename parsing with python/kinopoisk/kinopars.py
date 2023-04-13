import requests

headers ={"X-API-KEY": "6HS5FAD-29KMK7C-GKG2V9H-BVWARJ0"}
#токен
def get_movies_by_year( type = 1, year = 2004, sort_field = "rating.imdb", sort_type = 1, select_fields = "rating.imdb, names" ):
    #сортирую фильмы по нужным мне параметрам
    response = requests.get(
        'https://api.kinopoisk.dev/v1/movie', 
        params={
        "typeNumber": type,
        "year": year,
        "sortField": sort_field,
        "sortType": sort_type,
        "selectFields": select_fields
        },
        headers=headers
    )
    #делаю запрос добавляя в него параметры
    
    raw_movies = {}
    for i in range(len(response.json()['docs'])):
        raw_movies[response.json()['docs'][i]['names'][0]['name']] = response.json()['docs'][i]['names'][0]['name']
    return raw_movies

raw_movies = get_movies_by_year()


with open(r"C:movies.txt", "w", encoding="utf-8") as file:
    file.write("Лучшие фильмы вышедшие в 2004 году, отсортировынные по рейтингу IMDB: " + '\n')
    for  key, value in raw_movies.items():
        file.write( value + '\n')
