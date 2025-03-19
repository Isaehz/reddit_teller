from reddit import obtener_historias, guardar_historias

LIMIT_HISTORIAS = 2

if __name__ == "__main__":
    subreddit_url = input("Ingrese la URL del subreddit: ")
    if "/r/" in subreddit_url:
        subreddit_name = subreddit_url.split("/")[-2]
    
    historias = obtener_historias(subreddit_name, LIMIT_HISTORIAS)
    guardar_historias(historias, subreddit_name)

    for i, historia in enumerate(historias, 1):
        titulo = historia.get('title', f'Historia {i}')
        contenido = historia.get('content', '')
        print(f"{titulo}:\n{contenido}\n{'-'*40}")