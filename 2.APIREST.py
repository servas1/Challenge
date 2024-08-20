import requests

def get_tv_series_data(page):
    url = f"https://jsonmock.hackerrank.com/api/tvseries?page={page}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

def bestInGenre(genre):
    page = 1
    best_show = None

    while True:
        data = get_tv_series_data(page)
        if not data or len(data['data']) == 0:
            break
        
        for series in data['data']:
            if genre.lower() in series['genre'].lower():
                # Verificamos si aún no hemos encontrado un "best_show" o si la serie actual tiene un rating IMDb mayor
                if best_show is None:
                    # Si aún no hemos seleccionado un "best_show", lo asignamos a la primera serie que cumpla el género
                    best_show = series
                elif series['imdb_rating'] > best_show['imdb_rating']:
                    # Si la calificación de IMDb de la serie actual es mayor que la del "best_show" actual, actualizamos "best_show"
                    best_show = series
                elif series['imdb_rating'] == best_show['imdb_rating']:
                    # Si ambas series tienen la misma calificación IMDb, elegimos la que tiene el nombre alfabéticamente menor
                    if series['name'] < best_show['name']:
                        best_show = series
                    
        page += 1
    
    if best_show:
        return best_show['name']
    else:
        return None

# Ejemplo de uso:
print(bestInGenre('Romance'))

