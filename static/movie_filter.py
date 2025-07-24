import sys
import requests
import random

API_KEY = "7ffcf763a3b33742ed91be959ba351cf"
THRESHOLD = 400.0
LANGUAGE = "pt-BR"
BASE_URL = "https://api.themoviedb.org/3/discover/movie"
MAX_PAGES = 300  # Ajuste conforme limite da API


def fetch_page(page: int) -> dict:
    """
    Faz a requisicao para uma pagina ordenada por popularidade.
    Retorna o JSON como dict ou encerra em caso de erro.
    """
    params = {
        "api_key": API_KEY,
        "language": LANGUAGE,
        "sort_by": "popularity.desc",
        "include_adult": "true",
        "page": page,
    }
    resp = requests.get(BASE_URL, params=params)
    if not resp.ok:
        print(f"Erro na requisicao (pagina {page}): {resp.status_code}")
        sys.exit(1)
    data = resp.json()
    return data


def main():
    # 1) Descobre total de paginas
    first = fetch_page(1)
    total_pages = min(first.get("total_pages", 1), MAX_PAGES)
    print(f"Total de paginas disponiveis: {total_pages}")

    # 2) Percorre paginas até achar resultados acima do limiar
    found = False
    for page in range(1, total_pages + 1):
        data = fetch_page(page)
        results = data.get("results", [])
        # Filtra filmes com popularidade >= THRESHOLD
        movies = [m for m in results if m.get("popularity", 0) >= THRESHOLD]
        if movies:
            print(f"Pagina {page} com {len(movies)} filmes acima do limiar.")
            selected = random.choice(movies)
            found = True
            break

    if not found:
        print(f"Nenhum filme com popularidade >= {
              THRESHOLD} encontrado em {total_pages} paginas.")
        return

    # 3) Exibe o filme selecionado
    title = selected.get("title", "Titulo desconhecido")
    lang = selected.get("original_language", "?")
    overview = selected.get("overview") or "Sem sinopse disponivel."
    popularity = selected.get("popularity", 0)
    poster = selected.get("poster_path")
    backdrop = selected.get("backdrop_path")

    print(f"Filme aleatorio popular: {title}")
    print(f"Lingua original: {lang}")
    print(f"Sinopse: {overview}")
    print(f"Popularidade (TMDB): {popularity}")
    if poster:
        print(f"Poster: https://image.tmdb.org/t/p/original{poster}")
    else:
        print("Sem poster disponivel.")
    if backdrop:
        print(f"Backdrop: https://image.tmdb.org/t/p/original{backdrop}")
    else:
        print("Sem banner disponivel.")


if __name__ == "__main__":
    main()
