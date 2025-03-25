import praw
import os
import random

def obtener_historias(subreddit, limite, min_caracteres=300, max_caracteres=1500, orden='hot'):
    """Obtiene historias de un subreddit con un mínimo y máximo de caracteres, sin repetirse, sin links y las más votadas."""
    reddit = praw.Reddit(
        client_id='EAhNUcnGpSMx9U4r_lz8yA',
        client_secret='gHbSkcy4tKIh-UyvCKReThSP2y8SAw',
        user_agent='story_teller'
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
            if 'http' not in post.selftext:  # Filtrar historias que no tengan links
                historia = {
                    'title': post.title,
                    'content': post.selftext,
                    'score': post.score
                }
                historias.append(historia)
                ids_recolectados.add(post.id)
                if len(historias) >= limite:
                    break
    
    # Ordenar las historias por el número de votos (score) en orden descendente
    historias.sort(key=lambda x: x['score'], reverse=True)
    
    # Devolver solo el número de historias solicitado
    return historias[:limite]

def guardar_historias(historias, subreddit):
    """Guarda las historias en un archivo de texto."""
    if not historias:
        print("No se encontraron historias que cumplan con la longitud.")
        return

    carpeta_salida = "/home/isael/proyecto_vid/historias"
    os.makedirs(carpeta_salida, exist_ok=True)
    archivo_salida = os.path.join(carpeta_salida, f"{subreddit}.txt")
    
    with open(archivo_salida, "w", encoding="utf-8") as f:
        for i, historia in enumerate(historias, 1):
            f.write(f"{historia['title']}:\n{historia['content']}\n{'-'*40}\n")
    
    print(f"Historias guardadas en {archivo_salida}")