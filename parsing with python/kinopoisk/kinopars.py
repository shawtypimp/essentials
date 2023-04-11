import requests

headers ={"X-API-KEY": "6HS5FAD-29KMK7C-GKG2V9H-BVWARJ0"}
#токен
def get_movies_by_year( type = 1, year = 2004, sort_field = "rating.imdb", sort_type = 1, select_fields = "rating.imdb, alternativeName", ):
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
    movies = response.json()
    return movies["docs"]

movies = get_movies_by_year()

movies1 = str(movies)
movies1 = movies1.replace("[", "")
movies1 = movies1.replace("]", "")
movies1 = movies1.replace("{", "")
movies1 = movies1.replace("}", "")
movies1 = movies1.replace(":", "")
movies1 = movies1.replace("names", "")
movies1 = movies1.replace("name", "")
movies1 = movies1.replace("'", "")
movies1 = movies1.replace("alternativeName", "")
movies2 = movies1.split(',')
#убираю все ненужные мне символы, чтобы красиво записать названия в файл

with open(r"C:movies.txt", "w", encoding="utf-8") as file:
    for name in movies2:
        file.write( name + '\n')
