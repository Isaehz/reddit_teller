import praw
import os
import random

def obtener_historias(subreddit, limite, min_caracteres=1100, max_caracteres=5000, orden='new'):
    """Obtiene historias de un subreddit con un mínimo y máximo de caracteres."""
    reddit = praw.Reddit(
        client_id='Tu ID',
        client_secret='Secret ID',
        user_agent='Tu agente de usuario'
    )
    
    historias = []
    ids_recolectados = set()
    if orden == 'new':
        posts = reddit.subreddit(subreddit).new(limit=limite*50)
    elif orden == 'top':
        posts = reddit.subreddit(subreddit).top(limit=limite*50)
    else:
        posts = reddit.subreddit(subreddit).hot(limit=limite*50)
    
    for post in posts:  # Obtener más historias para tener una mejor selección
        if post.id not in ids_recolectados and len(post.selftext) >= min_caracteres and (max_caracteres is None or len(post.selftext) <= max_caracteres):
            historia = {
                'title': post.title,
                'content': post.selftext
            }
            historias.append(historia)
            ids_recolectados.add(post.id)
            if len(historias) >= limite:
                break
    
    # Devolver solo el número de historias solicitado
    return historias

def guardar_historias(historias, subreddit):
    """Guarda las historias en un archivo de texto."""
    if not historias:
        print("No se encontraron historias que cumplan con la longitud mínima.")
        return

    carpeta_salida = "historias"
    os.makedirs(carpeta_salida, exist_ok=True)
    archivo_salida = os.path.join(carpeta_salida, f"{subreddit}.txt")
    
    with open(archivo_salida, "w", encoding="utf-8") as f:
        for i, historia in enumerate(historias, 1):
            f.write(f"{historia['title']}:\n{historia['content']}\n{'-'*40}\n")
    
    print(f"Historias guardadas en {archivo_salida}")